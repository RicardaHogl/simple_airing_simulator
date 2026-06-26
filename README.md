# Was ist das
Eine grobe Simulation, ob man beim manuellen Lüften an heißen Tagen, wie sie aktuell herrschen, eine Komfortverbesserung erwarten kann.


# Getting started
- Clone das Repository.
- Erstelle am besten eine neue virtuelle Umgebung, um bisherige Installationen nicht zu stören.
- Navigiere in der Kommandozeile auf den Ordner des Repositories.
- Installiere mit `pip install -r requirements.txt` die benötigten Bibliotheken. 
- Führe `python main.py` aus.

# Nutzung
Zunächst fragt das Tool ein paar Werte ab:
- Raumfläche
- Raumhöhe
- Windgeschwindigkeit der Außenluft
- Fenstergröße (Breite mal Höhe)
- Zahl der Personen im Raum
- \* und am wichtigsten für den Kern des Rechners: Für Innen und Außen jeweils Temperatur und Luftfeuchtigkeit
- \* sowie die Zeitdauer der Lüftung.

Werte mit \* sind Pflichtangaben, bei den anderen Angaben sind bereits Defaultwerte hinterlegt, die durch Drücken der Enter-Taste genutzt werden können.

Anschließend ermittelt das Tool für die Zeit vor der Lüftung, unmittelbar nach der Lüftung, und nach der Abkühlung der Außenluft die Feuchtkugeltemperatur.

Außerdem wird eine Empfehlung angegeben, wie oft man mindestens Lüften sollte, um eine hohe CO2-Konzentration zu vermeiden.

Außerdem wird ein Plot angezeigt, der für die Dauer des Lüftungsvorgangs den Verlauf von Lufttemperatur, Luftfeuchtigkeit und Feuchtkugeltemperatur prognostiziert.

# Annahmen

- kompletter Luftaustausch der warmen feuchten Innenluft durch heiße trockene Außenluft,
- die dann durch die Wände & Möbel auf "warm und eher trocken" herabgekühlt wird.
- Mit den Feuchtkugel-Temperaturen kann man dann abschätzen, wie angenehm sich das ganze anfühlt.


# Caveats
## Allgemein
Ein Großteil des Codes ist KI-generiert. Nach der Generierung gab es manuelle Verbesserungen beim Output und bei den Default-Werten. Ebenfalls habe ich eine sehr grobe Lüftungsempfehlung zur CO2-Reduktion (und dieses Readme ;) ) manuell hinzugefügt.
Ich habe nicht jede einzelne Rechnung überprüft, aber die Ergebnisse wirken für mich als relativer Laie auf dem Gebiet soweit recht plausibel.

## Einige Annahmen sind natürlich stark vereinfacht
-  während des Lüftens wird eine konstante Außentemperatur angenommen
- eine Temperaturveränderung von Möbeln&Wänden ist nicht mit 
berücksichtigt, diese werden mit einer konstanten Temperatur modelliert
- Möbel, die das Raumvolumen reduzieren, sind ebenfalls nicht eingeplant
- kein weiterer Feuchtigkeitseintrag während des Lüftens und Abkühlens der Luft
- bei einem kurzen Lüftvorgang wird nicht unbedingt die gesamte Luft ausgetauscht, Der Plot kann allerdings einen ersten Eindruck davon geben, wann ein Großteil der Feuchtigkeitsreduktion erreicht ist.

## Für den Plot des Temperatur/Luftfeuchtigkeitsverlauf gelten folgende Vereinfachungen
- die gesamte Fensterfläche steht zum Luftaustausch zur Verfügung, je nach Öffnungswinkel des Fensters würde sich diese reduzieren
## Für die CO2-Berechnung gilt
- es wurde eine sehr geringe Luftwechselrate von 0.3/h angenommen (entspricht den Verhältnissen bei modernen Fenstern)
- es wurde ein CO2-Eintrag von 18 l/h und Person angenommen. 
- die CO2-Berechnung beruht aus der Angabe auf [dieser Seite](https://mt-tech.ch/rechner/co2-kohlendioxid-konzentration-im-raum-berechnen/), nach welcher Zeit die 1000 ppm-Schwelle erreicht wird, wobei ich die Zeit zum Erreichen der Schwelle bei Raumvolumina, die vom Referenzvolumen abweichen, linear skaliere. Belegungen >6 Personen sind in dem Tool nicht eingeplant. 


# Hintergrund
(zumindest, wie ich ihn als weitgehender Noob in der Gebäudephysik verstehe)

Die Belastung an heißen Tagen entsteht nicht allein durch eine hohe Luftemperatur, sondern ebenfalls durch eine hohe Luftfeuchtigkeit. Wenn bereits viel Wasserdampf in der Luft ist, kann der Schweiß von unserer Haut nicht mehr gut verdampfen - aber genau durch das Verdampfen des Schweißes von unserer Haut entsteht erst ein Kühlungseffekt.
Mithilfe der sogenannten Feuchtkugeltemperatur kann man grob abschätzen, bis zu welcher Temperatur man die Haut durch Schwitzen abkühlen kann.

Durch die bloße Existenz als Mensch in einem geschlossenen Raum erhöht man jedoch zwangsläufig mit der Zeit die Luftfeuchtigkeit (durch Schwitzen und unseren Atem).
Mit der gängigen Empfehlung: "An heißen Tagen erst lüften, wenn es draußen kühler als drinnen ist" erhält man zwar eine relativ konstante Lufttemperatur, aber durch die steigende Luftfeuchtigkeit erhöht sich auch die Feuchtkugeltemperatur - und dieser Wert ist für unser Wohlbefinden entscheidend.

Bei den in Mitteleuropa üblichen Wetterlagen mit einer heißen & trockenen Außenluft gilt daher stattdessen:
Wenn drinnen eine hohe Luftfeuchtigkeit herrscht, sollte man schon kurz lüften, um so die Luftfeuchtigkeit zu verringern. 
Zwar steigt dadurch die Raumtemperatur kurz an, jedoch verringert sich unmittelbar die Luftfeuchtigkeit. Da die Raumtemperatur in den Wänden und Möbeln noch "gespeichert" ist, verringert sich nach dem Ende des Lüftvorgangs mit der Zeit auch wieder die Lufttemperatur. 
Die absolute Feuchtigkeit bleibt konstant, da kühlere Luft jedoch insgesamt weniger Wasserdampf aufnehmen kann, steigt die relative Luftfeuchtigkeit wieder leicht an.
Mit diesem Rechner kann man abschätzen, welche relative Luftfeuchtigkeit und Feuchtkugeltemperatur sich unmittelbar nach dem Lüften, und nach der Wiederherstellung der ursprünglichen Temperatur einstellt.

Durch den menschlichen Atem steigt außerdem die CO2-Konzentration im Raum an - je mehr Menschen "mitatmen", desto schneller geschieht der Anstieg. Eine hohe CO2-Konzentration kann ebenfalls zu Unwohlsein führen, weshalb auch aus diesem Grund regelmäßig gelüftet werden sollte. 

Deswegen enthält dieser Rechner auch eine grobe Abschätzung, in welchen Zeitintervallen eine Lüftung mindestens erfolgen sollte.
