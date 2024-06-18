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
dargestellt. Dabei ist zu erkennen, dass das Stochastische Gradientenverfahren zwar am besten
abschneidet. Allerdings sind die Werte nicht zufriedenstellend.

Weiterhin ist erkennbar, dass sowohl das MLP als auch die SVM Werte von jeweils 0 annehmen. Bei
genauerer Betrachtung ist erkenntlich, dass alle Test-Daten als "Kein-Pfiff enthalten" klassifiziert
werden.

| Modell                           | Präzision | Recall | F1-Score |
|----------------------------------|-----------|--------|----------|
| [Perzeptron](./perceptron.ipynb) | 25,00%    | 1,61%  | 0,03     |
| [MLP](./mlp.ipynb) `(100,)`      | 0,00%     | 0,00%  | 0,00     |
| [SGD](./sgd.ipynb)               | 33,33%    | 1,61%  | 0,03     |
| [SVM](./svc.ipynb)               | 0,00%     | 0,00%  | 0,00     |
