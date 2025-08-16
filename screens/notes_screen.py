from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import functions
from dictionaries.notes_dict import notes_dict


def to_notes(root, screen_manager, date=functions.today):

    notes_frm = ttk.Frame(root, padding=10)
    notes_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(notes_frm, text="Welcome to notes")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    welcome_msg = ttk.Label(notes_frm, text="Please choose an option:")
    welcome_msg.place(relx=0.5, rely=0.35, anchor=CENTER) #centres in frm

    back_btn = ttk.Button(notes_frm, text="Back", command=lambda: screen_manager.go_back(notes_frm))
    back_btn.place(relx=0.9, rely=0.9)

    add_notes_btn = ttk.Button(notes_frm, 
                                 text="Add notes", 
                                 command=lambda:  screen_manager.change_screen("add_notes", notes_frm))
    add_notes_btn.place(relx=0.8, rely=0.5 )

    if notes_dict:
        notes_area = scrolledtext.ScrolledText(notes_frm, width = 100, height = 20)
        notes_area.place(relx = 0.5, rely= 0.5, anchor=CENTER)

        notes_area_frm = ttk.Frame(notes_area, padding=10)
        notes_area_frm.pack(fill = "both", expand=True)

        for title in notes_dict.keys():
            note_button = ttk.Button(notes_area_frm,
                                      text=title,
                                       command=lambda title_temp = title: 
                                       screen_manager.change_screen("read_notes",
                                                                                     notes_frm,
                                                                                     title=title_temp))
            note_button.pack(side=TOP, expand=TRUE, fill=BOTH)
        
        
