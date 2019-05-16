import tkinter as tk

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
        var1 = tk.StringVar()
        self.dropdown1= tk.OptionMenu(self.Window, var1, "Augsburg", "Berlin", "Bremen", "Dortmund", "Düsseldorf", "Frankfurt", "Freiburg", "Gladbach", "Hannover", "Hoffenheim", "Leipzig", "Leverkusen", "Mainz", "München", "Nürnberg", "Schalke", "Stuttgart", "Wolfsburg")
        var1.set("Augsburg")
        #var1.get()
        var2 = tk.StringVar()
        self.dropdown2= tk.OptionMenu(self.Window, var2, "Augsburg", "Berlin", "Bremen", "Dortmund", "Düsseldorf", "Frankfurt", "Freiburg", "Gladbach", "Hannover", "Hoffenheim", "Leipzig", "Leverkusen", "Mainz", "München", "Nürnberg", "Schalke", "Stuttgart", "Wolfsburg")
        var2.set("Berlin")
        #var2.get()


        #Label 
        self.label = tk.Label(self.Window, text="?")
        self.labelHeim = tk.Label(self.Window, text = "\nHeim:", width=25)
        self.labelGast = tk.Label(self.Window, text = "\nGast:", width=25)

        self.LabelkommenderSpieltag= tk.Label(self.Window, text="Der kommende Spieltag:", width=25)
        self.heim1 = tk.Label(self.Window, text="crawlHeim1", width=25)
        self.gast1 = tk.Label(self.Window, text="crawlGast1", width=25)
        self.erg1 = tk.Label(self.Window, text="W(crawlHeim1,crawlGast1)", width=25)
        self.heim2 = tk.Label(self.Window, text="crawlHeim2", width=25)
        self.gast2 = tk.Label(self.Window, text="crawlGast2", width=25)
        self.erg2 = tk.Label(self.Window, text="W(crawlHeim2,crawlGast2)", width=25)
        self.heim3 = tk.Label(self.Window, text="crawlHeim3", width=25)
        self.gast3 = tk.Label(self.Window, text="crawlGast3", width=25)
        self.erg3 = tk.Label(self.Window, text="W(crawlHeim3,crawlGast3)", width=25)
        self.heim4 = tk.Label(self.Window, text="crawlHeim4", width=25)
        self.gast4 = tk.Label(self.Window, text="crawlGast4", width=25)
        self.erg4 = tk.Label(self.Window, text="W(crawlHeim4,crawlGast4)", width=25)
        self.heim5 = tk.Label(self.Window, text="crawlHeim5", width=25)
        self.gast5 = tk.Label(self.Window, text="crawlGast5", width=25)
        self.erg5 = tk.Label(self.Window, text="W(crawlHeim5,crawlGast5)", width=25)
        self.heim6 = tk.Label(self.Window, text="crawlHeim5", width=25)
        self.gast6 = tk.Label(self.Window, text="crawlGast6", width=25)
        self.erg6 = tk.Label(self.Window, text="W(crawlHeim6,crawlGast6)", width=25)
        self.heim7 = tk.Label(self.Window, text="crawlHeim7", width=25)
        self.gast7 = tk.Label(self.Window, text="crawlGast7", width=25)
        self.erg7 = tk.Label(self.Window, text="W(crawlHeim7,crawlGast7)", width=25)
        self.heim8 = tk.Label(self.Window, text="crawlHeim8", width=25)
        self.gast8 = tk.Label(self.Window, text="crawlGast8", width=25)
        self.erg8 = tk.Label(self.Window, text="W(crawlHeim8,crawlGast8)", width=25)
        self.heim9 = tk.Label(self.Window, text="crawlHeim9", width=25)
        self.gast9 = tk.Label(self.Window, text="crawlGast9", width=25)
        self.erg9 = tk.Label(self.Window, text="W(crawlHeim9,crawlGast9)", width=25)
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


        #def crawlTeam...

gui = GUI()
gui.Window.mainloop()
