# Analyse verschiedener Modelle mit MFCC-Feature

In diesem Ordner untersuchen wir die Leistung verschiedener Modelle, welche basierend auf dem
MFCC-Feature trainiert werden. Die Feature-Matrix und der Label-Vektor wurde dabei mittels dem
zweiten `new_cut`-Ansatz generiert, siehe
[`src/research/new_cut/new_cut.ipynb`](../../new_cut/new_cut.ipynb). Dieser ist in der
[Dokumentation](../../../../doc/doc.md#zweiter-ansatz-new_cut) genauer erläutert.


## Untersuchte Modelle

Es wurden die folgenden Modelle untersucht:

- [Perzeptron](./perceptron.ipynb)
- Multi-layered Perzeptron
    - [Notebook](./mlp.ipynb) mit Hidden-Layer-Size `(30,30)`
    - [Notebook](./mlp_layer/mlp_layer.ipynb) zur Untersuchung des Einflusses der Hidden Layer Size
- [Stochastic-Gradient-Descent](./sgd.ipynb)
- [Support-Vektor-Maschine](./svc.ipynb)


## Ergebnisse

In der folgenden Tabelle sind die Präzisions-, Recall- und F1-Werte der jeweiligen Modelle
dargestellt. Die Daten werden in der
[Dokumentation](../../../../doc/doc.md#zweiter-schnipsel-ansatz-new_cut) ausgewertet.

| Modell                           | Präzision | Recall | F1-Score | Trainingszeit |
|----------------------------------|-----------|--------|----------|---------------|
| [Perzeptron](./perceptron.ipynb) | 74,60%    | 64,38% | 0,69     | 1,49s         |
| [MLP](./mlp.ipynb) `(30,30)`     | 54,63%    | 80,82% | 0,65     | 11,25s        |
| [SGD](./sgd.ipynb)               | 57,84%    | 80.82% | 0,67     | 4,85s         |
| [SVM](./svc.ipynb)               | 0,00%     | 0,00%  | 0,00     | 12,11s        |
