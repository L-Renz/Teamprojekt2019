from sqlalchemy import exists
import sqlalchemy

import sys

print(sqlalchemy.__version__)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Erstellen der Basis
Base = declarative_base()


# Erstellen unserer Spiele Klasse mit allen Argumenten und Operatoren
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

# Erstellen der Datebbank
Base.metadata.create_all(engine)

# Binden der Engine
Base.metadata.bind = engine
# Erstellen der Sitzung
Session = sessionmaker(bind=engine)
session = Session()
# Zugriff um einzelene Daten abzufragen
Spiel_zugriff = session.query(Spiele).all()

from sqlalchemy import func
import requests
import json

# While-Schleife für alle Saisonspieljahre

def Spieltagsjahre ():########
    i = 2009
    while i < 2019:
        Saisonlink = "https://www.openligadb.de/api/getmatchdata/bl1/" + str(i) + "/"
        SpieltageCounter(Saisonlink)
        i = i+1


# While-Schleife von allen Spieltagen; zählt alle Spieltage einer Saison hoch
def SpieltageCounter(a):#########
    i = 1
    while i < 35:
        Spieltaglink = (a) + str(i)
        r = requests.get(Spieltaglink)
        y = json.loads(r.text)
        AusgabeEinesSpieltages(y)
        i = i + 1
    session.commit()


# Wertet einen Spieltag aus: While-Schleife von 1 -9 für alle Spiele eines Spieltages; i= counter
def AusgabeEinesSpieltages(y):
    i = 0
    while i < 9:
        p = y[i]
        Spielliste(p)
        i = i + 1


# Aufruf der Einzelnen Elemente welche für die csv Datei benötigt werden; und direktes Schreiben der csv Datei.
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

    # ''ausgabe check ' alle Spiele in die Ausgabe zu Überprüfung; optional auschaltbar
    # diverse Tests für die Ausgabe
    print(dict.get(p, 'MatchID'))
    # print(Datum_L)
    # print(Heim_L)
    # print(Gast_L)
    # print(ToreHeim_L)
    # print(ToreGast_L)

    # erstellen der Spieldatei welche später in die Datenbank eingefügt wird
    Spiel_allgemein = Spiele(MatchID=MatchID_L, Datum=Datum_L, Heim=Heim_L, Gast=Gast_L, ToreHeim=ToreHeim_L,
                             ToreGast=ToreGast_L)

    # Check ob das aktuell erstellte Spiel bereits in der Datenbank enthalten ist
    ret = session.query(exists().where(Spiele.id == MatchID_L)).scalar()
    if (ret == True):
        pass
    else:
        session.add(Spiel_allgemein)  # falls nicht hinzufügen des Spiels

    # aktualisieren der Datei
    session.commit()


# Aufruf des Spieltagcounters
# SpieltageCounter()

# abschließende Aktualisierung
session.commit()


# Testaufruf einzelner Key eines Spiels

# Teste alle matchid`s Überprüfung auf doppelte ID`s

# Test eines Beispiels
def testeinesSpiels(d):
    print(Spiel_zugriff[d].id)
    print(Spiel_zugriff[d].Heim)
    print(Spiel_zugriff[d].ToreHeim)
    print(Spiel_zugriff[d].Gast)
    print(Spiel_zugriff[d].ToreGast)


# Möglichkeit sich alle IDS einer Saison auszugeben

def ausgabealleIDS():
    i = 0
    while i < 306:
        print(Spiel_zugriff[i].id)
        i = i + 1


AnzahlSpieleGesamt = session.query(Spiele).count()

#Auswahl der Daten von (Saison v, Spieltag w) bis (Saison x, Spieltag y)
def Schnittstelle (v, w, x, y):########
    if v < 2009 or v > aktuellesJahr or x < 2009 or x > aktuellesJahr or w < 1 or y < 1 or w > 34 or y > 34:
       return (-1 , -1)
    else:
       untereSchranke = (v - 2009) * 306 + (w - 1) *9
       obereSchranke = (x - 2009) * 306 + (y - 1) * 9 + 8
       #UntereID= Spiel_zugriff[untereSchranke].id
       #ObereID= Spiel_zugriff[obereSchranke].id
       print(AnzahlSpieleGesamt)
       if ((AnzahlSpieleGesamt - 1) < obereSchranke ) or (obereSchranke < untereSchranke):
           return (-1 , -1)#"out of ", "range"
       return (untereSchranke, obereSchranke)


