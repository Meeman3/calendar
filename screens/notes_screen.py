from tkinter import *
from tkinter import ttk


def to_notes(root, screen_manager):

    notes_frm = ttk.Frame(root, padding=10)
    notes_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(notes_frm, text="Welcome to notes")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    back_btn = ttk.Button(notes_frm, text="Back", command=lambda: screen_manager.go_back(notes_frm))
    back_btn.place(relx=0.9, rely=0.9)
