# New-Cut-Approach für FFT

In diesem Verzeichnis wird der `new-cut`-Ansatz verwendet, zunächst ohne Berücksichtigung
des Verhältnisses von Pfiff-Nicht-Pfiff-Daten. Der Schnitt-Ansatz ist im zugehörigen
[Notebook](../../new_cut/new_cut.ipynb) genauer dokumentiert.


## Untersuchte Modelle

In diesem Verzeichnis wurden die folgenden Modelle untersucht:

- [Perzeptron](./perceptron.ipynb)
- Multi-layered Perzeptron
    - [Notebook](./mlp.ipynb) mit Hidden-Layer-Size `(30,30)`
    - [Notebook](./mlp_layer/mlp_layer.ipynb) zur Untersuchung des Einflusses der Hidden Layer Size
- [Stochastic-Gradient-Descent](./sgd.ipynb)
- [Support-Vektor-Maschine](./svc.ipynb)


## Ergebnisse

Insgesamt kommen wir zu den folgenden Ergebnissen.

| Modell                           | Präzision | Recall | F1-Wert |
|----------------------------------|-----------|--------|---------|
| [Perzeptron](./perceptron.ipynb) | 81,42%    | 78,08% | 0,80    |
| [MLP](./mlp.ipynb) `(30,30)`     | 86,57%    | 79,45% | 0,83    |
| [SGD](./sgd.ipynb)               | 85,71%    | 73,97% | 0,79    |
| [SVM](./svc.ipynb)               | 86,00%    | 58,90% | 0,70    |

Erwartungsgemäß schneidet das Multi-layered Perzeptron am besten ab. Außerdem ist erkennbar, dass
die anderen Modelle, v.a. im Vergleich zu [MFCC](../../mfcc/README.md), sehr gut abschneiden.
