from sqlalchemy import exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
import tkinter as tk
import requests
import datetime
import numpy as np
from scipy.optimize import minimize_scalar
from math import factorial

#Erstellen der Datenbank
Base = declarative_base()  # Erstellen der Basis


class Spiele(Base):
    __tablename__ = "spiele"

    id = Column(Integer, primary_key=True, unique=True)
    Datum = Column(String)
    Heim = Column(String)
    Gast = Column(String)
    ToreHeim = Column(Integer)
    ToreGast = Column(Integer)

    def __init__(self, MatchID, Datum, Heim, Gast, ToreHeim, ToreGast):
        self.id = MatchID
        self.Datum = Datum
        self.Heim = Heim
        self.Gast = Gast
        self.ToreHeim = ToreHeim
        self.ToreGast = ToreGast


engine = create_engine('sqlite:///Bundesliga_Ergebnisse_DB.db')
Base.metadata.create_all(engine)  # Erstellen der Datenbbank
Base.metadata.bind = engine  # Binden der Engine
Session = sessionmaker(bind=engine)  # Erstellen der Sitzung
session = Session()
Spiel_zugriff = session.query(Spiele).all()
# Zugriff um einzelene Daten abzufragen

session.commit()  # abschließende Aktualisierung


# Testaufruf einzelner Key eines Spiels
# Teste alle matchid`s Überprüfung auf doppelte ID`s
# Test eines Beispiels
def testeinesSpiels(d):
    print(Spiel_zugriff[d].id)
    print(Spiel_zugriff[d].Heim)
    print(Spiel_zugriff[d].ToreHeim)
    print(Spiel_zugriff[d].Gast)
    print(Spiel_zugriff[d].ToreGast)


#Globale Variablen berechnen
'''
Funktion berechneAktuelleSaison findet das Jahr der aktuellen Saison gemäß openligadb.de
arguments: none
returns: jahr (int)
'''


def berechneAktuelleSaison():
    now = datetime.datetime.now()  # aktuelles Datum
    jahr = now.year
    monat = now.month
    # je nach dem, ob es vor oder nach Juli ist,
    #ist man in verschiednenen Saisons
    if monat >= 7:
        return jahr
    else:
        return jahr-1


# beziehe Daten der Startseite unserer Datenquelle
r = requests.get("https://www.openligadb.de/api/getmatchdata/bl1/")
y = json.loads(r.text)
p = y[0]

'''
Funktion oldMatchIsFinished überprüft ob auf der
Startseite der aktuelle spieltag angezeigt wird
arguments: none
returns: boolean
'''


def oldMatchIsFinished():
    global p
    a = dict.get(p, "MatchIsFinished")
    if (a == True):
        return True
    else:
        return False


'''
Funktion berechneAktuellerSpieltag berechnet den heutigen Spieltag
arguments: none
returns: aktueller Spieltag
'''


def berechneAktuellerSpieltag():
    global p
    a = dict.get(p, "Group")
    spieltag = dict.get(a, "GroupOrderID")
    b = oldMatchIsFinished()
    if (b == True):
        return spieltag
    else:
        if (spieltag - 1) > 0:
            return (spieltag - 1)
        else:
            global aktuellesJahr
            aktuellesJahr = aktuellesJahr - 1
            return 34


'''
Funktion berechneKommenderSpieltag berechnet den nächsten Spieltag
arguments: none
returns: kommender Spieltag
'''


def berechneKommenderSpieltag():
    if aktuellerSpieltag < 34:
        return (aktuellerSpieltag + 1)
    else:
        global aktuellesJahr
        aktuellesJahr = aktuellesJahr + 1
        return 1


AnzahlSpieleGesamt = session.query(Spiele).count()
aktuellesJahr = berechneAktuelleSaison()
aktuellerSpieltag = berechneAktuellerSpieltag()
kommenderSpieltag = berechneKommenderSpieltag()

