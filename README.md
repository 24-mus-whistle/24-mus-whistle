# Whistle Detection

## Context

Project for [C201.2](https://modulux.htwk-leipzig.de/modulux/modul/6325): Pattern Recognition held by [Prof Martin Grüttmüller](https://fim.htwk-leipzig.de/fakultaet/personen/professorinnen-und-professoren/martin-gruettmueller/)


## Usage

- Install Python 3.11
- Create and activate [virtual environment](https://docs.python.org/3/library/venv.html)
- Run `pip install -r src/requirements.txt`


## Note regarding the data

The data is not included in this repository due to licensing. The data is stored in `src/data` and includes `.flac` audio files and corresponding, identically named `.csv` files in which the labels are stored. The `csv` files include the start and end timestamp of the corresponding label (i.e. no whistle and whistle, respectively).

`False_Whistle` labels segments which are whistles on a different court. The first model does only detect general whistles and does not differentiate between `Whistle` and `False_Whistle`.

```csv
start,end,label
62.35092589842589,68.25101351351351,No_Whistle
68.97197278911564,69.7730612244898,Whistle
70.05104024354024,91.55135951885953,No_Whistle
93.70139144639144,96.25142931392931,No_Whistle
96.90557823129251,97.14938775510204,False_Whistle
```
