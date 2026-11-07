# Umsetzungsprotokoll

## 07.11.2026 – Web-App Version 1
- Strong-Export analysiert: 127 Trainings (18.11.2022–22.09.2026), 29 Übungen, Satztypen W/D/F, Pausenzeiten pro Übung ab 2025 enthalten.
- Web-App gebaut und als privates Artifact veröffentlicht: Übersicht, Verlauf, Übungsdetails mit Diagrammen (1RM, Höchstgewicht, Volumen), Rekorde nach Wiederholungen, letzte Einheit als Vorbelegung, Übungen anlegen, CSV-Import. → REQ-101 bis REQ-105
- Vorschau der Vorschlagslogik für die Uhr (Häufigkeit der letzten Wochen, Abstand zum letzten Training, typische Folgeübung). → REQ-007
- Projektstruktur angelegt (dieses Ablagesystem).

## 07.11.2026 – Klickdummy Uhr-App
- Klickdummy der fēnix-9-App gebaut: Übungsauswahl mit Vorschlägen, Sätze mit Vorbelegung aus der letzten Einheit, Gewicht/Wdh. per Tasten, Drop-Satz, Pausentimer mit Speicherung pro Übung, Trainingsabschluss. Daten aus dem Strong-Export. → REQ-009 (Entwurf für REQ-001 bis REQ-007)
- Datei: uhr-app/klickdummy/index.html, Artifact: https://claude.ai/artifact/BXiV8y3VvBAirvDrDppStA

## 07.11.2026 – Katzen REQ-008
- Fotos der drei Katzen erhalten. Zwei Varianten werden parallel verfolgt: Animation (A) und Einzelbild je Übung (B), Speicherschätzung siehe ADR-005 Nachtrag. → REQ-008

## 07.11.2026 – Web-App auf dem NUC (REQ-106)
- Home-Assistant-App `krafttraining/` gebaut: Server (Python-Standardbibliothek, SQLite in /data), Ingress, Seitenleiste „Krafttraining“. Chart.js lokal eingebunden.
- Web-App nutzt automatisch den eigenen Server, auf claude.ai weiterhin die Artifact-Datenbank.
- Lokal getestet: 127 Strong-Trainings importiert, Übung anlegen/löschen, Diagramme, keine Fehler.
- Fehler behoben: Ø Trainingsdauer zählte in Strong offen gelassene Trainings (bis 432 h) mit; jetzt nur Trainings bis 4 h.
- Repo auf GitHub angelegt (Alma-proggi/krafttraining-app), ADR-006.

## Nächste Schritte
1. Strong-CSV in der Web-App importieren und Werte (1RM) mit Strong vergleichen.
2. Projektordner auf den Mac übertragen.
3. Connect IQ SDK auf dem Mac installieren (nach Freigabe), Uhr-App im Simulator beginnen (REQ-001 bis REQ-006).
