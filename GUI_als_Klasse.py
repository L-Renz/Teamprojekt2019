import tkinter as tk
import requests
import json


aktuellesJahr = 2017
aktuellerSpieltag = 2
kommenderSpieltag = (aktuellerSpieltag+1)
#abfangen: aktuellerSpieltag=34 +1

def crawlTeam(Jahr, Spieltag):

    # enthält Teams einer Saison
    TeamListe = []

    # externe Daten
    Spieltaglink = ("https://www.openligadb.de/api/getmatchdata/bl1/")+ str(Jahr)+ ("/")+ str(Spieltag)

    #holt externe Daten eines Spieltages
    r = requests.get(Spieltaglink)
    y = json.loads(r.text)

    #geht alle Begegnungen des Spieltages durch
    i = 0
    while i < 9:
        p = y[i]

        # Speichere jeweils die Heimmanschaft
        a = dict.get(p, "Team1")
        b = dict.get(a, "TeamName")
        Heim = str(b)
        # Test
        #print(Heim)
        TeamListe.append(Heim)

        # Speichere jeweils die Gastmannschaft
        c = dict.get(p, "Team2")
        d = dict.get(c, "TeamName")
        Gast = str(d)
        # Test
        #print(Gast)
        TeamListe.append(Gast)

        i =i+1
    return TeamListe


