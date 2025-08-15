from tkinter import *
from tkinter import ttk
import functions


def to_daylist(root, screen_manager, date=functions.today):

    day = functions.day(date)
    

    daylist_frm = ttk.Frame(root, padding=10)
    daylist_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(daylist_frm,
                             text=f"Welcome to your daily checklist\nCurrent date: {date}\n{day}")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER)

    add_to_list_btn = ttk.Button(daylist_frm, 
                                 text="Update list", 
                                 command=lambda:  screen_manager.change_screen("add_list", daylist_frm))
    add_to_list_btn.place(relx=0.7, rely=0.5 )

    prev_list_btn = ttk.Button(daylist_frm, 
                                 text="Yesterday's list", 
                                 )
    prev_list_btn.place(relx=0.2, rely=0.45)

    next_list_btn = ttk.Button(daylist_frm, 
                                 text="Tomorrow's list", 
                                 )
    next_list_btn.place(relx=0.2, rely=0.55)


    back_btn = ttk.Button(daylist_frm, text="Back", command=lambda:  screen_manager.go_back(daylist_frm))
    back_btn.place(relx=0.9, rely=0.9)
