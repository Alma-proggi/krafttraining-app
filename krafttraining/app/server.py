"""Krafttraining-Server für Home Assistant (Ingress).

Liefert die Web-App aus und speichert Dokumente in SQLite unter /data
(ist damit in den Home-Assistant-Backups enthalten).

API (relativ zum Ingress-Pfad):
  GET    api/rev                -> {"rev": n}  Änderungszähler zum günstigen Abfragen
  GET    api/<sammlung>         -> {"docs": [{"id", "data"}], "rev": n}
  PUT    api/<sammlung>/<id>    Dokument setzen (JSON-Body)
  DELETE api/<sammlung>/<id>    Dokument löschen
"""
import json, os, re, sqlite3, threading
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote

DATA = os.environ.get("KT_DATA", "/data")
WWW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "www")
PORT = int(os.environ.get("KT_PORT", "8099"))
# Nur der Ingress-Proxy des Supervisors darf zugreifen (Login über Home Assistant).
ALLOWED = set(filter(None, os.environ.get("KT_ALLOWED", "172.30.32.2,127.0.0.1").split(",")))
COLLECTIONS = {"workouts", "exercises"}
ID_RE = re.compile(r"^[A-Za-z0-9._-]{1,120}$")
STATIC = {"index.html": "text/html; charset=utf-8", "chart.umd.min.js": "application/javascript"}
MAX_BODY = 1_000_000

os.makedirs(DATA, exist_ok=True)
db = sqlite3.connect(os.path.join(DATA, "krafttraining.db"), check_same_thread=False)
db.execute("PRAGMA journal_mode=WAL")
db.execute("CREATE TABLE IF NOT EXISTS docs (coll TEXT, id TEXT, data TEXT, updated TEXT DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (coll, id))")
db.execute("CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY, v INTEGER)")
db.execute("INSERT OR IGNORE INTO meta VALUES ('rev', 0)")
db.commit()
lock = threading.Lock()

def rev():
    return db.execute("SELECT v FROM meta WHERE k='rev'").fetchone()[0]

class H(BaseHTTPRequestHandler):
    server_version = "Krafttraining/1.0"

    def log_message(self, fmt, *a):
        if os.environ.get("KT_LOG"):
            super().log_message(fmt, *a)

    def send(self, code, body=b"", ctype="application/json"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False, separators=(",", ":")).encode()
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def route(self):
        if self.client_address[0] not in ALLOWED:
            self.send(403, {"error": "forbidden"}); return None
        p = unquote(self.path.split("?")[0]).strip("/").split("/")
        return [x for x in p if x]

    def api_target(self, p):
        if len(p) < 2 or p[0] != "api" or p[1] not in COLLECTIONS: return None
        if len(p) == 2: return (p[1], None)
        if len(p) == 3 and ID_RE.match(p[2]): return (p[1], p[2])
        return None

    def do_GET(self):
        p = self.route()
        if p is None: return
        if not p or (len(p) == 1 and p[0] in STATIC):
            name = p[0] if p else "index.html"
            with open(os.path.join(WWW, name), "rb") as f:
                return self.send(200, f.read(), STATIC[name])
        if p == ["api", "rev"]:
            with lock: return self.send(200, {"rev": rev()})
        t = self.api_target(p)
        if not t or t[1] is not None: return self.send(404, {"error": "not found"})
        with lock:
            rows = db.execute("SELECT id, data FROM docs WHERE coll=? ORDER BY id", (t[0],)).fetchall()
            return self.send(200, {"docs": [{"id": i, "data": json.loads(d)} for i, d in rows], "rev": rev()})

    def do_PUT(self):
        p = self.route()
        if p is None: return
        t = self.api_target(p)
        if not t or t[1] is None: return self.send(404, {"error": "not found"})
        n = int(self.headers.get("Content-Length") or 0)
        if n <= 0 or n > MAX_BODY: return self.send(413, {"error": "size"})
        try:
            data = json.loads(self.rfile.read(n))
            assert isinstance(data, dict)
        except Exception:
            return self.send(400, {"error": "invalid json"})
        with lock:
            db.execute("INSERT OR REPLACE INTO docs (coll, id, data, updated) VALUES (?,?,?,CURRENT_TIMESTAMP)",
                       (t[0], t[1], json.dumps(data, ensure_ascii=False)))
            db.execute("UPDATE meta SET v=v+1 WHERE k='rev'"); db.commit()
            return self.send(200, {"ok": True, "rev": rev()})

    def do_DELETE(self):
        p = self.route()
        if p is None: return
        t = self.api_target(p)
        if not t or t[1] is None: return self.send(404, {"error": "not found"})
        with lock:
            db.execute("DELETE FROM docs WHERE coll=? AND id=?", t)
            db.execute("UPDATE meta SET v=v+1 WHERE k='rev'"); db.commit()
            return self.send(200, {"ok": True, "rev": rev()})

if __name__ == "__main__":
    print(f"Krafttraining läuft auf Port {PORT}, Daten in {DATA}")
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
