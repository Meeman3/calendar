from tkinter import *
from tkinter import ttk
import functions 
from dictionaries.checklist_dict import daylist_dict


def add_list(root, screen_manager):

    def get_new_check(date_text_box, input_check_box, repeat = "single"):
        if functions.get_text(date_text_box) != "":
            check_date = functions.get_text(date_text_box)
        else:
            check_date = str(functions.today)
        

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

        check_info = functions.get_text(input_check_box)

        if check_info == "":
            return "no check"
        
        check_bool = False
        check_info_dict = {check_info: check_bool}
        check_repeat_dict = {repeat: check_info_dict}
        check_full_dict = {check_date: check_repeat_dict} 
        with open("dictionaries/checklist_dict.py", "w") as dl:
            daylist_dict.update(check_full_dict)
            dl.write(f"daylist_dict= {daylist_dict}")

    def add_new_check(date_text_box, input_check_box ="", repeat = "single"):
        get_new_check(date_text_box, input_check_box, repeat)

        if get_new_check(date_text_box, input_check_box, repeat) == "bad date":
            invalid_date_msg = ttk.Label(add_list_frm, text="Please input a valid date of form YYYY-MM-DD")
            invalid_date_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm
            return

        elif get_new_check(date_text_box, input_check_box, repeat) == "no check":
            no_check_msg = ttk.Label(add_list_frm, text="No entry, please input a checklist entry")
            no_check_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm
            return
    
        else:
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
                         text="Add check",
                          command= lambda: add_new_check(pick_date, new_check))
    add_btn.place(relx=0.5, rely= 0.6, anchor=CENTER)

    back_btn = ttk.Button(add_list_frm, text="Back", command=lambda: screen_manager.go_back(add_list_frm))
    back_btn.place(relx=0.9, rely=0.9)

