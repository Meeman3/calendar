from tkinter import *
from tkinter import ttk
import datetime
from dateutil.relativedelta import relativedelta


today = datetime.date.today()
today_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#function that gets current day of week
def day(date):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days_of_week[date.weekday()]


#function that gets day after inputted date
def tomorrow(today):
    return today + datetime.timedelta(days=1)

#funcion that gets day before input date
def yesterday(today):
    return today - datetime.timedelta(days=1)

def next_week(date):
    return date + datetime.timedelta(weeks=1)

def next_month(date):
    return date + relativedelta(months=1)

def next_year(date):
    return date + relativedelta(years=1)


#get text from text box
def get_text(text_box):
    if isinstance(text_box, Entry):
        input_text = text_box.get()
    
    elif isinstance(text_box, Text):
        input_text = text_box.get("1.0", END)

    return input_text

#check if date is valid
def date_checker(input):
    try:
        datetime.datetime.strptime(input, "%Y-%m-%d")
        return True
    except ValueError:
        return False




