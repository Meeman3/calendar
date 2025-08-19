from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import functions
from dictionaries.checklist_dict import daylist_dict
from screens.add_to_checklist import daylist_update


def to_daylist(root, screen_manager, date=functions.today):

    def checkbutton_value(date, repeat, entry):
        if var.get() == 1:
            daylist_update(date, repeat, entry, True)
        else:
            daylist_update(date, repeat, entry, False)
            

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
    add_to_list_btn.place(relx=0.8, rely=0.5 )

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

    checklist_date = daylist_dict[str(date)]

        
    if checklist_date:
        checklist_area = scrolledtext.ScrolledText(daylist_frm,width = 100, height = 20)
        checklist_area.place(relx = 0.5, rely= 0.5, anchor=CENTER)

        checklist_area_frm = Frame(checklist_area)
        checklist_area_frm.pack(fill = "both", expand=True)

        for repeat in checklist_date.keys():
            print(f"Processing repeat type: {repeat}")
            
            daily_repeats = checklist_date[repeat]
            for entry in daily_repeats.keys():
                print(f"Creating checkbox for: {entry}")
                var = IntVar()
                if daily_repeats[entry] == True:
                    var.set(1)
                else:
                    var.set(0)
                 
                check_button = Checkbutton(checklist_area_frm,
                                            text=entry, 
                                             variable=var,
                                             onvalue=1,
                                             offvalue=0,
                                             command= lambda r=repeat, e=entry: 
                                             checkbutton_value(date, r, e))
                check_button.pack(side=TOP, anchor="w")

        

    #back button
    back_btn = ttk.Button(daylist_frm, text="Back", command=lambda:  screen_manager.go_back(daylist_frm))
    back_btn.place(relx=0.9, rely=0.9)
