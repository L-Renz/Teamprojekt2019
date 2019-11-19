from sqlalchemy import exists
import sqlalchemy

print(sqlalchemy.__version__)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# erstellen der Basis
Base = declarative_base()


# erstellen unserer Spiele Klasse mit allen Argumenten und Operatoren
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

# erstellen der Datebbank
Base.metadata.create_all(engine)

# binden der Engine
Base.metadata.bind = engine
# erstellen der Sitzung
Session = sessionmaker(bind=engine)
session = Session()
# zugriff um einzelene Daten abzufragen
Spiel_zugriff = session.query(Spiele).all()

#index funktion
AnzahlSpieleGesamt = session.query(Spiele).count()

def Schnittstelle ( v, w, x, y):
    untereSchranke = (v-2009) * 306 + (w-1) *9
    obereSchranke = (x - 2009) * 306 + (y - 1) * 9 +8
    #UntereID= Spiel_zugriff[untereSchranke].id
    #ObereID= Spiel_zugriff[obereSchranke].id
    if ((AnzahlSpieleGesamt-1) < obereSchranke ): return "out of ", "range"
    return ( untereSchranke , obereSchranke)




