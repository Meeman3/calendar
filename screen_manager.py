from screens.checklist_screen import to_daylist
from screens.start_screen import start_screen
from screens.notes_screen import to_notes

class Screen_Manager:
    def __init__(self, root):
        self.root = root
        self.current_frame = None
        self.screen_hist = ["start"]

        #changes screen from one to another, adds former screen to history if not using back func
    def change_screen(self, screen_name, current_frame=None, back=False):
        if current_frame:
            if not back:
                self.screen_hist.append(screen_name)
            current_frame.pack_forget()

        
        if screen_name == "start":
            start_screen(self.root, self)
        if screen_name == "notes":
            to_notes(self.root, self)
        if screen_name == "checklist":
            to_daylist(self.root, self)
    
        #goes back to previous screen and removes current from history
    def go_back(self, current_frame):

        self.screen_hist.pop()
        prev_screen = self.screen_hist[-1]

        self.change_screen(prev_screen, current_frame, back=True)


        

    