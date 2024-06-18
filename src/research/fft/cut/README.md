# New-Cut-Approach für FFT

In diesem Verzeichnis wird der erste `cut`-Ansatz verwendet. Der Schnitt-Ansatz ist im zugehörigen
[Notebook](../../cut/cut.ipynb) sowie in der
[Dokumentation](../../../../doc/doc.md#erster-ansatz-cut) genauer erläutert.


## Untersuchte Modelle

In diesem Verzeichnis wurden die folgenden Modelle untersucht:

- [Perzeptron](./perceptron.ipynb)
- [Multi-layered Perzeptron](./mlp.ipynb) mit Hidden-Layer-Größe von `(30,30)`
- [Stochastic-Gradient-Descent](./sgd.ipynb)
- [Support-Vektor-Maschine](./svc.ipynb)


## Ergebnisse

Insgesamt kommen wir zu den folgenden Ergebnissen.

| Modell                           | Präzision | Recall | F1-Wert |
|----------------------------------|-----------|--------|---------|
| [Perzeptron](./perceptron.ipynb) | 65,45%    | 58,06% | 0,62    |
| [MLP](./mlp.ipynb) `(30,30)`     | 77,05%    | 75,81% | 0,76    |
| [SGD](./sgd.ipynb)               | 53,42%    | 62,90% | 0,58    |
| [SVM](./svc.ipynb)               | 82,93%    | 54,84% | 0,66    |
