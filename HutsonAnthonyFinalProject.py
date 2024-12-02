"""Author: Anthony Hutson
   Date Written: 9/30/2024
   Program Name: briansPzzaOrdrApp.py
   This program will provide the user with an interactive GUI that will guide the user through 
   ordering menu items. The program will keep list the price amount for each order and will show
   a pay screen once an item is selected. The user will then be prompted to enter credit card information
   which will be validated and then will display whether the information is correct or not."""



#Define Fonts for ease of use
labelFont = ('Comic Sans MS', 20, 'bold')
buttonFont = ('Botthanie', 15, 'bold')

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import re
import PIL

class BriansGUI(tk.Tk):
    
    # __init__ function for class BriansGUI 
    def __init__(self, *args, **kwargs): 
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("400x700")
        self.title("Brian's Pizza")
        self.configure(bg = 'medium sea green')

        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        

        self.frames = {} 
        self.frameStack = []
        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, PickUpMenu, deliveryMenu, wingMenu, pizzaMenu, payWindow):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, PickUpMenu, deliveryMenu respectively with 
            # for loop
            self.frames[F] = frame 

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

    def back(self):
        if self.frameStack:
            last_frame = self.frameStack.pop()
            self.show_frame(last_frame)

    # to display the current frame passed as
    def show_frame(self, cont):
        current_frame = self.current_frame()
        if current_frame and current_frame != cont:
            self.frameStack.append(current_frame)
        frame = self.frames[cont]
        frame.tkraise()

    # to define the current frame for "back()" function
    def current_frame(self):
        for cont, frame in self.frames.items():
            if frame.winfo_viewable():
                return cont
        return None

# Default startpage of program, displayed when user begins. Can also be visited when click the back button in any of the 
# other frames or finish an order and click "continue". Can lead to the Pick-Up or Delivery frames. Can also quit the program.
class StartPage(tk.Frame):
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        logoFile = Image.open("BriansPizzaImage.jpg")
        logoFile = logoFile.resize((200, 200))
        logoImage = ImageTk.PhotoImage(logoFile)

        #Color of window and labels
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")
        
        # Label indicating app name
        label = ttk.Label(self, text ="Brian's Pizza", style = "Style.Label", font = labelFont)
        label.place(x=100, y=0)

        # Label containing logo
        logoLabel = ttk.Label(self, image = logoImage)
        logoLabel.image = logoImage
        logoLabel.place(x=100, y=250)

        # Button to show PickUpMenu
        pickupButton = ttk.Button(self, text ="Pick-Up",
        command = lambda : controller.show_frame(PickUpMenu))
        pickupButton.place(x=50, y=600)

        # Button to show delivery Menu
        deliveryButton = ttk.Button(self, text ="Delivery",
        command = lambda : controller.show_frame(deliveryMenu))
        deliveryButton.place(x=250, y=600)
        
        #Button for Quitting out of the app
        backButton = ttk.Button(self, text ="Quit",
                            command = lambda : controller.destroy())
        backButton.place(x=150, y=650)

        


# Second window visited by user, can be reached from the startpage by clicking Pick-Up button.
# Can lead to the Pizza menu or the wings menu. Can lead to the startpage by clicking the back button.
class PickUpMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Color of window and labels
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")

        # Label to indicate pick up menu
        label = ttk.Label(self, text ="Pick-Up Menu", font = labelFont, style = "Style.Label")
        label.place(x=100, y=0)

        # Button to show pizzaMenu
        pizzaButton = ttk.Button(self, text ="Pizza",
                            command = lambda : controller.show_frame(pizzaMenu))
        pizzaButton.place(x=50,y=600)

        # Button to show wingMenu
        wingsButton = ttk.Button(self, text ="Wings",
                            command = lambda : controller.show_frame(wingMenu))
        wingsButton.place(x=250, y=600)

        # button to go back to previous page
        backButton = ttk.Button(self, text ="Back",
                            command = lambda :  controller.back())
        backButton.place(x=150, y=650)
        

# Second window visited by user, can be reached from the startpage by clicking Delivery button.
# Can lead to the Pizza menu or the wings menu. Can lead to the startpage by clicking the back button.
class deliveryMenu(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Color of window and labels
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")
        
        # Label to indicate delivery menu
        label = ttk.Label(self, text ="Delivery Menu", font = labelFont, style = "Style.Label")
        label.place(x=100, y=0)

        # Button to show pizzaMenu
        pizzaButton = ttk.Button(self, text ="Pizza",
                            command = lambda : controller.show_frame(pizzaMenu))
        pizzaButton.place(x=50, y=600)

        # Button to show wingMenu
        wingsButton = ttk.Button(self, text ="Wings",
                            command = lambda : controller.show_frame(wingMenu))
        wingsButton.place(x=250, y=600)
        
        # button to go back to previous page
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.back())
        backButton.place(x=150, y=650)

# Third window visited by the user. Can be reached from either the delivery menu or the pick-up menu by clicking 
# the wings button. Can reach the startpage by clicking the back button. Can also reach the pay window by clicking 
# either of the wing option buttons.
class wingMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Color of window and labels
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")
        label = ttk.Label(self, text ="Pick-Up Menu", font = labelFont, style = "Style.Label")
        label.place(x=100, y=0)

        # button to show payWindow
        bbqButton = ttk.Button(self, text ="Honey BBQ ($5.00)",
                            command = lambda : controller.show_frame(payWindow))
        bbqButton.place(x=50,y=600)

        # Button to show payWindow
        buffaloButton = ttk.Button(self, text ="Buffalo ($4.50)",
                            command = lambda : controller.show_frame(payWindow))
        buffaloButton.place(x=250, y=600)

        # Button to go back to previous page
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.back())
        backButton.place(x=150, y=650)
        

