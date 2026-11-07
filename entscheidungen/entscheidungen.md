# Entscheidungen

## ADR-001 – Eigene App statt fertiger Lösung (07.11.2026)
- **Entscheidung:** Eigene Connect-IQ-App + eigene Web-App.
- **Warum:** Fertige Apps (Garmin-Krafttraining, Rack, Reckoner, LiftTrack) decken REQ-007 (Übungsvorschläge auf der Uhr) nach Recherche nicht ab; Rack kostet ein Abo.
- **Verworfen:** Garmin-Bordmittel (pro Satz nur ein festes Gewicht, keine Vorbelegung vom letzten Mal).

## ADR-002 – Web-App als claude.ai-Artifact mit Datenbank (07.11.2026)
- **Entscheidung:** Erste Version läuft als privates Artifact mit eingebauter Datenbank; nur Alexandra kann lesen und schreiben.
- **Warum:** Sofort nutzbar auf Mac und iPhone, kein eigener Server nötig, Claude kann die Daten lesen.
- **Offen:** Für den Abgleich mit der Uhr (REQ-202) braucht es vermutlich einen eigenen Dienst (NUC/Home Assistant oder Mac), weil die Uhr die Artifact-Datenbank nicht direkt erreicht.

## ADR-003 – 1RM-Formel (07.11.2026)
- **Entscheidung:** Standard Brzycki (Gewicht × 36 / (37 − Wdh.)), umschaltbar auf Epley. Aufwärmsätze zählen nicht.
- **Offen:** Welche Formel Strong nutzt, ist nicht belegt → mit Werten aus Strong vergleichen.

## ADR-004 – Datenmodell (07.11.2026)
- `workouts/<w-YYYYMMDDhhmmss>`: `{date, name, durMin, src, ex:[{n, rest, sets:[{t, w, r, rpe?}]}]}`
- Satztypen `t`: `N` normal, `W` Aufwärmen, `D` Drop-Satz, `F` bis Versagen (wie Strong).
- `exercises/<x-name>`: eigene Übungen `{name, cat, rest, custom}`.

## ADR-005 – Katzen-Animationen (Vorschlag, Entscheidung offen, 07.11.2026)
- **Vorschlag:** Ausschneide-Puppe pro Katze: aus dem Foto wenige Einzelteile (Kopf, Rumpf, Beine, Schwanz) als kleine Bitmaps mit reduzierter Farbpalette. Die Uhr setzt sie pro Bild neu zusammen (Graphics.AffineTransform + drawBitmap2, ab API 4.2.x). Übungen = Keyframes (Winkel/Positionen), gelten für alle drei Katzen. Ressourcen nur für die aktuelle Katze laden.
- **Verworfen:** fertige Bildfolgen pro Übung und Katze (OpenAI oder Monkey Motion): Speicherbedarf wächst mit Übungen × Katzen × Bildern, KI-Bilder kostenpflichtig und uneinheitlich.

### ADR-005 Nachtrag (07.11.2026): zwei Varianten parallel, Entscheidung am Ende durch Alexandra
Fotos: 3 Katzen (Bengal, schwarz, grau), alle frontal bzw. von oben, keine Seitenansicht.

| Variante | Inhalt | Speicher geschätzt (11 Übungen / 29 Übungen) |
|---|---|---|
| A Animation | gemeinsame gezeichnete Katzenfigur (Code), Farbe/Zeichnung je Katze, echtes Gesicht 64×64 px je Katze, Bewegungsdaten je Übung ~1 KB | ~35 KB / ~50 KB (3 Gesichter ~12 KB, Zeichencode ~10 KB, Keyframes) |
| B Einzelbild | ein Bild je Übung mit der zugeordneten Katze, 160×160 px, 256 Farben | ~280 KB / ~730 KB (je Bild ~25 KB; bei 64 Farben ~13 KB → ~145 KB / ~380 KB) |

Schätzwerte; echte Größen werden beim ersten Build gemessen und hier nachgetragen.
Verteilung der Katzen: feste, ausgeglichene Zuordnung (einmal mischen, reihum; neue Übung → Katze mit den wenigsten Übungen).

## ADR-006 – Web-App als Home-Assistant-App auf dem NUC, Updates über GitHub (07.11.2026)
- **Entscheidung:** Web-App läuft als eigene Home-Assistant-App (`krafttraining/`): Python-Server ohne Zusatzpakete, Daten in SQLite im App-Datenordner, Aufruf über die HA-Seitenleiste (Ingress). Dieses öffentliche Repo ist als App-Repository in HA eingetragen; Updates per Klick.
- **Warum:** Fernzugriff sofort über Nabu Casa, Anmeldung über HA, Daten in HA-Backups, kein offener Port, wenig Wartung, erweiterbar (später Uhr-Abgleich REQ-202 über HA-Webhook).
- **Verworfen:** eigener Docker-Dienst mit eigener Domain (unter HA OS nur über Umwege, mehr Wartung); Samba-Kopie (jedes Update manuell); privates Repo (GitHub-Schlüssel in HA, läuft ab).
- **Datenschutz:** Persönliche Daten (Strong-CSV, Katzenfotos) sind per `.gitignore` ausgeschlossen; Trainingsdaten liegen nur auf dem NUC.
- **Homescreen (REQ-107):** Empfehlung iOS-Kurzbefehl, der die HA-App auf „Krafttraining“ öffnet.
