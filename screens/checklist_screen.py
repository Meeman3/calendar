from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
import functions
import datetime
from dateutil.relativedelta import relativedelta
from screens.add_to_checklist import daylist_update, valid_date, update_daylist_dict, write_daylist_dict


#   if dict files dont exist make temp dicts
try:
    from dictionaries.checklist_dict import daylist_dict
except ImportError:
    daylist_dict = {}

try:
    from dictionaries.recurring_check_dict import recurring_check_dict
except ImportError:
    recurring_check_dict = {}



#   function that creates the checklist screen
def to_daylist(root, screen_manager, date=functions.today, edit_mode = False):

    #   function for edit button, toggles deletion buttons
    def toggle_edit_list():
        nonlocal toggle_edit
        toggle_edit = not toggle_edit

        #   makes it so this screen refresh isnt added to screen history
        screen_manager.change_screen("checklist", daylist_frm, date=date, edit_mode=toggle_edit, back=True)

    #   function that sets checklist dict entries to reflect checkbutton state
    def checkbutton_value(date, repeat, entry, var):
        if var.get() == 1:
            daylist_update(date, repeat, entry, True)
        else:
            daylist_update(date, repeat, entry, False)

    #   function that allows changing date of checklist
    def goto_date(date_text_box):
        check_date = valid_date(date_text_box, date)
        if check_date == "bad date":
            invalid_date_msg = ttk.Label(daylist_frm, text="Please input a valid date of form YYYY-MM-DD")
            invalid_date_msg.place(relx=0.22, rely=0.27, anchor=CENTER) #centres in frm
            return
        go_date = datetime.datetime.strptime(check_date, "%Y-%m-%d").date()
        screen_manager.change_screen("checklist", daylist_frm, date = go_date)

    #   functionn for check deletion
    def delete_check(repeat, entry, amount= "single"):

        #   if deleting single entry, deletes entry and closes any empty dicts
        if amount == "single":
            del daylist_dict[str(date)][repeat][entry]
            if not daylist_dict[str(date)][repeat]:
                del daylist_dict[str(date)][repeat]
                if not daylist_dict[str(date)]:
                    del daylist_dict[str(date)]

        #   if deleting all entries, deletes entry from recurring dict so it doesnt recur and 
        #   deletes all entries from daylist dict, closing empty dicts
        elif amount == "all":
            if repeat in recurring_check_dict and entry in recurring_check_dict[repeat]:
                del recurring_check_dict[repeat][entry]
            
            for date_ in list(daylist_dict.keys()):
                if repeat in daylist_dict[date_]:
                    if entry in daylist_dict[date_][repeat]:
                        del daylist_dict[date_][repeat][entry]

                        if not daylist_dict[date_][repeat]:
                            del daylist_dict[date_][repeat]
                            if not daylist_dict[date_]:
                                del daylist_dict[date_]


        #   updates both dicts
        with open("dictionaries/recurring_check_dict.py", "w") as rcd:
            rcd.write(f"recurring_check_dict = {recurring_check_dict}")

        with open("dictionaries/checklist_dict.py", "w") as cd:
            cd.write(f"daylist_dict ={daylist_dict}")
            
        #   refreshes screen
        screen_manager.change_screen("checklist", daylist_frm, date = date)

    #   function that checks if date should have entry from recurring dict
    def recurring_date_checker(input_date, entry_date, repeat):

        #   makes sure right format
        if isinstance(entry_date, str):
            entry_date = datetime.datetime.strptime(entry_date, "%Y-%m-%d").date()

        #   checks if date satisfies conditions of each recursion type
        date_diff = relativedelta(input_date, entry_date)
        if repeat == "daily":
            return True
        elif repeat == "weekly":
            week_diff = input_date - entry_date
            return week_diff.days >= 0 and week_diff.days % 7 == 0
        elif repeat == "monthly":
            return date_diff.days == 0 and date_diff.months >= 0 and date_diff.years >= 0
        elif repeat == "yearly":
            return date_diff.days == 0 and date_diff.months == 0 and date_diff.years >= 0


    #   function that updates checklist with recurring entries from above func
    def generate_recurring_entries(date):
        for repeat, entry_dict in recurring_check_dict.items():
            for entry, info_dict in entry_dict.items():
                entry_date = info_dict["start_date"]

                if recurring_date_checker(date, entry_date, repeat):
                    update_daylist_dict(date, repeat, entry, False)
                    write_daylist_dict()

    #   updates daylist to ensure all entries present
    generate_recurring_entries(date)
    
    #   used to check if in edit mode
    toggle_edit = edit_mode

    #   gets functions for the current list's date
    day = functions.day(date)
    yesterday = functions.yesterday(date)
    tomorrow = functions.tomorrow(date)
    
    #   makes frame
    daylist_frm = ttk.Frame(root, padding=10)
    daylist_frm.pack(fill = "both", expand=True)

    #   used in home button
    screen_manager.current_frame = daylist_frm

    
    welcome_msg = ttk.Label(daylist_frm,
                             text=f"Welcome to your daily checklist\nCurrent date: {date}\n{day}")
    welcome_msg.place(relx=0.5, rely=0.25, anchor=CENTER)

    #   button that takes you to add list screen
    add_to_list_btn = ttk.Button(daylist_frm, 
                                 text="Update list", 
                                 command=lambda:  screen_manager.change_screen("add_list", daylist_frm, date=date))
    add_to_list_btn.place(relx=0.8, rely=0.5 )

    #   button that takes you to yesterdays list
    prev_list_btn = ttk.Button(daylist_frm, 
                                 text="Yesterday's list", 
                                 command=lambda:  screen_manager.change_screen("checklist", 
                                                                               daylist_frm, 
                                                                               date=yesterday)
                                 )
    prev_list_btn.place(relx=0.2, rely=0.4)

    #   button that takes you to tomorrows list
    next_list_btn = ttk.Button(daylist_frm, 
                                 text="Tomorrow's list",
                                 command=lambda:  screen_manager.change_screen("checklist", 
                                                                               daylist_frm, 
                                                                               date=tomorrow) 
                                 )
    next_list_btn.place(relx=0.2, rely=0.6)

    #   if current page isnt today makes button that takes to todays list
    if date != functions.today:
            today_list_btn = ttk.Button(daylist_frm, 
                                 text="Today's list",
                                 command=lambda:  screen_manager.change_screen("checklist", 
                                                                               daylist_frm, 
                                                                               date=functions.today) 
                                 )
            today_list_btn.place(relx=0.2, rely=0.5)

    #   back button
    back_btn = ttk.Button(daylist_frm, text="Back", command=lambda:  screen_manager.go_back(daylist_frm))
    back_btn.place(relx=0.9, rely=0.9)

    #   go to date
    goto_date_label = ttk.Label(daylist_frm, text= "Change to a different date?")
    goto_date_label.place(relx=0.2, rely=0.26)

    goto_date_entry = ttk.Entry(daylist_frm,
                                 width=20)
    goto_date_entry.place(relx=0.2, rely=0.28)

    goto_date_btn = ttk.Button(daylist_frm,
                                text="Change date",
                                 command= lambda: goto_date(goto_date_entry))
    goto_date_btn.place(relx=0.2, rely=0.3)

    #   button to enable delete mode
    edit_list_btn = ttk.Button(daylist_frm,
                                text="Delete check",
                                 command=lambda: toggle_edit_list())
    edit_list_btn.place(relx=0.8, rely=0.3)

    
    #   checks current list, telling user if it's empty
    try:
        checklist_date = daylist_dict[str(date)]
    except:
        goto_date_label = ttk.Label(daylist_frm, text= "This date's list is currently empty\n    consider adding to it!")
        goto_date_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        
    #   if current list isnt empty, makes scrollable checklist of list's checks
    if checklist_date:
        checklist_area = scrolledtext.ScrolledText(daylist_frm,width = 100, height = 20)
        checklist_area.place(relx = 0.5, rely= 0.5, anchor=CENTER)

        checklist_area_frm = Frame(checklist_area)
        checklist_area_frm.pack(fill = "both", expand=True)

        #   adds checkbutton for each entry in list
        for repeat in checklist_date.keys():
            
            daily_repeats = checklist_date[repeat]
            for entry in daily_repeats.keys():

                entry_frm = Frame(checklist_area_frm)
                entry_frm.pack(fill="x", pady=2)


                #   variable used to sync checkbuttons with daylist dict entry boolean 
                var = IntVar()
                if daily_repeats[entry] == True:
                    var.set(1)
                else:
                    var.set(0)
                 
                check_button = Checkbutton(entry_frm,
                                            text=entry, 
                                             variable=var,
                                             onvalue=1,
                                             offvalue=0,
                                             command= lambda d=date, r=repeat, e=entry, v=var: 
                                             checkbutton_value(d, r, e, v))
                check_button.pack(side=LEFT)
                
                #   if in edit mode, shows deletion button
                if toggle_edit == True:

                    #   only shows recursive delete for recursive entries
                    if repeat != "single":
                        delete_recursive_btn = Button(entry_frm,
                                          text = "DEL REPEATS",
                                           activebackground= "red4",
                                            command = lambda r = repeat, e = entry: delete_check(r, e, amount="all"))
                        delete_recursive_btn.pack(side=RIGHT)


                    delete_btn = Button(entry_frm,
                                          text = "X",
                                           activebackground= "firebrick2",
                                            command = lambda r = repeat, e = entry: delete_check(r, e))
                    delete_btn.pack(side=RIGHT)




        
