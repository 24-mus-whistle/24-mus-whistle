# Pfiff-Erkennung

<!-- Einführnug -->


## Dokumentation

Die resultierende Dokumentation kann unter [`doc/doc.md`](./doc/doc.md) eingesehen werden.
Ebenfalls sind die Beiträge der Einzelpersonen des Teams unter
[`doc/contributions.md`](./doc/contributions.md) aufgelistet.


## Kontext

Projekt für [C201.2](https://modulux.htwk-leipzig.de/modulux/modul/6325): Mustererkennung gehalten
von [Prof. Martin Grüttmüller](https://fim.htwk-leipzig.de/fakultaet/personen/professorinnen-und-professoren/martin-gruettmueller/)


## Reproduktion

- eigene Daten entsprechend der [src/data/README.md](src/data/README.md) einfügen
- Python 3.11 installieren
- [Virtual Environment](https://docs.python.org/3/library/venv.html) erstellen und aktivieren
- `pip install -r src/requirements.txt` ausführen


## Hinweis bzgl. der Daten

Die Daten sind aus Lizenz-Gründen nicht in diesem Repository enthalten. Die Dateien sind unter
`src/data` gespeichert und beinhalten `.flac` Audio-Dateien und zugehörige, identische benannte
`.csv`-Dateien, in welchen die Label gespeichert sind. Weitere Informationen können der zugehörigen
[README](src/data/README.md) im Daten-Verzeichnis eingesehen werden.
