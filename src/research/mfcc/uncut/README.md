# MFCC für ungeschnittene Daten

Dieses Verzeichnis enthält verschiedene Modelle, welche basierend auf dem MFCC-Feature trainiert
wurden.


## Vorverarbeitung der Daten

Da die Audio-Daten unterschiedlich lang sind und Numpy-Arrays homogene Dimensionen verlangen,
wurden die generierten Waveforms mit `0` ergänzt (*Padding*), sodass alle die gleiche Dimension
aufweisen. Anschließend wurde das MFCC-Feature für die aufgefüllten Audio-Daten erzeugt. Dies kann
im Notebook [`mfcc_generate.ipynb`](./mfcc_generate.ipynb) nachvollzogen werden.


## Untersuchte Modelle

Mit diesem Ansatz wurden die folgenden Modelle untersucht:

- [Perzeptron](./perceptron_mfcc.ipynb)
- [Stochastic Gradient Descent](./sgd_mfcc.ipynb) (SGD)
- [Support Vektor Maschine](./svc_mfcc.ipynb) (SVM)


## Ergebnisse

Insgesamt schnitten die Modelle wie folgt ab.

| Modell                                 | Präzision | Recall | F1-Score | Trainingszeit |
|----------------------------------------|-----------|--------|----------|---------------|
| [Perzeptron](./perceptron_mfcc.ipynb)  | 93,26%    | 100%   | 0,97     | 0,42s         |
| [SGD](./sgd_mfcc.ipynb)                | 93,26%    | 100%   | 0,97     | 0,35s         |
| [SVM](./svc_mfcc.ipynb)                | 95,40%    | 100%   | 0,98     | 0,85s         |
