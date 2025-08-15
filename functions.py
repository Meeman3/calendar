from tkinter import *
from tkinter import ttk
import datetime


today = datetime.date.today()

def day(date):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    return days_of_week[date.weekday()]