def Gewinnwahrscheinlichkeit(Team1, Team2):
    SiegTeam1 = 0
    UnentschiedenTeam1 = 0
    NiederlageTeam1 = 0
    SiegTeam2 = 0
    UnentschiedenTeam2 = 0
    NiederlageTeam2 = 0

    i = 0
    indexSpiel = AnzahlSpieleGesamt - 1  # indexfunction

    while i < 5:

        indexSp = (indexSpiel - (i * 9))
        j = 0
        while j < 9:
            if (Spiel_zugriff[indexSp - j].Heim == Team1):
                if (Spiel_zugriff[indexSp - j].ToreHeim > Spiel_zugriff[indexSp - j].ToreGast):
                    SiegTeam1 = SiegTeam1 + 1
                if (Spiel_zugriff[indexSp - j].ToreHeim == Spiel_zugriff[indexSp - j].ToreGast):
                    UnentschiedenTeam1 = UnentschiedenTeam1 + 1
                if (Spiel_zugriff[indexSp - j].ToreHeim < Spiel_zugriff[indexSp - j].ToreGast):
                    NiederlageTeam1 = NiederlageTeam1 + 1

            if ((Spiel_zugriff)[indexSp - j].Gast == Team1):
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

            if ((Spiel_zugriff)[indexSp - j].Gast == Team2):
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
        Unentschiedenwahrscheinlichkeit = ((UnentschiedenTeam1 + UnentschiedenTeam2) / 10 * 100)
        Siegwahrscheinlichkeit_Team2 = ((SiegTeam2 + NiederlageTeam1) / 10 * 100)
        ErgebnisWahrscheinlichkeiten = list(
            (Siegwahrscheinlichkeit_Team1, Unentschiedenwahrscheinlichkeit, Siegwahrscheinlichkeit_Team2))
        return ErgebnisWahrscheinlichkeiten

    else:
        return "keine 10 ergebnisse, Falscher Name ?"


import tkinter as tk
import requests
import json

aktuellesJahr = 2017
aktuellerSpieltag = 2
kommenderSpieltag = (aktuellerSpieltag + 1)


# abfangen: aktuellerSpieltag=34 +1

def crawlTeam(Jahr, Spieltag):
    # enthält Teams einer Saison
    TeamListe = []

    # externe Daten
    Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/") + str(Jahr) + ("/") + str(Spieltag)

    # holt externe Daten eines Spieltages
    r = requests.get(Spieltaglink)
    y = json.loads(r.text)

    # geht alle Begegnungen des Spieltages durch
    i = 0
    while i < 9:
        p = y[i]

        # Speichere jeweils die Heimmanschaft
        a = dict.get(p, "Team1")
        b = dict.get(a, "TeamName")
        Heim = str(b)
        # Test
        # print(Heim)
        TeamListe.append(Heim)

        # Speichere jeweils die Gastmannschaft
        c = dict.get(p, "Team2")
        d = dict.get(c, "TeamName")
        Gast = str(d)
        # Test
        # print(Gast)
        TeamListe.append(Gast)

        i = i + 1
    return TeamListe


