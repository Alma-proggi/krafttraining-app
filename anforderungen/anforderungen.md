# Anforderungen

Herkunft aller Einträge: Vorgaben von Alexandra, 07.11.2026.

## Uhr-App (fēnix 9)

| ID | Anforderung | Status |
|---|---|---|
| REQ-001 | Training im Gym komplett über die Uhr, ohne Handy | offen |
| REQ-002 | Schnelle Auswahl einer Übung | offen |
| REQ-003 | Sätze erfassen, inklusive Drop-Sätze | offen |
| REQ-004 | Sätze werden mit den Werten des letzten Trainings dieser Übung vorbelegt | offen |
| REQ-005 | Schnelle Anpassung von Gewicht und Wiederholungen | offen |
| REQ-006 | Pausentimer; Einstellung wird pro Übung gespeichert und beim nächsten Training übernommen | offen |
| REQ-008 | Jede Übung hat eine Animation auf der Uhr: eine von Alexandras drei Katzen führt die Übung aus (Fotos liefert Alexandra), möglichst platzsparend – 07.11.2026 | offen, Weg siehe ADR-005 |
| REQ-007 | Bei der Übungsauswahl schlägt die Uhr anhand des Trainingsverlaufs die meistgenutzten/passendsten Übungen vor | in Arbeit (Logik als Vorschau in der Web-App) |
| REQ-009 | Für die Uhr-App zuerst einen Klickdummy erstellen, der bis zum ersten echten Build als Vorlage dient – 07.11.2026 | umgesetzt (uhr-app/klickdummy, Artifact) |
| REQ-010 | Cardio-Einheiten (z. B. 20 min Ergometer, Laufband) sind wie Kraftübungen auswählbar und werden mit Dauer erfasst – 07.11.2026 | offen, Weg siehe ADR-007 |
| REQ-011 | Kraft und Cardio in einem Gym-Besuch ohne App-Wechsel; in Garmin Connect möglichst als Multisport mit passender Sportart je Teil – 07.11.2026 | offen, Machbarkeit siehe ADR-007 |

## Web-App (oder iOS/macOS)

| ID | Anforderung | Status |
|---|---|---|
| REQ-101 | Komplette Historie aller Trainings | umgesetzt |
| REQ-102 | Diverse Diagramme und Auswertungen | umgesetzt (1. Version) |
| REQ-103 | Hochrechnung auf das maximale 1RM, identisch zu Strong | umgesetzt, Formel noch nicht gegen Strong geprüft |
| REQ-104 | Weitere Übungen anlegen | umgesetzt |
| REQ-105 | Übernahme der bisherigen Strong-Historie (CSV-Import) | umgesetzt |
| REQ-106 | Web-App läuft auf dem NUC (Home Assistant), Daten ohne Artifact-Datenbank, Zugriff auch außerhalb des Heimnetzes | in Arbeit |
| REQ-107 | Web-App als Icon auf dem iPhone-Homescreen aufrufbar | offen |

## Übergreifend

| ID | Anforderung | Status |
|---|---|---|
| REQ-201 | Möglichst wenig kostenpflichtige KI, Logik über feste Regeln | gilt |
| REQ-202 | Abgleich Uhr ↔ Web-App | offen |
