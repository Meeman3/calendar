from tkinter import *
from tkinter import ttk


def to_daylist(root, screen_manager):

    daylist_frm = ttk.Frame(root, padding=10)
    daylist_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(daylist_frm, text="Welcome to your daily checklist")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER)

    back_btn = ttk.Button(daylist_frm, text="Back", command=lambda:  screen_manager.go_back(daylist_frm))
    back_btn.place(relx=0.9, rely=0.9)