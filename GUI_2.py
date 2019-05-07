
import tkinter as tk

Window = tk.Tk()
Window.title('Bundesliga Vorhersage')      

def berechneWahrscheinlichkeit():
    wahrscheinlichkeitNumber = 0
    wkt = str(wahrscheinlichkeitNumber)
    label.config(text=wkt)

#Auswahllisten
listbox1 = tk.Listbox(Window)
listbox1.insert(1, ' FC Bayern München') 
listbox1.insert(2, ' VfB Stuttgart') 
listbox1.insert(3, ' Borussia Dortmund') 
listbox1.insert(4, 'FC Schalke 04')

listbox2 = tk.Listbox(Window)
listbox2.insert(1, ' FC Bayern München') 
listbox2.insert(2, ' VfB Stuttgart') 
listbox2.insert(3, ' Borussia Dortmund') 
listbox2.insert(4, 'FC Schalke 04')

#Label
label = tk.Label(Window, text="?") 

#Knöpfe:

#Crawler
crawlerbutton = tk.Button(Window, text = 'Start Crawler', fg ='red') 

#Training
trainingbutton = tk.Button(Window, text = 'Start training', fg ='red') 

#Berechnung starten
calculateButton = tk.Button(Window, text = 'Berechne Gewinnwahrscheinlichkeit', fg ='red', command=berechneWahrscheinlichkeit) 

#Fenster schließen
closebutton = tk.Button(Window, text='Abbrechen', bg= "blue", fg = "white", width=25, command=Window.destroy) 

#Postition in Grid festlegen
listbox1.grid(column=0, row=0)
listbox2.grid(column=1, row=0)
crawlerbutton.grid(column=0, row=1)
trainingbutton.grid(column=1, row=1)
calculateButton.grid(column=2, row=0)
label.grid(column=2, row=1)
closebutton.grid(column=2, row=2)

Window.mainloop() 
