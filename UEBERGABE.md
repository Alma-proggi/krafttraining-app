# Übergabe für das Claude-Projekt „Krafttraining-App“ (Stand 07.11.2026)

## Ziel
Strong-App im Gym ersetzen: Training komplett über die Garmin fēnix 9 (eigene Connect-IQ-App), Auswertung in einer Web-App. Möglichst ohne kostenpflichtige KI.

## Wo liegt was
- Projektordner: ~/Documents/krafttraining-app (Mac mini), Ablagesystem siehe README.md
- Web-App V1 (privates Artifact mit Datenbank): https://claude.ai/artifact/EuigKAoPifrpfXAzypNagv
- Strong-Export: daten/strong_workouts_2026-11-07.csv (127 Trainings, 29 Übungen, 2022-11 bis 2026-09)

## Stand
- Web-App umgesetzt: Historie, Diagramme, 1RM (Brzycki/Epley umschaltbar), Rekorde, Übungen anlegen, CSV-Import, Vorschau der Übungsvorschläge für die Uhr.
- Strong-CSV muss Alexandra noch in der Web-App importieren (Einstellungen → Strong-Export importieren).
- 1RM-Formel noch nicht gegen Strong geprüft.

## Offen / nächste Schritte
1. Katzenfotos (3 Katzen, je Seite + Gesicht, mit Namen) nach assets/katzen/ → Vorschau einer Katze bei Bankdrücken (REQ-008, ADR-005: Ausschneide-Puppe mit AffineTransform/drawBitmap2).
2. Connect IQ SDK auf dem Mac installieren (Freigabe nötig), Uhr-App REQ-001 bis REQ-007.
3. Abgleich Uhr ↔ Web-App (REQ-202), vermutlich eigener Dienst auf NUC/Home Assistant oder Mac.

## Arbeitsregeln
- Neue Anforderungen als REQ-xxx in anforderungen/anforderungen.md, Entscheidungen als ADR-xxx, jede Umsetzung ins Protokoll.
- Schreibende Änderungen an Mac oder Home Assistant nur nach Freigabe.
