from tkinter import*

# Test-/Hilfsfuktion
def algo(x,y):
    return "..."

# Test-/Hilfsfuktion
def berechneWahrscheinlichkeit():
    wahrscheinlichkeitNumber = 0
    wkt = str(wahrscheinlichkeitNumber)
    ergebnis.config(text=wkt)



window = Tk()
window.title("Bundesliga-Vorhersage-Teamprojekt")

#Überschrift
#Label (window, text="Teamprojekt:", font="none 16 bold") .grid(row=0, column=0, sticky=W)
#Label (window, text="Vorhersagesystem für die Bundesliga", font="none 16 bold") .grid(row=1, column=0, sticky=W)

# CRAWLER
Button(window, text="Crawler aktivieren") .grid(row=3, column=0, sticky=W)
#crawler liefert .csv-datei mit name, heim, gast, tore-heim, tore-gast
# Leerzeile
Label (window, text="", width=25) .grid(row=4, column=0)

# TRAINING
Button (window, text="Trainiere ML-A") .grid(row=5, column=0, sticky=W)
# Leerzeile
Label (window, text="", width=25) .grid(row=6, column=0)

# DROPDOWN-LISTEN
var1 = StringVar()
dropdown1=OptionMenu(window, var1, "Augsburg", "Berlin", "Bremen", "Dortmund", "Düsseldorf", "Frankfurt", "Freiburg", "Gladbach", "Hannover", "Hoffenheim", "Leipzig", "Leverkusen", "Mainz", "München", "Nürnberg", "Schalke", "Stuttgart", "Wolfsburg")
var2 = StringVar()
dropdown2=OptionMenu(window, var2, "Augsburg", "Berlin", "Bremen", "Dortmund", "Düsseldorf", "Frankfurt", "Freiburg", "Gladbach", "Hannover", "Hoffenheim", "Leipzig", "Leverkusen", "Mainz", "München", "Nürnberg", "Schalke", "Stuttgart", "Wolfsburg")

Label (window, text="HEIM:", width=25) .grid(row=7, column=0)
dropdown1.grid(row=8, column=0)

Label (window, text="GAST:", width=25) .grid(row=7, column=1)
dropdown2.grid(row=8, column=1)

gewinnW = Button (window, text="berechne GewinnW'(Heim)", command=berechneWahrscheinlichkeit, width=25)
gewinnW.grid(row=7, column=2)
ergebnis = Label(window, text="-", width=25)
# statt algo(1,2) <-> algo(crawlHeim,crawlGast)
ergebnis.grid(row=8, column=2)
# Leerzeile
Label (window, text="", width=25) .grid(row=9, column=0)


Label (window, text="Der kommender Spieltag:", width=25) .grid(row=10, column=0)
heim1 = Label(window, text="...", width=25) .grid(row=11, column=0)
gast1 = Label(window, text="...", width=25) .grid(row=11, column=1)
erg1 =  Label(window, text=algo(1, 2), width=25) .grid(row=11, column=2)
# statt algo(1,2) <-> algo(crawlHeim,crawlGast)
#heim2 = (window, text=eineFUNKTION(), width=25) .grid(row=12, column=0)
#gast2 = (window, text=eineFUNKTION(), width=25) .grid(row=12, column=1)
#heim3 = (window, text=eineFUNKTION(), width=25) .grid(row=13, column=0)
#gast3 = (window, text=eineFUNKTION(), width=25) .grid(row=13, column=1)
#heim4 = (window, text=eineFUNKTION(), width=25) .grid(row=14, column=0)
#gast4 = (window, text=eineFUNKTION(), width=25) .grid(row=14, column=1)
#heim5 = (window, text=eineFUNKTION(), width=25) .grid(row=15, column=0)
#gast5 = (window, text=eineFUNKTION(), width=25) .grid(row=15, column=1)
#heim6 = (window, text=eineFUNKTION(), width=25) .grid(row=16, column=0)
#gast6 = (window, text=eineFUNKTION(), width=25) .grid(row=16, column=1)
#heim7 = (window, text=eineFUNKTION(), width=25) .grid(row=17, column=0)
#gast7 = (window, text=eineFUNKTION(), width=25) .grid(row=17, column=1)
#heim8 = (window, text=eineFUNKTION(), width=25) .grid(row=18, column=0)
#gast8 = (window, text=eineFUNKTION(), width=25) .grid(row=18, column=1)
#heim9 = (window, text=eineFUNKTION(), width=25) .grid(row=19, column=0)
#gast9 = (window, text=eineFUNKTION(), width=25) .grid(row=19, column=1)

window.mainloop()
