from tkinter import *
from tkinter import ttk

def to_notes(current_frm, root):

    current_frm.pack_forget()

    notes_frm = ttk.Frame(root, padding=10)
    notes_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(notes_frm, text="Welcome to notes")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm
