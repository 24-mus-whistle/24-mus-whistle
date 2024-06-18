# Erkennung von Pfiffen für NAO Robots

## Einleitung


## Datenbasis

### Initiale Daten

Initial haben wir die Daten vom *HTWK Robots*-Team erhalten. Das Paket beinhaltete verschiedene
Audio-Aufnahmen der Roboter, welche während diversen Spielen aufgenommen wurden. Diese lagen im
*Free Lossless Audio Codec* (`flac`) vor. Zu den meisten Audio-Dateien gab es eine entsprechende
CSV-Datei, welche die Label beinhaltet. Zugehörige Dateien sind (bis auf ihre Dateiendung) identisch
benannt. In diesem Projekt sind die Dateien unter `src/data` abgelegt. Die Dateistruktur sieht wie
folgt aus:

```
src
├── data
│   ├── 01.csv
│   ├── 01.flac
│   ├── 02.csv
│   ├── 02.flac
...
```

Die Label-Dateien beinhalten die folgenden Spalten: `start`, `end` und das entsprechende `label`
für den spezifizierten Zeitraum. Die Label unterscheiden sich dabei in drei Arten:

- `No_Whistle`: In dem Zeitraum war kein Pfiff zu hören
- `Whistle`: In dem Zeitraum war ein Pfiff zu hören
- `False_Whistle`: In dem Zeitraum war ein Pfiff zu hören, der allerdings zu einem anderen Feld
  gehört und daher nicht als Pfiff für den Roboter gilt.

Im Folgenden ist ein Beispiel für eine Label-Datei dargestellt.

```csv
start,end,label
62.35092589842589,68.25101351351351,No_Whistle
68.97197278911564,69.7730612244898,Whistle
70.05104024354024,91.55135951885953,No_Whistle
93.70139144639144,96.25142931392931,False_Whistle
```

Weiterhin haben wir uns dazu entschieden, zunächst `False_Whistle` nicht anders als `Whistle` zu
klassifizieren, um ein Grundverständnis für das Problem zu erhalten. Im Verlauf des Projekts hat
sich herausgestellt, dass wir die keine Zeit mehr für die Differenzierung zwischen diesen beiden
Labeln hatten.