#Funktionen für Crawler-Button
'''
Funktion CrawlHelper ruft die Funktion CrawlHelper
und aktualisiert danach das GUI-Fenster
arguments: none
returns: none
'''


def CrawlHelper():
    Spieltagsjahre()
    gui.Window.update()
    gui.Window.mainloop()


'''
Funktion Spieltagsjahre ruft für jedes Saisonjahr....?
arguments: none
returns: none
'''


def Spieltagsjahre():
    i = 2009
    while i < aktuellesJahr:
        Saisonlink ="https://www.openligadb.de/api/getmatchdata/bl1/" + str(i) + "/"
        SpieltageCounter(Saisonlink)
        i = i + 1


'''
Funktion SpieltageCounter zählt alle Spieltage einer Saison hoch
arguments: Saisonlink
returns: none
'''


def SpieltageCounter(a):
    i = 1
    while i < 35:
        Spieltaglink = (a) + str(i)
        r = requests.get(Spieltaglink)
        y = json.loads(r.text)
        AusgabeEinesSpieltages(y)
        i = i + 1
    session.commit()


'''
Funktion AusgabeEinesSpieltages wertet einen Spieltag
aus für alle neun Spiele eines Spieltages
arguments: ?
returns: none
'''


def AusgabeEinesSpieltages(y):
    for p in y:
        Spielliste(p)


'''
Funktion Spielliste ruft die einzelnen Elemente auf,
welche für die Datenbank benötigt werden
arguments: ?
returns: none
'''


def Spielliste(p):
    # Datum aufrufen aus der Liste
    Datum_L = str(dict.get(p, "MatchDateTime"))
    # Aufrufen der Heimmanschaft
    a = dict.get(p, "Team1")
    b = dict.get(a, "TeamName")
    Heim_L = str(b)

    # Aufrufen der Gastmannschaft
    c = dict.get(p, "Team2")
    d = dict.get(c, "TeamName")
    Gast_L = str(d)

    # ToreHeimTeam
    SpielErgebnis = dict.get(p, 'MatchResults')
    EndErgebnis = SpielErgebnis[1]
    ToreT1 = dict.get(EndErgebnis, 'PointsTeam1')
    ToreHeim_L = str(ToreT1)

    # ToreGastTeam
    SpielErgebnis = dict.get(p, 'MatchResults')
    EndErgebnis = SpielErgebnis[1]
    ToreT2 = dict.get(EndErgebnis, 'PointsTeam2')
    ToreGast_L = str(ToreT2)
    # Match ID entschlüsseln
    MatchID_L = (dict.get(p, 'MatchID'))

    # ''ausgabe check ' alle Spiele in die Ausgabe
    #zu Überprüfung, optional auschaltbar
    # diverse Tests für die Ausgabe
    print(dict.get(p, 'MatchID'))
    # print(Datum_L)
    # print(Heim_L)
    # print(Gast_L)
    # print(ToreHeim_L)
    # print(ToreGast_L)

    # erstellen der Spieldatei welche später in die Datenbank eingefügt wird
    Spiel_allgemein = Spiele(MatchID=MatchID_L, Datum=Datum_L, Heim=Heim_L,
    Gast=Gast_L, ToreHeim=ToreHeim_L, ToreGast=ToreGast_L)

    # Check ob das aktuell erstellte Spiel bereits
    #in der Datenbank enthalten ist
    ret = session.query(exists().where(Spiele.id == MatchID_L)).scalar()
    if(ret == True):
        pass
    else:
        session.add(Spiel_allgemein)  # falls nicht hinzufügen des Spiels

    session.commit()  # aktualisieren der Datei


#Funktionen für Trainingsbutton
'''
Funktion Schnittstelle berechnet die Indizes um auf
Teildatensatz zugreifen zu können, bei fehlerhafter
Eingabe wird die Liste (-1,-1) ausgegeben
arguments: Saisonjahr v Spieltag w, ab dem die Daten ausgewählt werden sollen
Saisonjahr x Spieltag y, bis zu dem die Daten ausgewählt werden sollen
returns: Liste, die die Indizes untereSchranke und obereSchranke enthält
'''