# Third window visited by the user. Can be reached from either the delivery menu or the pick-up menu by clicking 
# the pizza button. Can reach the startpage by clicking the back button. Can also reach the pay window by clicking 
# either of the pizza option buttons.
class pizzaMenu(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Color of window and labels
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background = "medium sea green")


        pizzaFile = Image.open("PizzaImage.jpg")
        pizzaFile = pizzaFile.resize((200, 200))
        pizzaImage = ImageTk.PhotoImage(pizzaFile)

        # Label to indicate pizza frame
        label = ttk.Label(self, text ="Pizza Menu", font = labelFont, style = "Style.Label")
        label.place(x=100, y=0)

        # Label that contains pizza image
        pizzaImageLabel = ttk.Label(self, image = pizzaImage)
        pizzaImageLabel.image = pizzaImage
        pizzaImageLabel.place(x=125, y=200)

        # Button to show payWindow
        pepperoniButton = ttk.Button(self, text ="Pepperoni ($9.50)",
                            command = lambda : controller.show_frame(payWindow))
        pepperoniButton.place(x=50, y=600)

        # Button to show payWindow
        cheeseButton = ttk.Button(self, text ="Cheese ($7.50)",
                            command = lambda : controller.show_frame(payWindow))
        cheeseButton.place(x=250, y=600)
        
        # Button to go back to previous page
        backButton = ttk.Button(self, text ="Back",
                            command = lambda : controller.back())
        backButton.place(x=150, y=650)

# Fourth window reached by the user. Can be reached from the pizzaMenu or the wingsMenu. Will test data for the name on card value
# and the card number value. If information isn't valid an error will appear on the window. Can reach the start page by either clicking 
# the back button or the continue button, which appears after valid data has been entered and the pay button has been clicked.
class payWindow(tk.Frame):
    def __init__(self, parent, controller):
        #Color of window and labels
        tk.Frame.__init__(self, parent)
        self.configure(bg="medium sea green")
        style = ttk.Style()
        style.configure("Style.Label", background="medium sea green")

        # Label to indicate Payment Window frame
        label = ttk.Label(self, text="Payment Window", font=labelFont, style="Style.Label")
        label.place(x=100, y=0)

        # Name on card entry label
        nameLabel = ttk.Label(self, text="Name on Card:", font=labelFont, style="Style.Label")
        nameLabel.place(x=50, y=100)

        # Name on card entry line
        self.nameEntry = tk.Entry(self, font=('Arial', 16), width=20)
        self.nameEntry.place(x=50, y=150)
        
        # Card number entry label
        entry_label = ttk.Label(self, text="Enter Credit Card Number:", font=labelFont, style="Style.Label")
        entry_label.place(x=50, y=200)

        # Card number entry line
        self.cardEntry = tk.Entry(self, font=('Arial', 16), width=20)
        self.cardEntry.place(x=50, y=250)

        # Bind the key release event to format the card number
        self.cardEntry.bind('<KeyRelease>', self.format_card_number)  # Highlighted

        # Label to display either errors or that the payment has been processed
        self.messageLabel = ttk.Label(self, text="", font=('Arial', 12, 'bold'), foreground="red", background="medium sea green")
        self.messageLabel.place(x=50, y=350)

        # Button to submit payment information
        payButton = ttk.Button(self, text="Pay", command=self.pay)
        payButton.place(x=150, y=290)

        # Button for going to the previous screen
        backButton = ttk.Button(self, text="Back", command=lambda: controller.back())
        backButton.place(x=150, y=650)

        self.continueButton = ttk.Button(self, text="Continue", command=lambda: controller.show_frame(StartPage))
        self.continueButton.place(x=150, y=400)
        self.continueButton.place_forget()     

    # Highlighted method to format card number
    def format_card_number(self, event):
        # Remove any non-digit characters
        card_number = ''.join(filter(str.isdigit, self.cardEntry.get()))

        # Format the card number into groups of 4 digits
        formatted_number = ' '.join(card_number[i:i + 4] for i in range(0, len(card_number), 4))

        # Update the entry with the formatted number
        self.cardEntry.delete(0, tk.END)
        self.cardEntry.insert(0, formatted_number)

    # Ability to update the message label after user fixes error
    def clearMessage(self, event):
        self.messageLabel.config(text="")  # Clear the message label

    def pay(self):
        customerName = self.nameEntry.get().strip()
        if not customerName:
            # Changed to use messageLabel to display error
            self.messageLabel.config(text="Error: Name on card cannot be empty.")
            return
        if not re.match(r"^[A-Za-z\s]+$", customerName):
            self.messageLabel.config(text="Error: Name can only contain letters and spaces.")
            return

        card_number = self.cardEntry.get().replace(" ", "").strip()
        if not card_number.isdigit() or len(card_number) != 16:
            self.messageLabel.config(text="Error: Invalid credit card number. \n It should be 16 digits long.")
            return

        firstName = customerName.split()[0]

        # Changed to use messageLabel to display success message
        self.messageLabel.config(text=f"Processing payment for: {firstName}")
        self.continueButton.place(x=50, y=650)

# Driver Code
app = BriansGUI()
app.mainloop()