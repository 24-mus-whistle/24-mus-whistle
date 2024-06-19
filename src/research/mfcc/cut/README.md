# Analyse verschiedener Modelle mit MFCC-Feature

In diesem Ordner untersuchen wir die Leistung verschiedener Modelle, welche basierend auf dem
MFCC-Feature trainiert werden. Die Feature-Matrix und der Label-Vektor wurde dabei mittel dem
ersten `cut`-Ansatz generiert, siehe [`src/research/cut/cut.ipynb`](../../cut/cut.ipynb). Dieser ist
in der [Dokumentation](../../../../doc/doc.md#erster-ansatz-cut) genauer erläutert.


## Untersuchte Modelle

Es wurden die folgenden Modelle untersucht:

- [Perzeptron](./perceptron.ipynb)
- [Multi-layered Perzeptron](./mlp.ipynb) mit Hidden-Layer-Size `(100,)` (default)
- [Stochastic-Gradient-Descent](./sgd.ipynb)
- [Support-Vektor-Maschine](./svc.ipynb)


## Ergebnisse

In der folgenden Tabelle sind die Präzisions-, Recall- und F1-Werte der jeweiligen Modelle
dargestellt. Die Daten werden in der
[Dokumentation](../../../../doc/doc.md#erster-schnipsel-ansatz-cut) ausgewertet.

| Modell                           | Präzision | Recall | F1-Score | Trainingszeit |
|----------------------------------|-----------|--------|----------|---------------|
| [Perzeptron](./perceptron.ipynb) | 91,18%    | 50,00% | 0,65     | 1,25s         |
| [MLP](./mlp.ipynb) `(100,)`      | 54,32%    | 70,97% | 0,62     | 53,6s         |
| [SGD](./sgd.ipynb)               | 84,49%    | 51,61% | 0,65     | 6,14s         |
| [SVM](./svc.ipynb)               | 0,00%     | 0,00%  | 0,00     | 14,3s         |