class GUI:
    def __init__(self):
        self.Window = tk.Tk()
        self.Window.title('Teamprojekt 19: Vorhersagesystem')
        #self.Window.configure(background='white')

        # Buttons:
        # Crawler
        self.crawlerbutton = tk.Button(self.Window, text='\nStarte Crawler\n', fg='black',bg="grey", width=10, height=1 , command=Spieltagsjahre)########

        # Training
        self.trainingbutton = tk.Button(self.Window, text='\nStarte Machine-Learning-Training\n', fg='black', bg="grey", width=30, height=1, command=self.starteMachineLearningTraining)

        # Berechnung starten
        self.calculateButton = tk.Button(self.Window, text='Berechne Gewinnwahrscheinlichkeit', fg='black',
                                         command=self.predict)

        # Fenster schließen
        self.closebutton = tk.Button(self.Window, text='Abbrechen', bg="grey", fg="white", width=25,
                                     command=self.Window.destroy)

        #Auswählleiste
        self.MV = tk.IntVar()
        self.MV.set(1)
        self.checkbutton1= tk.Checkbutton(self.Window, text='Minimaler Vorhersagealgorithmus', variable=self.MV, command=self.changeCheckbutton2) 
        self.MLA = tk.IntVar()
        self.MLA.set(0)
        self.checkbutton2 = tk.Checkbutton(self.Window, text='Machine Learning Algorithmus', variable=self.MLA, command=self.changeCheckbutton1) 

        # Dropdown-Listen
        mannschaften = crawlTeam(aktuellesJahr, aktuellerSpieltag)
        self.var1 = tk.StringVar()
        self.var1.set(mannschaften[0])
        self.dropdown1 = tk.OptionMenu(self.Window, self.var1, *mannschaften)

        self.var2 = tk.StringVar()
        self.var2.set(mannschaften[1])
        self.dropdown2 = tk.OptionMenu(self.Window, self.var2, *mannschaften)

        
        # Entries
        # Entries um Teildatensatz zum Trainieren des Machine-Learning-Algos auswählen zu können
        self.VonSaisonEntry = tk.Entry(self.Window)
        self.VonSaisonEntry.insert(10,"2009")
        self.BisSaisonEntry = tk.Entry(self.Window)
        self.BisSaisonEntry.insert(10,"2015")
        self.VonTagEntry = tk.Entry(self.Window)
        self.VonTagEntry.insert(10,"1")
        self.BisTagEntry = tk.Entry(self.Window)
        self.BisTagEntry.insert(10,"4")
        

        # Label
        self.labelWähleDatensatz = tk.Label(self.Window, text="Wähle Datensatz:")
        self.labelVon = tk.Label(self.Window, text="Von Saison, Spieltag:")
        self.labelBis = tk.Label(self.Window, text="Bis Saison, Spieltag:")
        self.ErrorLabel = tk.Label(self.Window, text="", fg = "red")
        
        self.labelUnentschieden = tk.Label(self.Window, text="Unentschieden:")
        self.labelGewinnHeim = tk.Label(self.Window, text="Gewinn Heim:")
        self.labelVerlustGast = tk.Label(self.Window, text="Gewinn Gast:")

        self.labelUnentschiedenNum = tk.Label(self.Window, text="?")
        self.labelGewinnHeimNum = tk.Label(self.Window, text="?")
        self.labelVerlustGastNum = tk.Label(self.Window, text="?")

        self.labelHeim = tk.Label(self.Window, text="\nHeim:", width=25)
        self.labelGast = tk.Label(self.Window, text="\nGast:", width=25)

        kommendeMannschaften = crawlTeam(aktuellesJahr, kommenderSpieltag)
        self.LabelkommenderSpieltag = tk.Label(self.Window, text="Der kommende Spieltag:", width=25)
        self.heim1 = tk.Label(self.Window, text=kommendeMannschaften[0], width=25)
        self.gast1 = tk.Label(self.Window, text=kommendeMannschaften[1], width=25)
        self.erg1 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[0], kommendeMannschaften[1]),width=55)

        self.heim2 = tk.Label(self.Window, text=kommendeMannschaften[2], width=25)
        self.gast2 = tk.Label(self.Window, text=kommendeMannschaften[3], width=25)
        self.erg2 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[2], kommendeMannschaften[3]),width=55)

        self.heim3 = tk.Label(self.Window, text=kommendeMannschaften[4], width=25)
        self.gast3 = tk.Label(self.Window, text=kommendeMannschaften[5], width=25)
        self.erg3 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[4], kommendeMannschaften[5]),width=55)

        self.heim4 = tk.Label(self.Window, text=kommendeMannschaften[6], width=25)
        self.gast4 = tk.Label(self.Window, text=kommendeMannschaften[7], width=25)
        self.erg4 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[6], kommendeMannschaften[7]),width=55)

        self.heim5 = tk.Label(self.Window, text=kommendeMannschaften[8], width=25)
        self.gast5 = tk.Label(self.Window, text=kommendeMannschaften[9], width=25)
        self.erg5 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[8], kommendeMannschaften[9]),width=55)

        self.heim6 = tk.Label(self.Window, text=kommendeMannschaften[10], width=25)
        self.gast6 = tk.Label(self.Window, text=kommendeMannschaften[11], width=25)
        self.erg6 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[10], kommendeMannschaften[11]),width=55)

        self.heim7 = tk.Label(self.Window, text=kommendeMannschaften[12], width=25)
        self.gast7 = tk.Label(self.Window, text=kommendeMannschaften[13], width=25)
        self.erg7 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[12], kommendeMannschaften[13]),width=55)

        self.heim8 = tk.Label(self.Window, text=kommendeMannschaften[14], width=25)
        self.gast8 = tk.Label(self.Window, text=kommendeMannschaften[15], width=25)
        self.erg8 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[14], kommendeMannschaften[15]),width=55)

        self.heim9 = tk.Label(self.Window, text=kommendeMannschaften[16], width=25)
        self.gast9 = tk.Label(self.Window, text=kommendeMannschaften[17], width=25)
        self.erg9 = tk.Label(self.Window, text=predictNext(kommendeMannschaften[16], kommendeMannschaften[17]),width=55)

        self.ueberschrift = tk.Label(self.Window, text="Bundesliga-Vorhersage \n", font='Arial 20 bold')

        # Postition in Grid festlegen
        self.crawlerbutton.grid(column=0, row=1, sticky='W')
        self.trainingbutton.grid(column=4, row=3, sticky='W')
        self.checkbutton1.grid(column=1,row=1, sticky='W')
        self.checkbutton2.grid(column=1,row=2, sticky='W')

        self.labelVon.grid(column=3,row=1)
        self.labelBis.grid(column=3,row=2)
        self.labelWähleDatensatz.grid(column=4,row=0)
        self.ErrorLabel.grid(column=4,row=4)
        self.VonSaisonEntry.grid(column=4,row=1)
        self.BisSaisonEntry.grid(column=4,row=2)
        self.VonTagEntry.grid(column=5,row=1)
        self.BisTagEntry.grid(column=5,row=2)
        
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
        self.labelVerlustGastNum.grid(column=3, row=24)

        self.ueberschrift.grid(column=0, row=0, columnspan=3)

        spieltag = 50
        self.LabelkommenderSpieltag.grid(column=0, row=spieltag)
        self.heim1.grid(column=0, row=spieltag + 1)
        self.gast1.grid(column=1, row=spieltag + 1)
        self.erg1.grid(column=2, row=spieltag + 1)
        self.heim2.grid(column=0, row=spieltag + 2)
        self.gast2.grid(column=1, row=spieltag + 2)
        self.erg2.grid(column=2, row=spieltag + 2)
        self.heim3.grid(column=0, row=spieltag + 3)
        self.gast3.grid(column=1, row=spieltag + 3)
        self.erg3.grid(column=2, row=spieltag + 3)
        self.heim4.grid(column=0, row=spieltag + 4)
        self.gast4.grid(column=1, row=spieltag + 4)
        self.erg4.grid(column=2, row=spieltag + 4)
        self.heim5.grid(column=0, row=spieltag + 5)
        self.gast5.grid(column=1, row=spieltag + 5)
        self.erg5.grid(column=2, row=spieltag + 5)
        self.heim6.grid(column=0, row=spieltag + 6)
        self.gast6.grid(column=1, row=spieltag + 6)
        self.erg6.grid(column=2, row=spieltag + 6)
        self.heim7.grid(column=0, row=spieltag + 7)
        self.gast7.grid(column=1, row=spieltag + 7)
        self.erg7.grid(column=2, row=spieltag + 7)
        self.heim8.grid(column=0, row=spieltag + 8)
        self.gast8.grid(column=1, row=spieltag + 8)
        self.erg8.grid(column=2, row=spieltag + 8)
        self.heim9.grid(column=0, row=spieltag + 9)
        self.gast9.grid(column=1, row=spieltag + 9)
        self.erg9.grid(column=2, row=spieltag + 9)

        self.closebutton.grid(column=5, row=100)

    # Wenn ein Checkbutton aktiviert ist, soll der andere automatisch deaktiviert sein
    def changeCheckbutton1(self):
        if self.MLA.get()==1:
           self.checkbutton1.config(variable=self.MV.set(0))
        else :
            self.checkbutton1.config(variable=self.MV.set(1))


    def changeCheckbutton2(self):
        if self.MV.get()==1:
           self.checkbutton2.config(variable=self.MLA.set(0))
        else :
            self.checkbutton2.config(variable=self.MLA.set(1))

    #Machine-Learning-Training mit ausgewählten Daten aus Entry starten
    def starteMachineLearningTraining(self):
        VonSaison = self.VonSaisonEntry.get()
        BisSaison = self.BisSaisonEntry.get()
        VonTag = self.VonTagEntry.get()
        BisTag = self.BisTagEntry.get()
        if VonSaison.isdigit() and BisSaison.isdigit() and VonTag.isdigit() and BisTag.isdigit(): 
           #Todo: Binde Funktion ein, die gewünschten Daten aus Datenbank holt...
           Schranken = Schnittstelle(int(VonSaison), int(VonTag), int(BisSaison), int(BisTag))
           if Schranken[0] < 0:
               self.ErrorLabel.config(text="Saison zwischen 2009 und 2018, Tag zwischen 1 und 34")
           else:
               self.ErrorLabel.config(text="")
        else:
            self.ErrorLabel.config(text="Eingaben müssen Zahlen sein")
          

    # Verwendet entweder Minimaler Vorhersage-Algo (MV) oder Machine-Learning-Algo (MLA)
    def predict(self):
        if self.MV.get()==1:
           if self.var1.get() == self.var2.get():#Dasselbe Team soll nicht gegen sich selbst spielen können
              self.labelGewinnHeimNum.config(text="Error: dasselbe Team ausgewählt")
              self.labelUnentschiedenNum.config(text="")
              self.labelVerlustGastNum.config(text="")
           else:
              Liste = Gewinnwahrscheinlichkeit (self.var1.get(),self.var2.get())

              self.labelGewinnHeimNum.config(text=str(Liste[0]))
              self.labelUnentschiedenNum.config(text=str(Liste[1]))
              self.labelVerlustGastNum.config(text=str(Liste[2]))
        else: #Todo: hier MLA einbinden...
            self.labelGewinnHeimNum.config(text="?")
            self.labelUnentschiedenNum.config(text="?")
            self.labelVerlustGastNum.config(text="?")


# gibt String aus, mit dem wahrscheinlichsten Ergebnis und allen 3 Wahrscheinlichkeiten
def predictNext(Team1, Team2):
        Liste = Gewinnwahrscheinlichkeit(Team1, Team2)

        if Liste[0] >= Liste[1] and Liste[0] >= Liste[2]:
            return str(Liste[0]) + "% " + "Heimsieg: " + str(Liste[0]) + " - " + str(Liste[1]) + " - " + str(Liste[2])

        elif Liste[2] >= Liste[0] and Liste[2] >= Liste[1]:
            return str(Liste[2]) + "% " + "Auswärtssieg: " + str(Liste[0]) + " - " + str(Liste[1]) + " - " + str(Liste[2])

        else:
            return str(Liste[1]) + "% " + "Unentschieden: " + str(Liste[0]) + " - " + str(Liste[1]) + " - " + str(Liste[2])


gui = GUI()
gui.Window.mainloop()