def Schnittstelle(v, w, x, y):
    if v < 2009 or v > aktuellesJahr or x < 2009 or x > aktuellesJahr or w < 1 or y < 1 or w > 34 or y > 34:
        return (-1, -1)
    else:
        untereSchranke = (v - 2009) * 306 + (w - 1) * 9
        obereSchranke = (x - 2009) * 306 + (y - 1) * 9 + 8
        # UntereID= Spiel_zugriff[untereSchranke].id
        # ObereID= Spiel_zugriff[obereSchranke].id
        print(AnzahlSpieleGesamt)
        if ((AnzahlSpieleGesamt - 1) < obereSchranke) or (obereSchranke < untereSchranke):
            return (-1, -1)
        return (untereSchranke, obereSchranke)


#Funktion für Dropdown-Listen
'''
Funktion crawlTeams holt die Namen der Teams aus der Datenbank
arguments: Jahr (int), Spieltag (int)
returns: Liste der Teamnamen
'''


def crawlTeams(Jahr, Spieltag):
    # enthält Teams einer Saison
    TeamListe = []

    # externe Daten
    Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(Spieltag)

    # holt externe Daten eines Spieltages
    r = requests.get(Spieltaglink)
    y = json.loads(r.text)

    # geht alle Begegnungen des Spieltages durch

    for p in y:
        # Speichere jeweils die Heimmanschaft
        a = dict.get(p, "Team1")
        b = dict.get(a, "TeamName")
        Heim = str(b)
        TeamListe.append(Heim)

        # Speichere jeweils die Gastmannschaft
        c = dict.get(p, "Team2")
        d = dict.get(c, "TeamName")
        Gast = str(d)
        TeamListe.append(Gast)
    return TeamListe


#Funktion für Label des kommenden Spieltages
'''
Funktion resultString erzeugt String, der das
wahrscheinlichste Ergebnis und die Wahrscheinlichkeiten
für Heimsieg, Auswärtssieg und Unentschieden enthält
arguments: Team1 (String, Name Heim), Team2 (String, Name Gast), Alg(String, Vorhersagealg.)
returns: String
'''


def resultString(Team1, Team2, Alg):

    if (Alg == "minimal"):
        Liste = Gewinnwahrscheinlichkeit(Team1, Team2)
    elif (Alg == "poisson"):
        Liste = poissonWahrscheinlichkeit(Team1, Team2)

    if (int(Liste[0]) + int(Liste[2]) + int(Liste[1]) < 10):
        return "keine Daten in der Datenbank"

    if (Liste[0] > 90 or Liste[2] > 90 or Liste[1] > 90):
        return "keine Daten in der Datenbank"

    elif Liste[0] >= Liste[1] and Liste[0] >= Liste[2]:
        return str(Liste[0]) + "% " + "Heimsieg: " + str(Liste[0]) + "% - " + str(Liste[1]) + "% - " + str(Liste[2]) + "% "

    elif Liste[2] >= Liste[0] and Liste[2] >= Liste[1]:
        return str(Liste[2]) + "% " + "Gastsieg: " + str(Liste[0]) + "% - " + str(Liste[1]) + "% - " + str(Liste[2])  + "% "

    elif Liste[1] >= Liste[0] and Liste[1] >= Liste[2]:
        return str(Liste[1]) + "% " + "Remis: " + str(Liste[0]) + "% - " + str(Liste[1]) + "% - " + str(Liste[2]) + "% "

    else:
        return "keine Daten in der Datenbank"


