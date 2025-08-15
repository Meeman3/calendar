from tkinter import *
from tkinter import ttk


def start_screen(root, screen_manager):



    #creates frame inside window
    start_frm = ttk.Frame(root, padding=10)
    start_frm.pack(fill = "both", expand=True) # packs frm to fill full window

    #specifies layout of label in window
    welcome_msg = ttk.Label(start_frm, text="        Welcome to notes\n\nWhat do you want to access?")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    #specifies layout of button in frame, when pressed calls to_notes
    notes_btn = ttk.Button(start_frm,
                            text="Notes",
                            command=lambda: screen_manager.change_screen("notes", start_frm))
    notes_btn.place(relx=0.5, rely=0.4, anchor=CENTER)

    checklist_btn = ttk.Button(start_frm,
                                text="Daily Checklist",
                                command=lambda: screen_manager.change_screen("checklist", start_frm))
    checklist_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

    if screen_manager.screen_hist != ["start"]:

        back_btn = ttk.Button(start_frm, text="Back", command= lambda: screen_manager.go_back(start_frm))
        back_btn.place(relx=0.9, rely=0.9)