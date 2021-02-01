Aufruf mittels:

argumente
 - f / --file	(pfad zur eingabe / template datei)
 - o / --output	(pfad zur ausgabedatei)
 - u / -- unit	(K oder C, C ist default)



python thersite.py -f <pfad-zur-txt.txt>
 -> gibt Ergebnis in Konsole aus

python thersite.py -f <pfad-zur-txt.txt> -o <pfad-zur-ausgabedatei>
 -> speichert Ergebnis am angebenen Pfad in angegebener Datei (wird überschrieben!)


python thersite.py -f <pfad-zur-txt.txt> -o <pfad-zur-ausgabedatei> -u C
 -> wie davor, aber temperatur ist in grad celsius!
