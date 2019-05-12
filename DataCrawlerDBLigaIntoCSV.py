import requests
import json
import csv

# while schleife von allen spieltagen; zählt alle SPieltage einer Saison hoch
def SpieltageCounter ():
     i = 1
     while i < 35:
         Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/2017/")+ str(i)
         r = requests.get(Spieltaglink)
         y = json.loads(r.text)
         AusgabeEinesSpieltages(y)
         i = i+1

# wertet einen Spieltag aus: whileschleife von 1 -9 für alle Spiele eines Spieltages; i= counter
def AusgabeEinesSpieltages (y):
    i = 0
    while i < 9:
        p = y[i]
        Spielliste(p)
        i =i+1

# Aufruf der Einzelnen Elemente welche für die csv Datei benötigt werden; und direktes Schreiben der csv Datei.
def Spielliste (p):
    # Datum aufrufen aus der Liste
    Datum = str(dict.get(p, "MatchDateTime"))
    # Aufrufen der Heimmanschaft
    a = dict.get(p, "Team1")
    b = dict.get(a, "TeamName")
    Heim = str(b)

    # aufrufen der Gastmannschaft
    c = dict.get(p, "Team2")
    d = dict.get(c, "TeamName")
    Gast = str(d)

    # ToreHeimTeam
    SpielErgebnis = dict.get(p, 'MatchResults')
    EndErgebnis = SpielErgebnis[1]
    ToreT1 = dict.get(EndErgebnis, 'PointsTeam1')
    ToreHeim = str(ToreT1)

    # ToreGastTeam
    SpielErgebnis = dict.get(p, 'MatchResults')
    EndErgebnis = SpielErgebnis[1]
    ToreT2 = dict.get(EndErgebnis, 'PointsTeam2')
    ToreGast = str(ToreT2)

    # ''ausgabe check ' alles SPiele in die Ausgabe zu Überprüfung; optional auschaltbar
    # diverse Tests für die Ausgabe
    print(dict.get(p, 'MatchID'))
    print(Datum)
    print(Heim)
    print(Gast)
    print(ToreHeim)
    print(ToreGast)

    #Match ID für die Initializierung der Spiele
    MatchID = (str(dict.get(p, 'MatchID')))
    # schreiben der Datei
    writer = csv.writer(open(MatchID, "w",))
    # writer.writerow([Datum, Heim, Gast, ToreHeim, ToreGast])

    # gewünschte daten als Liste anlegen
    ListeSpiel = list((Datum, Heim, Gast, ToreHeim, ToreGast))
    writer.writerow(ListeSpiel)


# aufruf der "main funktion des Crawlers"
SpieltageCounter()







