# Data directory

The data is not included in this repository due to licensing.
The files are stored in this directory and include `.flac` audio files and corresponding, identically named `.csv` files in which the labels are stored.

```
src
├── data
│   ├── 01.csv
│   ├── 01.flac
│   ├── 02.csv
│   ├── 02.flac
...
```

The `csv` files include the start and end timestamp of the corresponding label (i.e. no whistle and whistle, respectively).
`False_Whistle` labels segments which are whistles on a different court.
The first model does only detect general whistles and does not differentiate between `Whistle` and `False_Whistle`.

```csv
start,end,label
62.35092589842589,68.25101351351351,No_Whistle
68.97197278911564,69.7730612244898,Whistle
70.05104024354024,91.55135951885953,No_Whistle
93.70139144639144,96.25142931392931,No_Whistle
96.90557823129251,97.14938775510204,False_Whistle
```


# Adding your data

Add your data to `src/data/your_data`. Then execute the following commands:

```sh
cd src/data
sh pre_process.sh your_data .
```

This makes sure that all `.flac` and `.csv` files are directly in `src/data` (i.e. not in a sub directory).
It also only takes files that are named as described above and that have both a `.flac` and a corresponding `.csv` file.