Die Datenbasis können wir aus Lizenz- und Speichergründen nicht mit im Repository veröffentlichen.
Eine Anleitung, wie eigene Daten hinzugefügt werden können, ist in der 
[`src/data/README.md`](../src/data/README.md#adding-your-data) zu finden. Dabei ist ein Skript
zur Datenvorverarbeitung enthalten, welche im folgenden Abschnitt genauer erläutert wird.


### Vorverarbeitung der Rohdaten

Die Rohdaten enthielten teilweise Audio-Dateien ohne zugehörige Label-Datei oder vice versa.
Außerdem ist es im weiteren Verlauf wichtig gewesen, dass die Audio-Dateien exakt so wie die
Label- Dateien benannt sind. Teilweise existierten auch mehrere CSV-Dateien, welche sich auf
dieselbe Audio-Datei bezogen. Dabei sollen stets jene verwendet werden, die den `csv_new.csv`-Suffix
verwenden. Das Skript [`src/data/add_data.sh`](../src/data/add_data.sh) stellt diese
Anforderungen sicher.

Zunächst werden alle Daten, die ggf. in Unterverzeichnissen im spezifizierten *Source-Directory*
enthalten sind, in das Source-Directory verschoben. Falls es mehrere CSV-Dateien gibt, wird der
o.g. Anforderung entsprechend die neuere verwendet. Dafür wird die alte gelöscht und die neue
zur Datenstruktur passend umbenannt. Weiterhin werden alle Dateien gelöscht, die nicht sowohl eine
Audio-Datei als auch eine Label-Datei haben. Alle Dateien aus dem übergebenen Verzeichnis, welche
nicht auf `.flac` oder `.csv` enden, werden anschließend gelöscht. Schlussendlich werden die 
verbleibenden Dateien in das `src/data`-Verzeichnis verschoben und das Source-Directory gelöscht.
Somit sind die erforderlichen Daten im notwendigen Verzeichnis enthalten.


### Generierung der Grundmerkmale

Die Audio-Dateien wurden im Folgenden mittels der [`librosa`](https://librosa.org/)-Bibliothek
eingelesen. Die `librosa.load`-Funktion generiert eine Waveform, welche sie als `numpy`-Array
zurückgibt.

Das Einlesen der Label-Dateien haben wir mit der [`pandas`](https://pandas.pydata.org/)-Bibliothek
umgesetzt. Die Label wurden dann wie folgt auf die folgenden zwei Klassen abgebildet:

| Label           | Klasse |
|-----------------|--------|
| `No_Whistle`    | `-1`   |
| `Whistle`       | `+1`   |
| `False_Whistle` | `+1`   |

Zu Beginn des Projektes haben wir die Audio-Dateien nur anhand der Label-Datei geschnitten, d.h.
vom spezifizierten `start`-Wert bis zum `end`-Wert. Dieser Ansatz wird im Repository meist unter der
Bezeichnung `uncut` geführt.

Bei dem `uncut`-Ansatz war problematisch, dass die Waveform-Daten unterschiedlich lang sind. Ein
`numpy`-Array erwartet aber homogene Dimensionen. Daher haben wir den Ansatz des
[*Padding*](https://www.baeldung.com/cs/deep-neural-networks-padding) verwendet. Dies garantiert,
dass alle Daten die gleiche Dimension haben, in dem diese durch `0`-Werte ergänzt werden. Die
resultierenden Daten wurden als Basis verwendet, um verschiedene Features zu generieren (siehe
Abschnitt [Features](#features)).

Der Padding-Ansatz lieferte zwar gute Ergebnisse. Allerdings hatten wir die Vermutung, dass diese
durch den starken Unterschied von Pfiffen, die in der Regel sehr kurz (unter einer Sekunde) sind, im
Vergleich zu den `No_Whistle`-Abschnitten, welche in der Regeln eher lang sind. Aufgrund der
Null-Werte ist schnell und relativ zuverlässig erkennbar, ob es sich um eine Datei mit oder ohne
Pfiff handelt. Daher haben wir uns entschieden, weitere Ansätze zum Schneiden der Audio-Dateien
zu untersuchen. Diese werden im folgenden Abschnitt erläutert.


### Schnipsel-Ansätze

#### Erster Ansatz: `cut`

Der erste neue Ansatz zum Schneiden der Dateien sieht wie folgt aus. Jede Audio-Datei wird in
ein-sekündige Schnipsel geschnitten und entsprechend klassifiziert. Aus Beobachtungen der Rohdaten
wurde erkenntlich, dass die Pfiffe meistens kürzer als 0,4 Sekunden waren. Daraus folgerten wir,
dass wir die Start- und End-Zeiten nicht einfach runden können, da wir den Pfiff sonst verlieren
könnten und den Schnipsel falsch klassifizieren. Dies lässt sich am folgenden Beispiel darstellen:

$$
\begin{align}
  (\text{start},~\text{end}) &= (5.1,~5.4) \approx (5,~5) \\
  (\text{start},~\text{end}) &= (5.5,~5.9) \approx (6,~6)
\end{align}
$$

Hier ist zu erkennen, dass die beiden Zeiträume so gerundet wird, dass die Pfiffe in Sekunde 5
nicht als solche verarbeitet werden. Daher war unser erster Ansatz, einen Threshold $\theta = 0.1$
als Konstante einzuführen. Die Start- und Endwerte sollten dabei wie folgt gerundet werden.

$$
\begin{aligned}
  \texttt{start}(t) &= \begin{cases}
    \lceil t \rceil, &\left(t \bmod 1 \right) > 1 - \theta \\
    \max\left( 0, \lfloor t \rfloor\right), &\text{sonst}
  \end{cases}
  \\
  \texttt{end}(t) &= \begin{cases}
    \max\left( 0, \lfloor t \rfloor \right), &\left(t \bmod 1 \right) < \theta \\
    \lceil t \rceil, &\text{sonst}
  \end{cases}
\end{aligned}
$$

Die Implementierung kann unter
[`src/research/cut/cut.ipynb`](../src/research/cut/cut.ipynb) nachvollzogen werden. Dort ist in der
letzten Zelle erkennbar, dass insgesamt mehr Schnipsel als `whistle` markiert wurden, als
tatsächlich aus den originalen Daten hervorgegangen ist. Wir haben zunächst unsere Modell auf dieser
Basis trainiert. Da wir mit diesem Ansatz allerdings nicht gänzlich zufrieden waren, haben wir
später einen weiteren Ansatz konzipiert. Dieser wird im folgenden Abschnitt erläutert.


#### Zweiter Ansatz: `new_cut`

Das Ziel des zweiten Ansatzes war es, keine Daten in der Vorverarbeitung zu verfälschen. Ein
Mechanismus dafür war es, Pfiffe, die ungünstig zwischen zwei Sekunden liegen, zu löschen. Das
ursprüngliche Konzept ist in
[`src/research/new_cut/new_cut_approach.pdf`](../src/research/new_cut/new_cut_approach.pdf)
veranschaulicht und wird im Folgenden erklärt.

Zunächst haben wir erneut einen Threshold $\theta = 0.1$ festgelegt. Anschließend geht die Funktion
`cut_labels` (siehe [`src/research/new_cut/new_cut.ipynb`](../src/research/new_cut/new_cut.ipynb))
eine Label-Datei zeilenweise (d.h. entsprechend der definierten Intervalle) durch.

Zunächst legen wir ein Array an, welches exakt so lang ist, wie die Länge der Audio-Schnipsel für
diese Datei. Dieses wird mit dem Label für kein Pfiff initialisiert. Wenn das aktuell betrachtete
Intervall keinen Pfiff enthält, belassen wir das Label-Array an dem zugehörigen Index so. Falls
allerdings ein Pfiff enthalten ist, muss die Start- und Endzeit genauer betrachtet werden.

Zunächst bestimmen wir den Abstand des Startwertes von der (ganzen) Startsekunde
(`duration_end_sec`) und den Abstand des Endwertes zur Endsekunde (`duration_end_sec`). Wenn der
Abstand zur Startsekunde über dem Threshold $\theta = 0.1$ liegt, wird die ganze Startsekunde als
Pfiff gewertet, da hier ein hinreichender Pfiff zu hören ist. Falls dem nicht so ist, wird die
Startsekunde zu einem extra Array `to_remove` hinzugefügt. Alle Sekunden, die am Ende der Funktion
dort enthalten sind, werden im folgenden aus den Daten gelöscht.

Dies begründet sich darin, dass in der Sekunde ein Pfiff nur kürzer als der Threshold $\theta$ zu
hören ist. Da wir die markierten Daten nicht verfälschen wollten, haben wir diese entsprechend
entfernt. In der Praxis wäre es hier egal, wie das entsprechende Modell klassifiziert, sodass hier
kein Nachteil entstanden ist.

Selbiges wird mit dem Abstand zur Endsekunde durchgeführt. Ist dieser größer oder gleich dem
Threshold $\theta$, wird die Endsekunde als Pfiff markiert. Ansonsten wird diese als zu entfernen
markiert und im Folgenden aus dem Datensatz gelöscht.

Im zugehörigen [Notebook](../src/research/new_cut/new_cut.ipynb) ist ein Beispiel dafür aufgezeigt
– siehe Abschnitt *Debug print from `cut_labels`*. Dort ist zu sehen, dass die Daten wie von uns
erwartet und konzipiert markiert bzw. entfernt werden.


#### Dritter Ansatz: `new_cut_ratio`

Nach den Experimenten mit dem vorhergehenden Ansatz war zwar eine Verbesserung erkennbar. Allerdings
wurden dennoch viele Pfiffe als kein Pfiff klassifiziert. Nach einigen Überlegungen stellen wir die
These auf, dass das Verhältnis der Schnipsel ohne Pfiff im Vergleich zu den Ausschnitten mit Pfiff
ggf. einen Einfluss haben könnte. Wir haben insgesamt 120-Mal mehr Sekunden ohne Pfiff als mit,
siehe u.a. in diesem [Notebook](../src/research/mfcc/new_cut_ratio/perceptron.ipynb). Daher wollten
wir die Leistung der verschiedenen Modelle (siehe Abschnitt [Modelle](#modelle)) in Abhängigkeit von
verschiedenen Verhältnissen der Label untersuchen.

Da das MFCC-Feature wesentlich schneller zu generieren war als die FFTs – mehr dazu im folgenden
– [Abschnitt](#features) – entschieden wir uns, diesen Ansatz ausschließlich für erste zu
untersuchen. Den Ansatz zur Ermittlung des Bias kann in der
[`README`](../src/research/mfcc/new_cut_ratio/README.md#ansatz-für-ermittlung-des-bias) unter
`src/research/mfcc/new_cut_ratio` genauer nachgelesen werden. Die Ergebnisse werden im Abschnitt
[Ergebnisse](#ergebnisse) dargestellt.


## Features

Für das Projekt haben wir uns zwei verschiedene Feature überlegt: die *Fast Fourier-Transformation*
(FFT) und *Mel Frequency Cepstral Coefficients* (MFCC). Diese werden in den folgenden Abschnitten
kurz erläutert.


### Fast Fourier-Transformation

<!-- TODO: Johann: Erklärung -->


### Mel Frequency Cepstral Coefficients

Die Mel Frequency Cepstral Coefficients (MFCC) wurden zur Modellierung von Audio-Eigenschaften
entwickelt. Dabei werden die Dimensionen der Audio-Daten start reduziert ohne dabei wichtige
Eigenschaften zu verlieren. Dabei werden die Oberschwingungen (*Harmonics*) und die Seitenbänder
(*Sidebands*) des Signalspektrums extrahiert. Dabei soll das menschliche Gehör nachempfunden werden.
Dieses Feature ist in der Mustererkennung, v.a. bei der Stimmen- und Spracherkennung besonders
beliebt. Allerdings werden bei der Verkleinerung Informationen über die Tonlage (*Pitch*) 
verloren[^1][^2].

<!-- TODO: MFCC Bild für Whistle und No-Whistle -->

Im Verlauf des Projektes hat sich herausgestellt, dass sowohl die  MFCC-Generierung als auch das
Trainieren der verschiedenen Modelle zwar im Vergleich zur FFT sehr viel schneller funktioniert.
Allerdings waren die Ergebnisse wesentlich schlechter und meist für die Praxis unbrauchbar. Darauf
wird genauer im Abschnitt [Ergebnisse](#ergebnisse) eingegangen. Zunächst werden allerdings die
verschiedenen betrachteten Modelle erläutert.


## Modelle

Im Verlauf des Projektes haben wir unterschiedliche Modelle und Verfahren zur Klassifikation
trainiert. Diese stammten meist aus der Python-Bibliothek
[`scikit-learn`](https://scikit-learn.org/stable/index.html). Dabei haben wir uns vorrangig auf die
Modelle fokussiert, welche in dieser Lehrveranstaltung (Mustererkennung) sowie in der
Lehrveranstaltung *Numerische Methoden im Data Science und Machine Learning* von
[Prof. Patrick Kürschner](https://sites.google.com/view/patrickkuerschner/) vorgestellt wurden.

Insgesamt haben wir die folgenden Modelle untersucht:

- Perzeptron
- Multi-layered Perzeptron
- Gradientenverfahren (*Gradient Descent*, GD) (eigene Implementierung)
- Stochastisches Gradientenverfahren (*Stochastic Gradient Descent*, SGD)
- Support Vektor Maschine (SVM, *Support Vector Classifier*)

Die Modelle werden im folgenden Abschnitt ausgewertet.


## Ergebnisse


<!-- ------------------------------------------------------------------------------------------- -->

<!-- LITERATUR -->

[^1]: Z. Kh. Abdul und A. K. Al-Talabani, „Mel Frequency Cepstral Coefficient and its Applications:
      A Review“, _IEEE Access_, Bd. 10, S. 122136–122158, Nov. 2022, doi:
      [10.1109/ACCESS.2022.3223444](https://doi.org/10.1109/ACCESS.2022.3223444).

[^2]: F. Zheng, G. Zhang, und Z. Song, „Comparison of different implementations of MFCC“,
      _J. Comput. Sci. & Technol._, Bd. 16, Nr. 6, S. 582–589, Nov. 2001, doi:
      [10.1007/BF02943243](https://doi.org/10.1007/BF02943243).

