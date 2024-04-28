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

    cars_button = tk.Button(window, text="cars", command=cars, fg ="black", bg="white")#creates button to go to car page
    cars_button.pack()

def cars(): makes window to show the cars
    carWindow = tk.Tk()
    car_label = tk.Label(carWindow, text="Here is the cars we have on the lot!") #car welcome label
    car_label.pack()

    carList = ['Jeep Patriot', 'Dodge Charger', 'Porsche 911'] #list of cars
    for x in range(0, len(carList)):
        text = tk.Label(carWindow, text=carList[x]) #Loop to print cars out
        text.pack()
    carWindow.title("Cars")


    home_button = tk.Button(carWindow, text="Home", command=home, fg ="black", bg="white") #creates button to return to home page
    home_button.pack()

    
home()