#Funktion für Gewinnwahrscheinlichkeits-Button
'''
Funktion Gewinnwahrscheinlichkeit berechnet die Wahrscheinlichkeiten
der Teams für Gewinn Heim, Unentschieden, Gewinn Gast
arguments: Team1 (Heim), Team2 (Gast)
returns: ErgebnisWahrscheinlichkeiten
(dreielementige Liste, die die Gewinnwhkt von Team1, Unentschieden,
Gewinnwhkt von Team2 enthält)
'''


def Gewinnwahrscheinlichkeit(Team1, Team2):
    SiegTeam1 = 0
    UnentschiedenTeam1 = 0
    NiederlageTeam1 = 0
    SiegTeam2 = 0
    UnentschiedenTeam2 = 0
    NiederlageTeam2 = 0

    i = 0
    indexSpiel = AnzahlSpieleGesamt - 1  # Indexfunktion

    while i < 5:

        indexSp = (indexSpiel - (i * 9))
        j = 0
        while j < 9:
            if (Spiel_zugriff[indexSp - j].Heim == Team1):
                if(Spiel_zugriff[indexSp - j].ToreHeim > Spiel_zugriff[indexSp - j].ToreGast):
                 SiegTeam1 = SiegTeam1 + 1
                if(Spiel_zugriff[indexSp - j].ToreHeim == Spiel_zugriff[indexSp - j].ToreGast):
                    UnentschiedenTeam1 = UnentschiedenTeam1 + 1
                if (Spiel_zugriff[indexSp - j].ToreHeim < Spiel_zugriff[indexSp - j].ToreGast):
                    NiederlageTeam1 = NiederlageTeam1 + 1

            if (Spiel_zugriff[indexSp - j].Gast == Team1):
                if (Spiel_zugriff[indexSp - j].ToreGast > Spiel_zugriff[indexSp - j].ToreHeim):
                    SiegTeam1 = SiegTeam1 + 1
                if (Spiel_zugriff[indexSp - j].ToreGast == Spiel_zugriff[indexSp - j].ToreHeim):
                    UnentschiedenTeam1 = UnentschiedenTeam1 + 1
                if (Spiel_zugriff[indexSp - j].ToreGast < Spiel_zugriff[indexSp - j].ToreHeim):
                    NiederlageTeam1 = NiederlageTeam1 + 1

            if (Spiel_zugriff[indexSp - j].Heim == Team2):
                if (Spiel_zugriff[indexSp - j].ToreHeim > Spiel_zugriff[indexSp - j].ToreGast):
                    SiegTeam2 = SiegTeam2 + 1
                if (Spiel_zugriff[indexSp - j].ToreHeim == Spiel_zugriff[indexSp - j].ToreGast):
                    UnentschiedenTeam2 = UnentschiedenTeam2 + 1
                if (Spiel_zugriff[indexSp - j].ToreHeim < Spiel_zugriff[indexSp - j].ToreGast):
                    NiederlageTeam2 = NiederlageTeam2 + 1

            if (Spiel_zugriff[indexSp - j].Gast == Team2):
                if (Spiel_zugriff[indexSp - j].ToreGast > Spiel_zugriff[indexSp - j].ToreHeim):
                    SiegTeam2 = SiegTeam2 + 1
                if (Spiel_zugriff[indexSp - j].ToreGast == Spiel_zugriff[indexSp - j].ToreHeim):
                    UnentschiedenTeam2 = UnentschiedenTeam2 + 1
                if (Spiel_zugriff[indexSp - j].ToreGast < Spiel_zugriff[indexSp - j].ToreHeim):
                    NiederlageTeam2 = NiederlageTeam2 + 1

            j = j + 1

        i = i + 1

    # test der einzelnen counter
    # print(SiegTeam1)
    # print(UnentschiedenTeam1)
    # print(NiederlageTeam1)
    # print(SiegTeam2)
    # print(UnentschiedenTeam2)
    # print(NiederlageTeam2)

    if ((SiegTeam1 + SiegTeam2 + UnentschiedenTeam1 + UnentschiedenTeam2 + NiederlageTeam1 + NiederlageTeam2) == 10):
        Siegwahrscheinlichkeit_Team1 = ((SiegTeam1 + NiederlageTeam2) / 10 * 100)
        Unentschiedenwahrscheinlichkeit = (
            (UnentschiedenTeam1 + UnentschiedenTeam2) / 10 * 100)
        Siegwahrscheinlichkeit_Team2 = ((SiegTeam2 + NiederlageTeam1) / 10 * 100)
        ErgebnisWahrscheinlichkeiten = list(
            (Siegwahrscheinlichkeit_Team1, Unentschiedenwahrscheinlichkeit, Siegwahrscheinlichkeit_Team2))
        return ErgebnisWahrscheinlichkeiten

    else:
        return list((0, 0, 0))


