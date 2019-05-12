import tkinter as tk

Window = tk.Tk()
Window.title('Teamprojekt 19: Vorhersagesystem')

#Platzhalter: Minimaler Vorhersage-Algorithmus
def predict():
    wahrscheinlichkeitNumber = 0
    wkt = str(wahrscheinlichkeitNumber)
    labelErgebnis.config(text=wkt)

'''
def crawlTeam...
'''


#Buttons:

#Crawler
crawlerbutton = tk.Button(Window, text = '\nStarte Crawler\n', fg ='black')

#Training
trainingbutton = tk.Button(Window, text = '\nStarte training\n', fg ='black')

#Berechnung starten
calculateButton = tk.Button(Window, text = 'Berechne Gewinnwahrscheinlichkeit', fg ='black', command=predict)

#Fenster schließen
closebutton = tk.Button(Window, text='Abbrechen', bg= "grey", fg = "white", width=25, command=Window.destroy)


# DROPDOWN-LISTEN 
var1 = tk.StringVar()
dropdown1= tk.OptionMenu(Window, var1, "Augsburg", "Berlin", "Bremen", "Dortmund", "Düsseldorf", "Frankfurt", "Freiburg", "Gladbach", "Hannover", "Hoffenheim", "Leipzig", "Leverkusen", "Mainz", "München", "Nürnberg", "Schalke", "Stuttgart", "Wolfsburg")
var1.set("Augsburg")
#var1.get()
var2 = tk.StringVar()
dropdown2= tk.OptionMenu(Window, var2, "Augsburg", "Berlin", "Bremen", "Dortmund", "Düsseldorf", "Frankfurt", "Freiburg", "Gladbach", "Hannover", "Hoffenheim", "Leipzig", "Leverkusen", "Mainz", "München", "Nürnberg", "Schalke", "Stuttgart", "Wolfsburg")
var2.set("Berlin")
#var2.get()


#Label 
label = tk.Label(Window, text="?")
labelHeim = tk.Label(Window, text = "\nHeim:", width=25)
labelGast = tk.Label(Window, text = "\nGast:", width=25)

LabelkommenderSpieltag= tk.Label(Window, text="Der kommende Spieltag:", width=25)
heim1 = tk.Label(Window, text="crawlHeim1", width=25)
gast1 = tk.Label(Window, text="crawlGast1", width=25)
erg1 = tk.Label(Window, text="W(crawlHeim1,crawlGast1)", width=25)
heim2 = tk.Label(Window, text="crawlHeim2", width=25)
gast2 = tk.Label(Window, text="crawlGast2", width=25)
erg2 = tk.Label(Window, text="W(crawlHeim2,crawlGast2)", width=25)
heim3 = tk.Label(Window, text="crawlHeim3", width=25)
gast3 = tk.Label(Window, text="crawlGast3", width=25)
erg3 = tk.Label(Window, text="W(crawlHeim3,crawlGast3)", width=25)
heim4 = tk.Label(Window, text="crawlHeim4", width=25)
gast4 = tk.Label(Window, text="crawlGast4", width=25)
erg4 = tk.Label(Window, text="W(crawlHeim4,crawlGast4)", width=25)
heim5 = tk.Label(Window, text="crawlHeim5", width=25)
gast5 = tk.Label(Window, text="crawlGast5", width=25)
erg5 = tk.Label(Window, text="W(crawlHeim5,crawlGast5)", width=25)
heim6 = tk.Label(Window, text="crawlHeim5", width=25)
gast6 = tk.Label(Window, text="crawlGast6", width=25)
erg6 = tk.Label(Window, text="W(crawlHeim6,crawlGast6)", width=25)
heim7 = tk.Label(Window, text="crawlHeim7", width=25)
gast7 = tk.Label(Window, text="crawlGast7", width=25)
erg7 = tk.Label(Window, text="W(crawlHeim7,crawlGast7)", width=25)
heim8 = tk.Label(Window, text="crawlHeim8", width=25)
gast8 = tk.Label(Window, text="crawlGast8", width=25)
erg8 = tk.Label(Window, text="W(crawlHeim8,crawlGast8)", width=25)
heim9 = tk.Label(Window, text="crawlHeim9", width=25)
gast9 = tk.Label(Window, text="crawlGast9", width=25)
erg9 = tk.Label(Window, text="W(crawlHeim9,crawlGast9)", width=25)
ueberschrift = tk.Label(Window, text="Vorhersage-System für die Bundesliga\n", font='Arial 20 bold')


#Postition in Grid festlegen
crawlerbutton.grid(column=0, row=1, sticky='W')
trainingbutton.grid(column=0, row=10, sticky='W')
labelHeim.grid(column =0, row =20)
labelGast.grid(column =1, row =20)
dropdown1.grid(column=0, row=21)
dropdown2.grid(column=1, row=21)
calculateButton.grid(column=2, row=21)
label.grid(column=2, row=22)
ueberschrift.grid(column=0, row=0, columnspan=3)

spieltag = 50
LabelkommenderSpieltag.grid(column=0,row=spieltag)
heim1.grid(column=0,row=spieltag+1)
gast1.grid(column=1,row=spieltag+1)
erg1.grid(column=2,row=spieltag+1)
heim2.grid(column=0,row=spieltag+2)
gast2.grid(column=1,row=spieltag+2)
erg2.grid(column=2,row=spieltag+2)
heim3.grid(column=0,row=spieltag+3)
gast3.grid(column=1,row=spieltag+3)
erg3.grid(column=2,row=spieltag+3)
heim4.grid(column=0,row=spieltag+4)
gast4.grid(column=1,row=spieltag+4)
erg4.grid(column=2,row=spieltag+4)
heim5.grid(column=0,row=spieltag+5)
gast5.grid(column=1,row=spieltag+5)
erg5.grid(column=2,row=spieltag+5)
heim6.grid(column=0,row=spieltag+6)
gast6.grid(column=1,row=spieltag+6)
erg6.grid(column=2,row=spieltag+6)
heim7.grid(column=0,row=spieltag+7)
gast7.grid(column=1,row=spieltag+7)
erg7.grid(column=2,row=spieltag+7)
heim8.grid(column=0,row=spieltag+8)
gast8.grid(column=1,row=spieltag+8)
erg8.grid(column=2,row=spieltag+8)
heim9.grid(column=0,row=spieltag+9)
gast9.grid(column=1,row=spieltag+9)
erg9.grid(column=2,row=spieltag+9)

closebutton.grid(column=2, row=100)



Window.mainloop()
