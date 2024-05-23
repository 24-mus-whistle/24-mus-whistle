# Whistle Detection

## Context

Project for [C201.2](https://modulux.htwk-leipzig.de/modulux/modul/6325): Pattern Recognition held by [Prof Martin Grüttmüller](https://fim.htwk-leipzig.de/fakultaet/personen/professorinnen-und-professoren/martin-gruettmueller/)


## Usage

- Install Python 3.11
- Create and activate [virtual environment](https://docs.python.org/3/library/venv.html)
- Run `pip install -r src/requirements.txt`


## Note regarding the data

The data is not included in this repository due to licensing. The data is stored in `src/data` and includes `.flac` audio files and corresponding, identically named `.csv` files in which the labels are stored. The `csv` files include the start and end timestamp of the corresponding label (i.e. no whistle and whistle, respectively).

```csv
start,end,label
0.0,212.02452673542106,No_Whistle
212.02452673542106,212.37158719145785,Whistle
```