'''
Funktion crawlTore packt die Tore die zwei Mannschaften gegeneinander geschossen haben in eine Matrix
arguments: Heim (String), Gast (String)
returns: numpy array
'''


def crawlTore (Heim, Gast):
    HeimListe = []
    GastListe = []

    for x in Spiel_zugriff:
        if ((x.Heim == Heim) and (x.Gast == Gast)):
            HeimListe.append(x.ToreHeim)
            GastListe.append(x.ToreGast)

    toreMatrix = np.array([HeimListe, GastListe])
    return toreMatrix


'''
Funktion neg_llh definiert eine log-Likelihood-Funktion
arguments: Variable theta, Matrix y
returns: negative log-Likelihood-Funktion
'''

def neg_llh(theta, y):
    f = np.sum(y * theta - np.exp(theta))
    return -f


'''
Funktion poissonWahrscheinlichkeit berechnet mit Poisson-Regr. die Ergebniswarscheinlichkeiten eines Spiels
arguments: Heim (String), Gast (String)
returns: ErgebnisWahrscheinlichkeiten
(dreielementige Liste, die die Gewinnwhkt von Heim, Unentschieden,
Gewinnwhkt von Gast enthält)
'''

def poissonWahrscheinlichkeit(Heim, Gast):
    goal_probabilities = np.zeros((10, 10))
    a = crawlTore(Heim, Gast).T

    #compute theta for the home-team
    result_home = minimize_scalar(neg_llh, method='Bounded', bounds=(0., 1000.), args=(a[:, 0]))
    #convert theta to lambda:
    lambda1 = np.exp(-result_home.x)

    #compute theta for the away-team
    result_away = minimize_scalar(neg_llh, method='Bounded', bounds=(0., 1000.), args=(a[:, 1]))
    #convert theta to lambda:
    lambda2 = np.exp(-result_away.x)

    for j in range(10):
        #Probability for home to score j goals against away as a home-team
        prob_home = lambda1**j * np.exp(-lambda1) / factorial(j)
        for k in range(10):
            #Probability for away to score k goals against home as a away-team
            prob_away = np.exp(-lambda2) * lambda2**k / factorial(k)
            #fill table with probabilities of all results
            goal_probabilities[j, k] = prob_home * prob_away


    obereDreicksmatrix = np.triu(goal_probabilities, k=1)
    Siegwahrscheinlichkeit_Team1 = round(100 * np.sum(obereDreicksmatrix), 1)

    untereDreicksmatrix = np.tril(goal_probabilities, k=-1)
    Siegwahrscheinlichkeit_Team2 = round(100 * np.sum(untereDreicksmatrix), 1)

    Unentschiedenwahrscheinlichkeit = round(100 - Siegwahrscheinlichkeit_Team1 - Siegwahrscheinlichkeit_Team2, 1)

    ErgebnisWahrscheinlichkeiten = list(
        (Siegwahrscheinlichkeit_Team1, Unentschiedenwahrscheinlichkeit, Siegwahrscheinlichkeit_Team2))
    return ErgebnisWahrscheinlichkeiten



