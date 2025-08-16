from tkinter import *
from tkinter import ttk
import functions
from dictionaries.notes_dict import notes_dict
from tkinter import scrolledtext 

def read_notes(root, screen_manager, title):

    #getting value from note_dict
    note_dict = notes_dict[title].keys()
    note_words = list(note_dict)[0]

    read_notes_frm = ttk.Frame(root, padding=10)
    read_notes_frm.pack(fill = "both", expand=True)

    note_time = notes_dict[title][note_words]
    read_notes_msg = ttk.Label(read_notes_frm, text=f"Note made at {note_time}")
    read_notes_msg.place(relx=0.5, rely=0.1, anchor=CENTER) #centres in frm



    #title input
    note_title = ttk.Entry(read_notes_frm, width= 100)
    note_title.place(relx=0.5, rely=0.3, anchor=CENTER)
    note_title.delete("0", END)
    note_title.insert("0", title)
    note_title.configure(state="readonly")

    


    #new note input
    note_contents = scrolledtext.ScrolledText(read_notes_frm, width= 100, height = 20)
    note_contents.place(relx=0.5, rely=0.5, anchor=CENTER)
    note_contents.delete("1.0", END)
    note_contents.insert("1.0", note_words)
    note_contents.configure(state="disabled")

    

    #edit button
    edit_btn = ttk.Button(read_notes_frm, 
                         text="Edit note",
                          command = lambda: replacement_mode())
    edit_btn.place(relx=0.5, rely= 0.7, anchor=CENTER)




    back_btn = ttk.Button(read_notes_frm, text="Back", command=lambda: screen_manager.go_back(read_notes_frm))
    back_btn.place(relx=0.9, rely=0.9)

    undo_btn = ttk.Button(read_notes_frm, 
                         text="Undo changes?",
                          command=lambda: undo())

    confirm_btn = ttk.Button(read_notes_frm, 
                         text="confirm changes?",
                          command=lambda: replace_note(note_title, note_contents))
    
    delete_btn = ttk.Button(read_notes_frm, 
                         text="delete note?",
                          command=lambda: delete_note())

    def replacement_mode():
        edit_btn.place_forget()
        note_title.configure(state="enabled")
        note_contents.configure(state="normal")


        undo_btn.place(relx=0.9, rely= 0.5, anchor=CENTER)
        confirm_btn.place(relx=0.5, rely= 0.7, anchor=CENTER)
        delete_btn.place(relx=0.9, rely= 0.6, anchor=CENTER)

    def undo():
        undo_btn.place_forget()
        confirm_btn.place_forget()
        edit_btn.place(relx=0.5, rely= 0.7, anchor=CENTER)
        note_title.configure(state="readonly")
        note_contents.configure(state="disabled")

    def delete_note():
        with open("dictionaries/notes_dict.py", "w") as nd:
            new_notes_dict = notes_dict
            del new_notes_dict[title]
            nd.write(f"notes_dict = {notes_dict}")

        screen_manager.go_back(read_notes_frm)


    def replace_note(title_text_box, note_text_box):
        note_title = functions.get_text(title_text_box)
        note_text = functions.get_text(note_text_box)
        time = functions.today_time
        note_with_time = {note_text: time}
        note_dict = {note_title: note_with_time}
        with open("dictionaries/notes_dict.py", "w") as nd:
            new_notes_dict = notes_dict
            del new_notes_dict[title]
            new_notes_dict.update(note_dict)
            nd.write(f"notes_dict = {notes_dict}")

        undo()



