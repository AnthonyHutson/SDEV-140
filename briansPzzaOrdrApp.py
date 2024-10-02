"""Author: Anthony Hutson
   Date Written: 9/30/2024
   Program Name: briansPzzaOrdrApp.py
   This program will provide the user with an interactive GUI that will guide the user through 
   ordering menu items. Throughout the ordering process, the program will keep track of the subtotal
   and will show the user the total cost on the pay screen."""

import tkinter as tk
from tkinter import font

#Declare the SuperClass
class BriansGUI():
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("400x700")
        self.root.configure(bg='medium sea green')
    
        self.label = tk.Label(self.root, text="Brian's Pizza", font=('Comic Sans MS', 20), bg='black', fg='snow', borderwidth=10)
        self.label.place(x=120, y=0)

        self.pckUpButton = tk.Button(self.root, text="Pick-Up", font=('Botthanie', 15, 'bold'), bg='white', fg='black', borderwidth=5)
        self.pckUpButton.place(x=50,y=600)

        self.delivryButton = tk.Button(self.root, text="Delivery", font=('Botthanie', 15, 'bold'), bg='white', fg='black', borderwidth=5)
        self.delivryButton.place(x=250, y=600)

        self.root.mainloop()
        
BriansGUI()