#GUI-Klasse
class GUI:
    def __init__(self):
        self.Window = tk.Tk()
        self.Window.title('Teamprojekt 19: Vorhersagesystem')

        # Buttons:
        # Crawler
        self.crawlerbutton = tk.Button(self.Window, text='\nStarte Crawler\n',
                                       fg='black', bg="grey", width=10,
                                       height=1,
                                       command=CrawlHelper)

        # Training
        self.trainingbutton = tk.Button(self.Window,
                                        text='\nStarte \n Poisson-Training\n',
                                        fg='black', bg="grey",
                                        width=15, height=2,
                                        command=self.starteMachineLearningTraining)

        # Berechnung starten
        self.calculateButton = tk.Button(self.Window, text='Berechne Gewinnwahrscheinlichkeit',
                                         fg='black',
                                         command=self.predict)

        # Fenster schließen
        self.closebutton = tk.Button(self.Window, text='Abbrechen',
                                     bg="grey", fg="white", width=25,
                                     command=self.Window.destroy)

        # Auswählleiste
        self.MV = tk.IntVar()
        self.MV.set(1)
        self.checkbutton1 = tk.Checkbutton(self.Window, text='Minimaler Vorhersagealgorithmus', variable=self.MV,
                                           command=self.changeCheckbutton2)
        self.MLA = tk.IntVar()
        self.MLA.set(0)
        self.checkbutton2 = tk.Checkbutton(self.Window, text='Poisson Algorithmus', variable=self.MLA,
                                           command=self.changeCheckbutton1)

        # Dropdown-Listen
        mannschaften = crawlTeams(aktuellesJahr, aktuellerSpieltag)
        self.var1 = tk.StringVar()
        self.var1.set(mannschaften[0])
        self.dropdown1 = tk.OptionMenu(self.Window, self.var1, *mannschaften)

        self.var2 = tk.StringVar()
        self.var2.set(mannschaften[1])
        self.dropdown2 = tk.OptionMenu(self.Window, self.var2, *mannschaften)

        # Entries
        # Entries um Teildatensatz zum Trainieren des Machine-Learning-Algos auswählen zu können
        self.VonSaisonEntry = tk.Entry(self.Window)
        self.VonSaisonEntry.insert(10, "2009")
        self.BisSaisonEntry = tk.Entry(self.Window)
        self.BisSaisonEntry.insert(10, "2015")
        self.VonTagEntry = tk.Entry(self.Window)
        self.VonTagEntry.insert(10, "1")
        self.BisTagEntry = tk.Entry(self.Window)
        self.BisTagEntry.insert(10, "4")

        # Label
        self.ueberschrift = tk.Label(self.Window, text="Bundesliga-Vorhersage \n", font='Helvetica 20 bold')

        self.labelWähleDatensatz = tk.Label(self.Window, text="Wähle Zeitraum:", font='Helvetica 10 bold')
        self.labelVon = tk.Label(self.Window, text="Von Saison, Spieltag:")
        self.labelBis = tk.Label(self.Window, text="Bis Saison, Spieltag:")
        self.ErrorLabel = tk.Label(self.Window, text="", fg="red")

        self.labelUnentschieden = tk.Label(self.Window, text="Unentschieden:")
        self.labelGewinnHeim = tk.Label(self.Window, text="Gewinn Heim:")
        self.labelVerlustGast = tk.Label(self.Window, text="Gewinn Gast:")

        self.labelUnentschiedenNum = tk.Label(self.Window, text="?")
        self.labelGewinnHeimNum = tk.Label(self.Window, text="?")
        self.labelGewinnGastNum = tk.Label(self.Window, text="?")

        self.labelHeim = tk.Label(self.Window, text="\nHeim:", width=25, font='Helvetica 10 bold')
        self.labelGast = tk.Label(self.Window, text="\nGast:", width=25, font='Helvetica 10 bold')

        self.LabelkommenderSpieltag = tk.Label(self.Window, text="Der kommende Spieltag:", width=25, font='Helvetica 10 bold')

        self.heim1 = None
        self.gast1 = None
        self.erg1 = None
        self.erg1P = None
        self.heim2 = None
        self.gast2 = None
        self.erg2 = None
        self.erg2P = None
        self.heim3 = None
        self.gast3 = None
        self.erg3 = None
        self.erg3P = None
        self.heim4 = None
        self.gast4 = None
        self.erg4 = None
        self.erg4P = None
        self.heim5 = None
        self.gast5 = None
        self.erg5 = None
        self.erg5P = None
        self.heim6 = None
        self.gast6 = None
        self.erg6 = None
        self.erg6P = None
        self.heim7 = None
        self.gast7 = None
        self.erg7 = None
        self.erg7P = None
        self.heim8 = None
        self.gast8 = None
        self.erg8 = None
        self.erg8P = None
        self.heim9 = None
        self.gast9 = None
        self.erg9 = None
        self.erg9P = None

        self.erstelleKommenderSpieltag()

        # Postition in Grid festlegen
        self.crawlerbutton.grid(column=0, row=1, sticky='W')
        self.trainingbutton.grid(column=3, row=4)
        self.checkbutton1.grid(column=0, row=4, sticky='W')
        self.checkbutton2.grid(column=0, row=3, sticky='W')
        self.LabelkommenderSpieltag.grid(column=0, row=50)
        self.labelVon.grid(column=1, row=2)
        self.labelBis.grid(column=1, row=3)
        self.labelWähleDatensatz.grid(column=1, row=1)
        self.ErrorLabel.grid(column=2, row=4)
        self.VonSaisonEntry.grid(column=2, row=2)
        self.BisSaisonEntry.grid(column=2, row=3)
        self.VonTagEntry.grid(column=3, row=2)
        self.BisTagEntry.grid(column=3, row=3)

        self.labelHeim.grid(column=0, row=20)
        self.labelGast.grid(column=1, row=20)
        self.dropdown1.grid(column=0, row=21)
        self.dropdown2.grid(column=1, row=21)
        self.calculateButton.grid(column=2, row=21)
        self.labelGewinnHeim.grid(column=2, row=22)
        self.labelUnentschieden.grid(column=2, row=23)
        self.labelVerlustGast.grid(column=2, row=24)
        self.labelGewinnHeimNum.grid(column=3, row=22)
        self.labelUnentschiedenNum.grid(column=3, row=23)
        self.labelGewinnGastNum.grid(column=3, row=24)

        self.ueberschrift.grid(column=0, row=0, columnspan=3)
        self.closebutton.grid(column=3, row=100)

    '''
    Funktion erstelleKommenderSpieltag weist den Labels
    des kommenden Spieltages Werte zu
    arguments: none
    returns: none
    '''

    def erstelleKommenderSpieltag(self):
        kommendeMannschaften = crawlTeams(aktuellesJahr, kommenderSpieltag)
        labelNamesHeim = [self.heim1, self.heim2, self.heim3, self.heim4, self.heim5,
                          self.heim6, self.heim7, self.heim8, self.heim9]
        labelNamesGast = [self.gast1, self.gast2, self.gast3, self.gast4, self.gast5,
                          self.gast6, self.gast7, self.gast8, self.gast9]
        labelNamesErgebnis = [self.erg1, self.erg2, self.erg3, self.erg4, self.erg5,
                              self.erg6, self.erg7, self.erg8, self.erg9]
        labelNamesErgPoiss = [self.erg1P, self.erg2P, self.erg3P, self.erg4P, self.erg5P,
                              self.erg6P, self.erg7P, self.erg8P, self.erg9P]

        spieltag = 50
        # definiere Reihe ab der die Labels angezeigt werden sollen

        for i, (a, b, c, d) in enumerate(zip(labelNamesHeim, labelNamesGast, labelNamesErgebnis, labelNamesErgPoiss)):
            a = tk.Label(self.Window, text=kommendeMannschaften[2 * i], width=20).grid(column=0, row=spieltag + i + 1)
            b = tk.Label(self.Window, text=kommendeMannschaften[2 * i + 1], width=20).grid(column=1, row=spieltag + i + 1)
            c = tk.Label(self.Window, text=resultString(kommendeMannschaften[2 * i], kommendeMannschaften[2 * i + 1], "minimal"),
                         width=30).grid(column=2, row=spieltag + i + 1)
            d = tk.Label(self.Window, text=resultString(kommendeMannschaften[2 * i], kommendeMannschaften[2 * i + 1], "poisson"),
                         width=30).grid(column=3, row=spieltag + i + 1)

    '''
    Funktion changeCheckbutton1 deaktiviert
    Checkbutton1 wenn Checkbutton2 aktiviert wird
    arguments: none
    returns: none
    '''

    def changeCheckbutton1(self):
        if self.MLA.get() == 1:
            self.checkbutton1.config(variable=self.MV.set(0))
        else:
            self.checkbutton1.config(variable=self.MV.set(1))

    '''
    Funktion changeCheckbutton2 deaktiviert
    Checkbutton2 wenn Checkbutton1 aktiviert wird
    arguments: none
    returns: none
    '''

    def changeCheckbutton2(self):
        if self.MV.get() == 1:
            self.checkbutton2.config(variable=self.MLA.set(0))
        else:
            self.checkbutton2.config(variable=self.MLA.set(1))

    '''
    Funktion starteMachineLearningTraining startet
    Machine-Learning-Training mit Daten aus Entries und
    prüft Eingaben auf Korrektheit
    arguments: none
    returns: none
    '''

    def starteMachineLearningTraining(self):
        VonSaison = self.VonSaisonEntry.get()
        BisSaison = self.BisSaisonEntry.get()
        VonTag = self.VonTagEntry.get()
        BisTag = self.BisTagEntry.get()
        if VonSaison.isdigit() and BisSaison.isdigit() and VonTag.isdigit() and BisTag.isdigit():
            #Todo: Binde Funktion ein, die die gewünschten Daten aus der Datenbank holt
            Schranken = Schnittstelle(
                int(VonSaison), int(VonTag), int(BisSaison), int(BisTag))
            if Schranken[0] < 0:
                self.ErrorLabel.config(
                    text="Saison zwischen 2009 und 2018,\n Tag zwischen 1 und 34"
                    )
            else:
                self.ErrorLabel.config(text="")
        else:
            self.ErrorLabel.config(text="Eingaben müssen Zahlen sein")

    '''
    Funktion predict verwendet entweder Minimaler
    Vorhersage-Algo (MV) oder Machine-Learning-Algo (MLA)
    um Gewinnwahrscheinlichkeiten zu berechnen
    arguments: none
    returns: none
    '''

    def predict(self):
        if self.var1.get() == self.var2.get():
            self.labelGewinnHeimNum.config(text="Error: dasselbe Team ausgewählt")
            self.labelUnentschiedenNum.config(text="")
            self.labelGewinnGastNum.config(text="")
        else:
            if self.MV.get() == 1:
                Liste = Gewinnwahrscheinlichkeit(self.var1.get(), self.var2.get())
                self.labelGewinnHeimNum.config(text=str(Liste[0])+"%")
                self.labelUnentschiedenNum.config(text=str(Liste[1])+"%")
                self.labelGewinnGastNum.config(text=str(Liste[2])+"%")
            else:
                Liste = poissonWahrscheinlichkeit(self.var1.get(), self.var2.get())
                self.labelGewinnHeimNum.config(text=str(Liste[0])+"%")
                self.labelUnentschiedenNum.config(text=str(Liste[1])+"%")
                self.labelGewinnGastNum.config(text=str(Liste[2])+"%")
gui = GUI()
gui.Window.mainloop()
