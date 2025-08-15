from tkinter import *
from tkinter import ttk
from variables import *
from screens.notes_screen import to_notes
from screens.checklist_screen import to_daylist
from screens.start_screen import start_screen

def main():

    #creates instance of Tk class, opens "root window" which is main window
    root = Tk()
    #calls window notes
    root.title("Notes")
    #sets window size to screen width and height
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    
    start_screen(root)


    #displays everything and responds to input until terminated
    root.mainloop()




main()