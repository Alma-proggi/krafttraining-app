# Krafttraining-App (Garmin fēnix 9 + Web-App)

Ersatz für die Strong-App im Gym: Training komplett über die Uhr, Auswertung in einer Web-App.

## Ablagesystem

| Ordner | Inhalt |
|---|---|
| `anforderungen/` | Anforderungen mit fester ID (REQ-xxx), Status und Herkunft |
| `entscheidungen/` | Technische Entscheidungen (ADR-xxx): was, warum, Alternativen |
| `umsetzung/` | Umsetzungsprotokoll: was wann gebaut wurde, Bezug auf REQ-IDs |
| `krafttraining/` | Web-App als Home-Assistant-App (Historie, Diagramme, 1RM, Übungen, Import); Seite: `krafttraining/app/www/index.html` |
| `uhr-app/` | Connect-IQ-App für die fēnix 9 (Monkey C) |
| `assets/katzen/` | Fotos der drei Katzen und daraus geschnittene Animationsteile (REQ-008) |
| `daten/` | Exporte und Rohdaten (z. B. Strong-CSV) |
| `tools/` | Hilfsskripte (z. B. Strong-CSV → JSON) |

## Regeln

- Jede neue Anforderung bekommt eine neue REQ-ID in `anforderungen/anforderungen.md`, nichts wird überschrieben, nur der Status ändert sich.
- Jede Umsetzung wird in `umsetzung/protokoll.md` mit Datum und REQ-IDs eingetragen.
- Statuswerte: `offen` · `in Arbeit` · `umgesetzt` · `getestet` · `verworfen`

## Links

- Web-App (privat): https://claude.ai/artifact/EuigKAoPifrpfXAzypNagv

## Installation auf Home Assistant

Einstellungen → Apps → App-Store → ⋮ → Repositories → `https://github.com/Alma-proggi/krafttraining-app` hinzufügen, dann „Krafttraining“ installieren und starten. Updates: Versionsnummer in `krafttraining/config.yaml` erhöhen, HA zeigt das Update an.
