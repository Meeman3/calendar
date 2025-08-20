from tkinter import *
import datetime
from dateutil.relativedelta import relativedelta

    #   date today
today = datetime.date.today()

    #   todays date AND time
today_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    #   function that gets current day of week
def day(date):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days_of_week[date.weekday()]


    #   functions that related date based on input date
def tomorrow(today):
    return today + datetime.timedelta(days=1)

def yesterday(today):
    return today - datetime.timedelta(days=1)

def next_week(date):
    return date + datetime.timedelta(weeks=1)

def next_month(date):
    return date + relativedelta(months=1)

def next_year(date):
    return date + relativedelta(years=1)


    #   function that gets text from text boxes, Entry or Text
def get_text(text_box):
    if isinstance(text_box, Entry):
        input_text = text_box.get()
    
    elif isinstance(text_box, Text):
        input_text = text_box.get("1.0", END)

    return input_text

    #   functionn that checks if date is valid
def date_checker(input):
    try:
        datetime.datetime.strptime(input, "%Y-%m-%d")
        return True
    except ValueError:
        return False




