# Gradientenabstiegsverfahren

In diesem Verzeichnis wird untersucht wie gut sich die Daten mithilfe des
Gradientenabstiegsverfahren (*Gradient Descent*, GD) trennen lassen. Dazu werden die Daten durch
eine FFT in ihre Frequenzanteile zerlegt. Anschließend werden bestimmte Frequenzbereiche isoliert
und versucht die Features "Mit Pfiff" und "Ohne Pfiff" durch GD zu Trennen. Dabei werden zuerst zwei
Frequenzbereiche gewählt um das Verfahren gut visualisieren zu können. Danach wird das gleiche
Verfahren für 10 Frequenzbereiche durchgeführt.


## Untersuchte Modelle

Im ersten Versuch [`split_gd`](./split_gd.ipynb) werden die Daten direkt eingelesen und anhand ihrer
Label geschnitten.

Im zweiten Versuch [`cut_gd`](./cut_gd.ipynb) wird der Ansatz aus
[`src/research/cut/cut.ipynb`](../cut/cut.ipynb) gewählt um die Audio-Dateien in gleich lange
Abschnitte zu unterteilen.


## Ergebnisse

Insgesamt kommen wir zu den folgenden Ergebnissen.

| Modell                           | Präzision | Recall | F1-Wert |
|----------------------------------|-----------|--------|---------|
| [Split 2D](./split.ipynb)        | 77.14%    | 87,10% | 0,81    |
| [Split 10D](./split.ipynb)       | 69,57%    | 84,21% | 0,76    |
| [Cut 2D](./cut_gd.ipynb)         | 68,22%    | 41,48% | 0,51    |
| [Cut 10D](./cut_gd.ipynb)        | 59,80%    | 34,66% | 0,43    |
