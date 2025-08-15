from tkinter import *
from tkinter import ttk
from .notes_screen import to_notes
from .checklist_screen import to_daylist

def start_screen(root, current_frm = ""):
    if current_frm:
        current_frm.pack_forget()

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
