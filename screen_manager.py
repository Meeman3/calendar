from screens.checklist_screen import to_daylist
from screens.start_screen import start_screen
from screens.notes_screen import to_notes
from screens.add_to_checklist import add_list
from screens.add_notes_screen import add_notes
from screens.read_notes_screen import read_notes
from dictionaries.notes_dict import notes_dict
import functions

class Screen_Manager:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.screen_hist = [["start", functions.today]]

        #changes screen from one to another, adds former screen to history if not using back func
    def change_screen(self, screen_name, current_frame=None, back=False, date=functions.today, title ="", edit_mode = False):
        if current_frame:
            if not back:
                self.screen_hist.append([screen_name, date])
            current_frame.pack_forget()

        
        if screen_name == "start":
            start_screen(self.root, self)
        if screen_name == "notes":
            to_notes(self.root, self)
        if screen_name == "checklist":
            to_daylist(self.root, self, date, edit_mode)
        if screen_name == "add_list":
            add_list(self.root, self)
        if screen_name == "add_notes":
            add_notes(self.root, self)
        if screen_name == "read_notes":
            read_notes(self.root, self, title)

    
        #goes back to previous screen and removes current from history
    def go_back(self, current_frame):
        if self.screen_hist[-2][0] == "read_notes":
            self.screen_hist.pop()

        self.screen_hist.pop()
        prev_screen = self.screen_hist[-1][0]
        prev_date = self.screen_hist[-1][1]

        self.change_screen(prev_screen, current_frame, back=True, date= prev_date)

    def home_cmd(self):
        self.change_screen("start", self.current_frame)

        


        

    