# Pfiff-Erkennung

Die Robocup [Standard Platform League (SPL)](https://spl.robocup.org/) ist eine internationale Liga
im Roboterfußball. In dieser Liga treten Teams von verschiedenen Hochschulen und Universitäten
weltweit gegeneinader an. Verwendet wird dabei ein für alle Teams baugleicher Roboter vom Typ
[NAO](https://www.aldebaran.com/en/nao) der Firma [Aldebaran](https://www.aldebaran.com/en).

Die Spielregeln werden dabei kontinuierlich erweitert, um sich Stück für Stück den Regeln des
menschlichen Fußballs anzunähern. In diesem Zuge wurde eine neue Regeln eingeführt, die fordert,
dass die Roboter Pfiffe der Schiedsrichter:innen erkennen und darauf reagieren können sollen.

Das Team der [HTWK Robots](https://robots.htwk-leipzig.de/startseite) hat daher bereits Audiodaten
von vergangenen Spielen gesammelt und Labels dazu erstellt. Durch dieses Projekt, im Rahmen des
Moduls [Mustererkennung](https://modulux.htwk-leipzig.de/modulux/modul/6325), wird untersucht, wie
die Erkennung der Pfiffen mit Hilfe von Methoden der Mustererkennung durchgeführt werden können.


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
