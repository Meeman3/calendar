from tkinter import *
from tkinter import ttk
import functions
from tkinter import scrolledtext 


#   if notes_dict.py doesnt exist make a temp dict
try:
    from dictionaries.notes_dict import notes_dict
except ImportError:
    notes_dict = {}


#   function that boots the add_notes screen
def add_notes(root, screen_manager):

    #    function that adds inputted notes and titles to notes_dict
    def get_new_note(title_text_box, note_text_box):

        #   gets title, entry and time of a note
        note_title = functions.get_text(title_text_box)
        note_text = functions.get_text(note_text_box)
        time = str(functions.today_time)

        #   makes dict out of above values
        note_with_time = {note_text: time}
        note_dict = {note_title: note_with_time}

        #   updates dict
        with open("dictionaries/notes_dict.py", "w") as nd:
            notes_dict.update(note_dict)
            nd.write(f"notes_dict = {notes_dict}")

    #    function for add_note btn, uses get_new_note then returns to regular notes page
    def add_new_note(title_text_box, note_text_box):
        get_new_note(title_text_box, note_text_box)
        screen_manager.go_back(add_notes_frm)


    #   makes frame for add_notes_screen
    add_notes_frm = ttk.Frame(root, padding=10)
    add_notes_frm.pack(fill = "both", expand=True)

    #   keeps track of current frame, used for home button feature
    screen_manager.current_frame = add_notes_frm

        
    add_notes_msg = ttk.Label(add_notes_frm, text="What note would you like to add?")
    add_notes_msg.place(relx=0.5, rely=0.25, anchor=CENTER) #centres in frm


    #   shows where to input note
    input_msg = ttk.Label(add_notes_frm, text="Input text here:")
    input_msg.place(relx=0.4, rely=0.35, anchor=CENTER)

    #   new note input
    new_note = scrolledtext.ScrolledText(add_notes_frm, width= 100, height = 20)
    new_note.place(relx=0.7, rely=0.5, anchor=CENTER)
    

    #   shows where to put title
    title_msg = ttk.Label(add_notes_frm, 
                         text="Title")
    title_msg.place(relx=0.4, rely= 0.3, anchor=CENTER)

    #   title input
    pick_title = ttk.Entry(add_notes_frm, width= 100)
    pick_title.place(relx=0.71, rely=0.3, anchor=CENTER)



    #   confirms note add
    add_btn = ttk.Button(add_notes_frm, 
                         text="Add note",
                          command=lambda : add_new_note(pick_title, new_note))
    add_btn.place(relx=0.5, rely= 0.7, anchor=CENTER)



    #   takes to previous page in history
    back_btn = ttk.Button(add_notes_frm, text="Back", command=lambda: screen_manager.go_back(add_notes_frm))
    back_btn.place(relx=0.9, rely=0.9)

