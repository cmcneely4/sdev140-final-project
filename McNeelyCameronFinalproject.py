"""
Program:mcneelycameronFinalproject
Date:24April2024
Author:Cameron McNeely
This program is designed to act as a sort of website for a car lot.
It will build a GUI that the user can browse cars on, favorite cars, and even
their own custom vehicle if they choose.
"""
import tkinter as tk


def home():
    window =tk.Tk()#creates main window
    window.title("Cam's car lot")#sets title of window
    window.minsize(100, 100)

    welcome_label=tk.Label(window, text="Welcome to Cam's Car Lot")#creates welcome label
    welcome_label.pack()
                   

    cars_button = tk.Button(window, text="cars", command=carPage, fg ="black", bg="white")#creates button to go to car page
    cars_button.pack()

def carPage(): #makes window to show the cars
    carWindow = tk.Tk()
    car_label = tk.Label(carWindow, text="Here is the cars we have on the lot!") #car welcome label
    car_label.grid()

    carList = ['Jeep Patriot', 'Dodge Charger', 'Porsche 911'] #list of cars
    for x in range(0, len(carList)):
        text = tk.Label(carWindow, text=carList[x]) #Loop to print cars out
        text.grid()
    carWindow.title("Cars")


    home_button = tk.Button(carWindow, text="Home", command=home, fg ="black", bg="white") #creates button to return to home page
    home_button.grid()

    patriot_button = tk.Button(carWindow, text="View", command=patriot, fg ="black", bg="white",)#Creates button to view the patriot page
    patriot_button.grid(row=1, column=1)

    charger_button = tk.Button(carWindow, text="View", command=charger, fg ="black", bg="white",)#Creates button to view the charger page
    charger_button.grid(row=2, column=1)

    porsche_button = tk.Button(carWindow, text="View", command=porsche, fg ="black", bg="white",)#Creates button to view the porsche page
    porsche_button.grid(row=3, column=1)


def patriot():#creates window to show off the patriot
    patriotWindow = tk.Tk()
    patriottext_Label = tk.Label(patriotWindow, text = "Maker:Jeep\n Model:Patriot\n Mileage:1243\n Price:$40,000")#displays the information about the patriot
    patriottext_Label.pack()

    back_button = tk.Button(patriotWindow, text="Back", command=carPage, fg ="black", bg="white")#creates a button to go back to the car page
    back_button.pack()

def charger():#creates window to show off the charger
    chargerWindow = tk.Tk()
    chargertext_Label = tk.Label(chargerWindow, text = "Maker:Dodge\n Model:Charger\n Mileage:423\n Price:$80,000")#displays the information about the charger
    chargertext_Label.pack()

    back_button = tk.Button(chargerWindow, text="Back", command=carPage, fg ="black", bg="white")#creates a button to go back to the car page
    back_button.pack()

def porsche():#creates window to show off the porsche
    porscheWindow = tk.Tk()
    porschetext_Label = tk.Label(porscheWindow, text = "Maker:Porsche\n Model:911\n Mileage:241\n Price:$120,000")#displays the information about the porsche
    porschetext_Label.pack()

    back_button = tk.Button(porscheWindow, text="Back", command=carPage, fg ="black", bg="white")#creates a button to go back to the car page
    back_button.pack()

    
home()
