from tkinter import *
from tkinter import ttk
import datetime


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


#get text from text box
def get_text(text_box):
    if isinstance(text_box, Entry):
        input_text = text_box.get()
    
    elif isinstance(text_box, Text):
        input_text = text_box.get("1.0", END)

    return input_text



