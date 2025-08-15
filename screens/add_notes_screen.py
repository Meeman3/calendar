from tkinter import *
from tkinter import ttk
import functions

def add_notes(root, screen_manager):

    add_notes_frm = ttk.Frame(root, padding=10)
    add_notes_frm.pack(fill = "both", expand=True)

    add_notes_msg = ttk.Label(add_notes_frm, text="What note would you like to add?")
    add_notes_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    input_msg = ttk.Label(add_notes_frm, text="Input text here:")
    input_msg.place(relx=0.4, rely=0.35, anchor=CENTER)

    new_note = Text(add_notes_frm, width= 100, height = 20)
    new_note.place(relx=0.7, rely=0.5, anchor=CENTER)

    title_msg = ttk.Label(add_notes_frm, 
                         text="Title")
    title_msg.place(relx=0.4, rely= 0.3, anchor=CENTER)

    pick_title = ttk.Entry(add_notes_frm, width= 100)
    pick_title.place(relx=0.71, rely=0.3, anchor=CENTER)




    add_btn = ttk.Button(add_notes_frm, 
                         text="Add note")
    add_btn.place(relx=0.5, rely= 0.7, anchor=CENTER)




    back_btn = ttk.Button(add_notes_frm, text="Back", command=lambda: screen_manager.go_back(add_notes_frm))
    back_btn.place(relx=0.9, rely=0.9)