class GUI:
    def __init__(self):
        self.Window = tk.Tk()
        self.Window.title('Teamprojekt 19: Vorhersagesystem')

        #Buttons:

        #Crawler
        self.crawlerbutton = tk.Button(self.Window, text = '\nStarte Crawler\n', fg ='black')

        #Training
        self.trainingbutton = tk.Button(self.Window, text = '\nStarte training\n', fg ='black')

        #Berechnung starten
        self.calculateButton = tk.Button(self.Window, text = 'Berechne Gewinnwahrscheinlichkeit', fg ='black', command= self.predict)

        #Fenster schließen
        self.closebutton = tk.Button(self.Window, text='Abbrechen', bg= "grey", fg = "white", width=25, command=self.Window.destroy)


        # DROPDOWN-LISTEN
        mannschaften = crawlTeam(2017, 1)
        var1 = tk.StringVar()
        self.dropdown1= tk.OptionMenu(self.Window, var1, mannschaften[0], mannschaften[1], mannschaften[2], mannschaften[3], mannschaften[4], mannschaften[5], mannschaften[6], mannschaften[7], mannschaften[8], mannschaften[9], mannschaften[10], mannschaften[11], mannschaften[12], mannschaften[13], mannschaften[14], mannschaften[15], mannschaften[16], mannschaften[17])
        var1.set(mannschaften[0])
        #var1.get()
        var2 = tk.StringVar()
        self.dropdown2= tk.OptionMenu(self.Window, var2, mannschaften[0], mannschaften[1], mannschaften[2], mannschaften[3], mannschaften[4], mannschaften[5], mannschaften[6], mannschaften[7], mannschaften[8], mannschaften[9], mannschaften[10], mannschaften[11], mannschaften[12], mannschaften[13], mannschaften[14], mannschaften[15], mannschaften[16], mannschaften[17])
        var2.set(mannschaften[1])
        #var2.get()


        #Label 
        self.label = tk.Label(self.Window, text="?")
        self.labelHeim = tk.Label(self.Window, text = "\nHeim:", width=25)
        self.labelGast = tk.Label(self.Window, text = "\nGast:", width=25)

        kommendeMannschaften = crawlTeam(aktuellesJahr, kommenderSpieltag)
        self.LabelkommenderSpieltag= tk.Label(self.Window, text="Der kommende Spieltag:", width=25)
        self.heim1 = tk.Label(self.Window, text=kommendeMannschaften[0], width=25)
        self.gast1 = tk.Label(self.Window, text=kommendeMannschaften[1], width=25)
        self.erg1 = tk.Label(self.Window, text="W "+kommendeMannschaften[0]+ " - "+kommendeMannschaften[1], width=25)
        self.heim2 = tk.Label(self.Window, text=kommendeMannschaften[2], width=25)
        self.gast2 = tk.Label(self.Window, text=kommendeMannschaften[3], width=25)
        self.erg2 = tk.Label(self.Window, text="W "+kommendeMannschaften[2]+ " - "+kommendeMannschaften[3], width=25)
        self.heim3 = tk.Label(self.Window, text=kommendeMannschaften[4], width=25)
        self.gast3 = tk.Label(self.Window, text=kommendeMannschaften[5], width=25)
        self.erg3 = tk.Label(self.Window, text="W "+kommendeMannschaften[4]+ " - "+kommendeMannschaften[5], width=25)
        self.heim4 = tk.Label(self.Window, text=kommendeMannschaften[6], width=25)
        self.gast4 = tk.Label(self.Window, text=kommendeMannschaften[7], width=25)
        self.erg4 = tk.Label(self.Window, text="W "+kommendeMannschaften[6]+ " - "+kommendeMannschaften[7], width=25)
        self.heim5 = tk.Label(self.Window, text=kommendeMannschaften[8], width=25)
        self.gast5 = tk.Label(self.Window, text=kommendeMannschaften[9], width=25)
        self.erg5 = tk.Label(self.Window, text="W "+kommendeMannschaften[8]+ " - "+kommendeMannschaften[9], width=25)
        self.heim6 = tk.Label(self.Window, text=kommendeMannschaften[10], width=25)
        self.gast6 = tk.Label(self.Window, text=kommendeMannschaften[11], width=25)
        self.erg6 = tk.Label(self.Window, text="W "+kommendeMannschaften[10]+ " - "+kommendeMannschaften[11], width=25)
        self.heim7 = tk.Label(self.Window, text=kommendeMannschaften[12], width=25)
        self.gast7 = tk.Label(self.Window, text=kommendeMannschaften[13], width=25)
        self.erg7 = tk.Label(self.Window, text="W "+kommendeMannschaften[12]+ " - "+kommendeMannschaften[13], width=25)
        self.heim8 = tk.Label(self.Window, text=kommendeMannschaften[14], width=25)
        self.gast8 = tk.Label(self.Window, text=kommendeMannschaften[15], width=25)
        self.erg8 = tk.Label(self.Window, text="W "+kommendeMannschaften[14]+ " - "+kommendeMannschaften[15], width=25)
        self.heim9 = tk.Label(self.Window, text=kommendeMannschaften[16], width=25)
        self.gast9 = tk.Label(self.Window, text=kommendeMannschaften[17], width=25)
        self.erg9 = tk.Label(self.Window, text="W "+kommendeMannschaften[16]+ " - "+kommendeMannschaften[17], width=25)
        self.ueberschrift = tk.Label(self.Window, text="Vorhersage-System für die Bundesliga\n", font='Arial 20 bold')


        #Postition in Grid festlegen
        self.crawlerbutton.grid(column=0, row=1, sticky='W')
        self.trainingbutton.grid(column=0, row=10, sticky='W')
        self.labelHeim.grid(column =0, row =20)
        self.labelGast.grid(column =1, row =20)
        self.dropdown1.grid(column=0, row=21)
        self.dropdown2.grid(column=1, row=21)
        self.calculateButton.grid(column=2, row=21)
        self.label.grid(column=2, row=22)
        self.ueberschrift.grid(column=0, row=0, columnspan=3)

        spieltag = 50
        self.LabelkommenderSpieltag.grid(column=0,row=spieltag)
        self.heim1.grid(column=0,row=spieltag+1)
        self.gast1.grid(column=1,row=spieltag+1)
        self.erg1.grid(column=2,row=spieltag+1)
        self.heim2.grid(column=0,row=spieltag+2)
        self.gast2.grid(column=1,row=spieltag+2)
        self.erg2.grid(column=2,row=spieltag+2)
        self.heim3.grid(column=0,row=spieltag+3)
        self.gast3.grid(column=1,row=spieltag+3)
        self.erg3.grid(column=2,row=spieltag+3)
        self.heim4.grid(column=0,row=spieltag+4)
        self.gast4.grid(column=1,row=spieltag+4)
        self.erg4.grid(column=2,row=spieltag+4)
        self.heim5.grid(column=0,row=spieltag+5)
        self.gast5.grid(column=1,row=spieltag+5)
        self.erg5.grid(column=2,row=spieltag+5)
        self.heim6.grid(column=0,row=spieltag+6)
        self.gast6.grid(column=1,row=spieltag+6)
        self.erg6.grid(column=2,row=spieltag+6)
        self.heim7.grid(column=0,row=spieltag+7)
        self.gast7.grid(column=1,row=spieltag+7)
        self.erg7.grid(column=2,row=spieltag+7)
        self.heim8.grid(column=0,row=spieltag+8)
        self.gast8.grid(column=1,row=spieltag+8)
        self.erg8.grid(column=2,row=spieltag+8)
        self.heim9.grid(column=0,row=spieltag+9)
        self.gast9.grid(column=1,row=spieltag+9)
        self.erg9.grid(column=2,row=spieltag+9)

        self.closebutton.grid(column=2, row=100)

        
    #Platzhalter: Minimaler Vorhersage-Algorithmus
    def predict(self):
        wahrscheinlichkeitNumber = 0
        wkt = str(wahrscheinlichkeitNumber)
        self.label.config(text=wkt)

        

gui = GUI()
gui.Window.mainloop()
