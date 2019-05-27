
from sqlalchemy import exists
import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#erstellen der Basis
Base = declarative_base()

# erstellen unserer Spiele Klasse mit allen Argumenten und Operatoren
class Spiele(Base):
    __tablename__ = "spiele"

    id  = Column( Integer, primary_key=True, unique=True)
    Datum = Column( String)
    Heim = Column( String)
    Gast = Column(String)
    ToreHeim = Column( Integer)
    ToreGast = Column( Integer)

    def __init__(self, MatchID, Datum, Heim, Gast, ToreHeim, ToreGast):
        self.id = MatchID
        self.Datum = Datum
        self.Heim = Heim
        self.Gast = Gast
        self.ToreHeim = ToreHeim
        self.ToreGast = ToreGast


engine = create_engine('sqlite:///Bundesliga_Ergebnisse_DB.db')

#erstellen der Datebbank
Base.metadata.create_all(engine)

#binden der Engine
Base.metadata.bind =engine
#erstellen der Sitzung
Session = sessionmaker(bind=engine)
session =Session()
# zugriff um einzelene Daten abzufragen
Spiel_zugriff = session.query(Spiele).all()


import requests
import json



# while schleife von allen spieltagen; zählt alle SPieltage einer Saison hoch
def SpieltageCounter():
    i = 1
    while i < 35:
        Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/2017/") + str(i)
        r = requests.get(Spieltaglink)
        y = json.loads(r.text)
        AusgabeEinesSpieltages(y)
        i = i + 1


# wertet einen Spieltag aus: whileschleife von 1 -9 für alle Spiele eines Spieltages; i= counter
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

    # aufrufen der Gastmannschaft
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

    # ''ausgabe check ' alles SPiele in die Ausgabe zu Überprüfung; optional auschaltbar
    # diverse Tests für die Ausgabe
    #print(dict.get(p, 'MatchID'))
    #print(Datum_L)
    #print(Heim_L)
    #print(Gast_L)
    #print(ToreHeim_L)
    #print(ToreGast_L)

    #erstellen der Spieldatei welche später in die Datenbank eingefügt wird
    Spiel_allgemein = Spiele(MatchID= MatchID_L, Datum= Datum_L, Heim= Heim_L, Gast= Gast_L, ToreHeim= ToreHeim_L, ToreGast= ToreGast_L )

    # Check ob das aktuell erstellte Spiel bereits in der Datenbank enthalten ist
    ret = session.query(exists().where(Spiele.id == MatchID_L)).scalar()
    if (ret == True):
        pass
    else: session.add(Spiel_allgemein)      # falls nicht hinzufügen des Spiels


    #aktualisieren der Datei
    session.commit()

#aufruf des Spieltagcounters
SpieltageCounter()

#abschließende Aktualisierun
session.commit()

#Testaufruf einzelner Key eins Spieles

# test alle matchid`s überprüfung auf doppelte ID`s

#test eines Beispiels
def testeinesSpiels():
    d = 305
    print(Spiel_zugriff[d].id)
    print(Spiel_zugriff[d].Heim)
    print(Spiel_zugriff[d].ToreHeim)
    print(Spiel_zugriff[d].Gast)
    print(Spiel_zugriff[d].ToreGast)

# Möglichkeit sich alle IDS einer saison auszugeben

def ausgabealleIDS() :
    i = 0
    while i < 306:
        print (Spiel_zugriff[i].id)
        i= i+1