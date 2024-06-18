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
    \lfloor t \rfloor, &\text{sonst}
  \end{cases}
  \\
  \texttt{end}(t) &= \begin{cases}
    \max \{ 0, \lfloor t \rfloor \}, &\left(t \bmod 1 \right) < \theta \\
    \lceil t \rceil, &\text{sonst}
  \end{cases}
\end{aligned}
$$

Die Implementierung kann unter
[src/research/cut/cut.ipynb](../src/research/cut/cut.ipynb) nachvollzogen werden. Dort ist in der
letzten Zelle erkennbar, dass insgesamt mehr Schnipsel als `whistle` markiert wurden, als
tatsächlich aus den originalen Daten hervorgegangen ist. Wir haben zunächst unsere Modell auf dieser
Basis trainiert. Da wir mit diesem Ansatz allerdings nicht gänzlich zufrieden waren, haben wir
später einen weiteren Ansatz konzipiert. Dieser wird im folgenden Abschnitt erläutert.


#### Zweiter Ansatz: `new_cut`

*TBA*

[`src/research/new_cut/new_cut.ipynb`](../src/research/new_cut/new_cut.ipynb)


## Features


## Modelle


## Ergebnisse

