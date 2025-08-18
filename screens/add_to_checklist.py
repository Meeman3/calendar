from tkinter import *
from tkinter import ttk


def add_list(root, screen_manager):

    add_list_frm = ttk.Frame(root, padding=10)
    add_list_frm.pack(fill = "both", expand=True)

    screen_manager.current_frame = add_list_frm 


    add_list_msg = ttk.Label(add_list_frm, text="What would you like to add to the list?")
    add_list_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    # shows where to input new check
    input_msg = ttk.Label(add_list_frm, text="Input text here:")
    input_msg.place(relx=0.4, rely=0.4, anchor=CENTER)

    #place to input new check
    new_check = ttk.Entry(add_list_frm, width= 100)
    new_check.place(relx=0.7, rely=0.4, anchor=CENTER)

    #shows where to input wanted date
    date_msg = ttk.Label(add_list_frm, 
                         text="Date for checklist entry YYYY-MM-DD\n(leave blank for today)")
    date_msg.place(relx=0.4, rely= 0.3, anchor=CENTER)

    #date input
    pick_date = ttk.Entry(add_list_frm, width= 20)
    pick_date.place(relx=0.55, rely=0.3, anchor=CENTER)

    #unfinished buttons
    daily_repeat = ttk.Button(add_list_frm, 
                         text="Repeat daily")
    daily_repeat.place(relx=0.35, rely= 0.5, anchor=CENTER)

    weekly_repeat = ttk.Button(add_list_frm, 
                         text="Repeat weekly")
    weekly_repeat.place(relx=0.45, rely= 0.5, anchor=CENTER)

    monthly_repeat = ttk.Button(add_list_frm, 
                         text="Repeat monthly")
    monthly_repeat.place(relx=0.55, rely= 0.5, anchor=CENTER)

    yearly_repeat = ttk.Button(add_list_frm, 
                         text="Repeat yearly")
    yearly_repeat.place(relx=0.65, rely= 0.5, anchor=CENTER)

    #button to confirm entry
    add_btn = ttk.Button(add_list_frm, 
                         text="Add check")
    add_btn.place(relx=0.5, rely= 0.6, anchor=CENTER)

    back_btn = ttk.Button(add_list_frm, text="Back", command=lambda: screen_manager.go_back(add_list_frm))
    back_btn.place(relx=0.9, rely=0.9)

