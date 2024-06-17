# Analyse des Bias bzgl. Pfiff-kein-Pfiff-Verhältnis

In diesem Ordner untersuchen wir die Auswirkung des Verhältnisses zwischen dem Verhältnis
der Daten ohne Pfiff im Vergleich zu den Daten mit Pfiff. Dies begründet sich durch die Tatsache,
dass wir insgesamt 120-mal mehr Daten ohne Pfiff haben als mit Pfiff. Daher erwarten wir
unterschiedliche Ergebnisse basierend auf dem Verhältnis.


## Datenbasis der Untersuchung

Als Basis verwenden wir den "New-Cut-Approach". In diesem schneiden wir die vorhanden Audio-Dateien
in Abschnitte, die jeweils 1 Sekunde lang sind. Die Label werden entsprechend den Label-CSVs
eingelesen und mit Hilfe eines Thresholds von $\Theta = 0.1$ gerundet. Weitere Informationen dazu
können unter dem zugehörigen [Notepad](../../new_cut/new_cut.ipynb) eingesehen werden. Dieses
muss initial ausgeführt werden, bevor die anderen Notepads ausgeführt werden können.

Für diese Abschnitte wurde jeweils das MFCC-Feature generiert. Das zugehörige
[Notebook](./mfcc_generate.ipynb) muss dabei vor der Ausführung der anderen Notebooks ebenfalls
ausgeführt werden, um die Feature-Matrix und den Label-Vektoren initial zu generieren. Diese werden
anschließend in diesem Verzeichnis als
[Numpy-Datei](https://numpy.org/doc/stable/reference/routines.io.html) gespeichert und von den
Notebooks, die die Modelle untersuchen, wieder eingelesen.


## Ansatz für Ermittlung des Bias

Um den Bias zu ermitteln wurde eine [`reduce_and_reshuffle`-Funktion](./helper.py) eingeführt.
Diese erhält eine Feature-Matrix (bspw. FFT- oder MFCC-Daten) und den dazugehörigen Label-Vektor.
Weiterhin wird ein `ratio`-Parameter übergeben, welcher das Verhältnis der Daten ohne Pfiff zu den
Daten mit Pfiff spezifiziert.

```py
def reduce_and_reshuffle(X, y, ratio):
    # ...
    return X_new, y_new
```

Der `ratio`-Parameter ist dabei wie folgt zu verstehen:

$$\verb|ratio| = \frac{\vert\text{no-whistle}\vert}{\vert\text{whistle}\vert}$$

Dementsprechend bedeutet eine `ratio` von `1 / 1`, dass gleich viele Daten mit und ohne Pfiff
in der resultierenden reduzierten Feature-Matrix enthalten sein sollen. Eine `ratio` von `n / 1`
würde hingegen bedeuten, dass $n$-mal mehr Daten ohne Pfiff als mit Pfiff enthalten sein sollen.

Die Funktion unterscheidet zunächst zwischen Daten ohne und mit Pfiff. Alle Daten mit Pfiff sollen
in der zurückgegebenen Feature-Matrix wieder enthalten sein. Die Feature ohne Pfiff sollen so
reduziert werden, dass sie dem in `ratio` spezifizierten Verhältnis entsprechen. Die Wahl der
Indizes, welche übernommen werden sollen, geschieht dabei zufällig. Um das Ergebnis reproduzierbar
zu gestalten, wird der Random-State entsprechend einer `RANDOM_STATE`-Konstante zu Beginn der
jeweiligen Notepads festgelegt.

Die Funktion gibt schlussendlich die neue Feature-Matrix mit dem entsprechendem Label-Vektor
zurück. Dabei sind bei einem Verhältnis von $m : n$ insgesamt $n+m$ Features enthalten.


## Untersuchte Modell und Ergebnisse

In diesem Ordner wurden die folgenden verschiedenen Modelle untersucht:

- [Perzeptron](./perceptron.ipynb)
- [Multi-layered Perzeptron](./mlp.ipynb) mit Hidden-Layer-Size `(30,30)`
- [Stochastic-Gradient-Descent](./sgd.ipynb)
- [Support-Vektor-Maschine](./svc.ipynb)

Die Ergebnisse sind in den jeweiligen verlinkten Notebooks zu finden. Insgesamt scheint allerdings
ausschließlich bei der Support-Vektor-Maschine eine tatsächliche Korrelation zwischen dem Verhältnis
der Label und den Leistungsmetriken der Modelle vorhanden zu sein. Weiterhin schließt dieses Modell
mit einer Präzision von 100% bei einem Recall von 8,22% am besten ab.

| Modell                           | Verhältnis | Präzision | Recall | F1-Score |
|----------------------------------|------------|-----------|--------|----------|
| [Perzeptron](./perceptron.ipynb) | 59:1       | 17,31%    | 12,33% | 0,14     |
| [MLP](./mlp.ipynb) `(30,30)`     | 94:1       | 100%      | 1,37%  | 0,03     |
| [SGD](./sgd.ipynb)               | 47:1       | 14,86%    | 15,07% | 0,15     |
| [SVM](./svc.ipynb)               | 21:1       | 100%      | 8,22%  | 0,15     |
