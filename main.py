from tkinter import *
from tkinter import ttk
from variables import *
from functions import to_notes

def main():

    #creates instance of Tk class, opens "root window" which is main window
    root = Tk()
    #calls window notes
    root.title("Notes")
    #sets window size to screen width and height
    root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    #creates frame inside window
    start_frm = ttk.Frame(root, padding=10)
    start_frm.pack(fill = "both", expand=True) # packs frm to fill full window


    #specifies layout of label in window
    welcome_msg = ttk.Label(start_frm, text="        Welcome to notes\n\nWhat do you want to access?")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm


    #specifies layout of button in frame, when pressed calls destroy for root window
    quit_btn = ttk.Button(start_frm, text="Quit", command=root.destroy)
    quit_btn.place(relx=0.9, rely=0.9)

    notes_btn = ttk.Button(start_frm, text="Notes", command=lambda: to_notes(start_frm, root))
    notes_btn.place(relx=0.5, rely=0.4, anchor=CENTER)

    checklist_btn = ttk.Button(start_frm, text="Daily Checklist", command=lambda: to_daylist(start_frm, root))
    checklist_btn.place(relx=0.5, rely=0.5, anchor=CENTER)



    #displays everything and responds to input until terminated
    root.mainloop()

def to_notes(current_frm, root):

    current_frm.destroy()

    notes_frm = ttk.Frame(root, padding=10)
    notes_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(notes_frm, text="Welcome to notes")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    return

def to_daylist(current_frm, root):

    current_frm.destroy()

    daylist_frm = ttk.Frame(root, padding=10)
    daylist_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(daylist_frm, text="Welcome to your daily checklist")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER)

main()