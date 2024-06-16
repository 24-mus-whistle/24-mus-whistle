# MFCC

In diesem Verzeichnis sind verschiedene Unterverzeichnisse enthalten, welche alle das MFCC-Feature
untersuchen, aber sich in der Datenbasis unterscheiden.

## `uncut`

Der erste Ansatz ist im `uncut`-Verzeichnis zu finden. Hier wurden die Audio-Dateien
unterschiedlicher Länge exakt so übernommen und nur anhand der Label geschnitten. Um auf die
gleiche Länge zu kommen, haben wir die Feature-Matrizen auf die gleiche Länge mithilfe des
Padding-Verfahrens manipuliert.

Wir kamen zum Ergebnis, dass die verschiedenen Modelle zwar gut funktionieren. Dies liegt aber
vermutlich daran, dass die Pfiff-Dateien erheblich kürzer sind. Somit mutmaßen wir, dass für die
gute Leistung es fast schon genügt, nur auf die Länge der Nicht-Null-Werte zu schauen. Aus diesem
Grund haben wir eine zweite Datenbasis untersucht.


## `cut`

Die zweite Datenbasis stellen geschnittene Audio-Dateien dar. Dabei haben wir diese auf jeweils
eine Sekunde geschnitten. Die Label wurden dabei basierend auf einem Threshold von $\theta = 0.1$
gerundet. Der Ansatz führte allerdings dazu, dass einige Sekunden, die tatsächlich einen Pfiff
enthielten, so gerundet wurde, dass das Endresultat dies nicht mehr tat.  Weitere Informationen
können dem zugehörigen [Notebook](../cut/cut.ipynb) entnommen werden.

Da wir mit diesem Ansatz nicht zufrieden waren, haben wir eine weitere Schneide-Methodik konzipiert.


## `new_cut`

In diesem Ansatz sind wir die Thematik des falsch-Labelns angegangen. Es wird erneut ein Threshold
definiert. Allerdings wird in diesem Ansatz “klüger” gerundet. Der Ansatz kann im zugehörigen
[Notebook](../new_cut/new_cut.ipynb) eingesehen werden.

Die Ergebnisse zeigen, dass die Modell hier im Vergleich zur `uncut`-Methodik miserabel abschneiden.
Unsere Hypothese war, dass ein Problem das Verhältnis zwischen den Schnipsel mit und ohne Pfiff
sind. Daher haben wir einen weiteren Ansatz ausprobiert.


## `new_cut_ratio`

Der finale Ansatz basiert auf der `new_cut`-Methodik. Allerdings werden die Daten ohne Pfiff
entsprechend eines Verhältnisses – spezifiziert durch den `ratio`-Parameter deutlich reduziert.
Dabei haben wir für die verschiedenen Modelle verschiedene Verhältnisse probiert und versucht zu
ermitteln, wo das Optimum liegt.

Der Ansatz und die Methodik werden in der zugehörigen [README](./new_cut_ratio/README.md) genauer
beschrieben. Wir kommen zu den Ergebnissen, dass es bei dem Modell der Support-Vektor-Maschine
zu einer Korrelation zwischen dem Verhältnis und der Leistung des Modells kommt. Bei den anderen
beiden Modellen (Perzeptron und Stochastic-Gradient-Descent) konnten wir dies allerdings nicht
feststellen.
