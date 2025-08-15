from tkinter import *
from tkinter import ttk
import datetime

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
today = datetime.date.today()
day = days_of_week[today.weekday()]


