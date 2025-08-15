from tkinter import *
from tkinter import ttk

def to_daylist(current_frm, root):

    current_frm.pack_forget()

    daylist_frm = ttk.Frame(root, padding=10)
    daylist_frm.pack(fill = "both", expand=True)

    welcome_msg = ttk.Label(daylist_frm, text="Welcome to your daily checklist")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER)