from tkinter import *
from tkinter import ttk
from variables import *

from screen_manager import Screen_Manager

def main():

    #creates instance of Tk class, opens "root window" which is main window
    root = Tk()
    #calls window daily organizer
    root.title("Daily Organizer")

    #sets window size to screen width and height
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    menu_bar = Menu(root)
    home_menu = Menu(menu_bar, tearoff = 0)
    home_menu.add_command(label="Menu", 
                          command= lambda: screen_manager.home_cmd())
    menu_bar.add_cascade(label = "Home", menu=home_menu)

    root.config(menu=menu_bar)

    screen_manager = Screen_Manager(root)
    
    screen_manager.change_screen("start") #runs my start screen thats in start_screen.py


    #displays everything and responds to input until terminated
    root.mainloop()




main()