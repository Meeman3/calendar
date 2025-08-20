from tkinter import *
from tkinter import ttk
from variables import *
import os
from screen_manager import Screen_Manager

#checks if dictionaries directory exists, if not makes one
if not os.path.exists("dictionaries"):
    os.makedirs("dictionaries")

def main():

    #creates instance of Tk class, opens "root window" which is main window
    root = Tk()

    #calls window daily organizer
    root.title("Daily Organiser")

    #sets window size to screen width and height (can change later through some settings menu)
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    #makes a menu bar with option Menu which has option Home, takes to main screen
    menu_bar = Menu(root)
    home_menu = Menu(menu_bar, tearoff = 0)
    home_menu.add_command(label="Menu", 
                          command= lambda: screen_manager.home_cmd())
    menu_bar.add_cascade(label = "Home", menu=home_menu)

    #puts menu bar onto root, meaning will always be on screen
    root.config(menu=menu_bar)

    #makes a screen manager which will handle and track screens
    screen_manager = Screen_Manager(root)

    #runs my start screen thats in start_screen.py
    screen_manager.change_screen("start")


    #displays everything and responds to input until terminated
    root.mainloop()




main()