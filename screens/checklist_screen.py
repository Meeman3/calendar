from tkinter import *
from tkinter import ttk
import functions


def to_daylist(root, screen_manager, date=functions.today):

    day = functions.day(date)
    yesterday = functions.yesterday(date)
    tomorrow = functions.tomorrow(date)
    

    daylist_frm = ttk.Frame(root, padding=10)
    daylist_frm.pack(fill = "both", expand=True)

    screen_manager.current_frame = daylist_frm

    
    welcome_msg = ttk.Label(daylist_frm,
                             text=f"Welcome to your daily checklist\nCurrent date: {date}\n{day}")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER)

    #button that takes you to add list screen
    add_to_list_btn = ttk.Button(daylist_frm, 
                                 text="Update list", 
                                 command=lambda:  screen_manager.change_screen("add_list", daylist_frm))
    add_to_list_btn.place(relx=0.7, rely=0.5 )

    #button that takes you to yesterdays list
    prev_list_btn = ttk.Button(daylist_frm, 
                                 text="Yesterday's list", 
                                 command=lambda:  screen_manager.change_screen("checklist", 
                                                                               daylist_frm, 
                                                                               date=yesterday)
                                 )
    prev_list_btn.place(relx=0.2, rely=0.4)

    #button that takes you to tomorrows list
    next_list_btn = ttk.Button(daylist_frm, 
                                 text="Tomorrow's list",
                                 command=lambda:  screen_manager.change_screen("checklist", 
                                                                               daylist_frm, 
                                                                               date=tomorrow) 
                                 )
    next_list_btn.place(relx=0.2, rely=0.6)

    #if current page isnt today makes button that takes to todays list
    if date != functions.today:
            today_list_btn = ttk.Button(daylist_frm, 
                                 text="Today's list",
                                 command=lambda:  screen_manager.change_screen("checklist", 
                                                                               daylist_frm, 
                                                                               date=functions.today) 
                                 )
            today_list_btn.place(relx=0.2, rely=0.5)

    #back button
    back_btn = ttk.Button(daylist_frm, text="Back", command=lambda:  screen_manager.go_back(daylist_frm))
    back_btn.place(relx=0.9, rely=0.9)
