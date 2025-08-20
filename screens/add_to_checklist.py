from tkinter import *
from tkinter import ttk
import functions 
from dictionaries.checklist_dict import daylist_dict
from dictionaries.recurring_check_dict import recurring_check_dict


def daylist_update(date, repeat, entry, bool = False, num_of_occurance = "none"):
    if repeat != "single":

        recursive_date = date
        if num_of_occurance == "none":
            add_to_recurring_dict(date, repeat, entry)
            write_recurring_check_dict()
            return

        else:
            for i in range(num_of_occurance):
                update_daylist_dict(recursive_date, repeat, entry, bool)

                if repeat == "daily":
                    recursive_date = functions.tomorrow(recursive_date)
                elif repeat == "weekly":
                    recursive_date = functions.next_week(recursive_date)
                elif repeat == "monthly":
                    recursive_date = functions.next_month(recursive_date)
                elif repeat == "yearly":
                    recursive_date = functions.next_year(recursive_date)

    else:
        update_daylist_dict(date, repeat, entry, bool)

    write_daylist_dict()

def add_to_recurring_dict(date, repeat, entry):
    if repeat in recurring_check_dict.keys():
        repeat_date_dict = recurring_check_dict[repeat]
        if entry in repeat_date_dict.keys():
            entry_dict = repeat_date_dict[entry]
            entry_dict.update({"start_date": date,
                                 "active": True})
        else:
            repeat_date_dict.update({entry: 
                             {"start_date": date,
                                 "active": True
                                 }
                            }
                        )


    else:
        recurring_check_dict[repeat] = {entry: 
                             {"start_date": date,
                                 "active": True
                                 }
                            }
                        
        
def write_recurring_check_dict():
    with open("dictionaries/recurring_check_dict.py", "w") as rcd:
        rcd.write(f"recurring_check_dict = {recurring_check_dict}")
                             


def update_daylist_dict(date, repeat, entry, bool):
    if str(date) in daylist_dict.keys():
        date_dict = daylist_dict[str(date)]
        if repeat in date_dict.keys():
            repeat_dict = date_dict[repeat]
            repeat_dict.update({entry: bool})
        else:
            date_dict.update({repeat: {entry: bool}})
    else:
        date_dict = {repeat: {entry: bool}}

    
    daylist_dict.update({str(date): date_dict})

def write_daylist_dict():
    with open("dictionaries/checklist_dict.py", "w") as dl:
        dl.write(f"daylist_dict= {daylist_dict}")


def valid_date(date_text_box, date):
    if functions.get_text(date_text_box) != "":
            check_date = functions.get_text(date_text_box)
    else:
        check_date = str(date)
    

    try:
        input_date = check_date.split("-")
        input_year = input_date[0]
        input_month = input_date[1]
        input_day = input_date[2]
        if not input_year.isdigit() or not input_month.isdigit() or not input_day.isdigit():
            return "bad date"
        if len(input_year) !=4 or len(input_month) !=2 or len(input_day) !=2:
            return "bad date"
        if functions.date_checker(check_date) == False:
            return "bad date"
    except:
        return "bad date"
    
    return check_date

def valid_check(input_check_box):
    check_info = functions.get_text(input_check_box)
    if check_info == "":
        return "no check"
    
    return check_info
    


def add_list(root, screen_manager, date):

    def add_new_check(date_text_box, input_check_box ="", repeat = "single"):
        check_date = valid_date(date_text_box, date)
        check_info = valid_check(input_check_box)

        if check_date == "bad date":
            invalid_date_msg = ttk.Label(add_list_frm, text="Please input a valid date of form YYYY-MM-DD")
            invalid_date_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm
            return

        elif check_info == "no check":
            no_check_msg = ttk.Label(add_list_frm, text="No entry, please input a checklist entry")
            no_check_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm
            return
    
        else:
            daylist_update(check_date, repeat, check_info)
            screen_manager.go_back(add_list_frm)




    add_list_frm = ttk.Frame(root, padding=10)
    add_list_frm.pack(fill = "both", expand=True)

    screen_manager.current_frame = add_list_frm 


    #title ish
    add_list_msg = ttk.Label(add_list_frm, text="What would you like to add to the list?")
    add_list_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm

    # shows where to input new check
    input_check = ttk.Label(add_list_frm, text="Input text here:")
    input_check.place(relx=0.4, rely=0.4, anchor=CENTER)

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
                         text="Repeat daily",
                          command= lambda: add_new_check(pick_date, new_check, repeat="daily"))
    daily_repeat.place(relx=0.35, rely= 0.5, anchor=CENTER)

    weekly_repeat = ttk.Button(add_list_frm, 
                         text="Repeat weekly",
                          command= lambda: add_new_check(pick_date, new_check, repeat="weekly"))
    weekly_repeat.place(relx=0.45, rely= 0.5, anchor=CENTER)

    monthly_repeat = ttk.Button(add_list_frm, 
                         text="Repeat monthly",
                          command= lambda: add_new_check(pick_date, new_check, repeat="monthly"))
    monthly_repeat.place(relx=0.55, rely= 0.5, anchor=CENTER)

    yearly_repeat = ttk.Button(add_list_frm, 
                         text="Repeat yearly",
                          command= lambda: add_new_check(pick_date, new_check, repeat="yearly"))
    yearly_repeat.place(relx=0.65, rely= 0.5, anchor=CENTER)


    #button to confirm entry
    add_btn = ttk.Button(add_list_frm, 
                         text="Add check",
                          command= lambda: add_new_check(pick_date, new_check))
    add_btn.place(relx=0.5, rely= 0.6, anchor=CENTER)

    back_btn = ttk.Button(add_list_frm, text="Back", command=lambda: screen_manager.go_back(add_list_frm))
    back_btn.place(relx=0.9, rely=0.9)

