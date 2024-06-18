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
    - [Notebook](./mlp_layer.ipynb) zur Untersuchung des Einflusses der Hidden Layer Size
- [Stochastic-Gradient-Descent](./sgd.ipynb)
- [Support-Vektor-Maschine](./svc.ipynb)


## Ergebnisse

In der folgenden Tabelle sind die Präzisions-, Recall- und F1-Werte der jeweiligen Modelle
dargestellt. Dabei ist zu erkennen, dass die Werte vom MLP und der SVM jeweils 0 annehmen. Bei
genauerer Betrachtung ist erkenntlich, dass alle Test-Daten als "Kein-Pfiff enthalten" klassifiziert
werden. Auch wenn die anderen beiden Modelle überhaupt Pfiffe als solche identifizieren, schneiden
diese dennoch sehr schlecht ab.

| Modell                           | Präzision | Recall | F1-Score |
|----------------------------------|-----------|--------|----------|
| [Perzeptron](./perceptron.ipynb) | 12,50%    | 2,74%  | 0,04     |
| [MLP](./mlp.ipynb) `(30,30)`     | 0,00%     | 0,00%  | 0,00     |
| [SGD](./sgd.ipynb)               | 8,11%     | 4,11%  | 0,05     |
| [SVM](./svc.ipynb)               | 0,00%     | 0,00%  | 0,00     |
