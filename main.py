from tkinter import *
from tkinter import ttk
from variables import *
from screens.notes_screen import to_notes
from screens.checklist_screen import to_daylist
from screens.start_screen import start_screen
from screen_manager import Screen_Manager

def main():

    #creates instance of Tk class, opens "root window" which is main window
    root = Tk()
    #calls window notes
    root.title("Notes")
    #sets window size to screen width and height
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    screen_manager = Screen_Manager(root)
    
    start_screen(root, screen_manager) #runs my start screen thats in start_screen.py


    #displays everything and responds to input until terminated
    root.mainloop()




main()