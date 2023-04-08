# Import libraries
from tkinter import *

# Set constants
WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600
FRAME_WIDTH = WINDOW_WIDTH-188-188

# Functions
def clear_entry(event, entry):
    entry.delete(0,END)
    entry.config(fg="#ffffff")

# Initialize the window
window = Tk()
window.title("StudyStorm | Login")
window.resizable(False, False)
window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
window.config(background="#17255A")

# Create frame
frame1 = Frame(window, width=FRAME_WIDTH, height=WINDOW_HEIGHT, bg="#18206F")
frame1.place(x=188, y=0)

# Create logo label
try:
    logo_photo = PhotoImage(file="./img/StudyStorm.png")
except TclError:
    print("File not found!")
else:
    logo_label = Label(frame1, text="", image=logo_photo,
                       bg="#17255A", width=163, height=44, compound=CENTER)
    logo_label.place(x=156, y=72)

# Create login label
login_label = Label(frame1, text="Login:", font=('Lato', 25), fg="#ffffff", bg="#18206F")
login_label.place(x=195, y=139)

# Create form frame
form_frame = Frame(frame1, width=335, height=83, bg="#18206F")
form_frame.place(x=50, y=220)

email_label = Label(form_frame, text="Email:", font=("Lato", 16), bg="#18206F", fg="#FFFFFF")
email_label.grid(row=0, column=0, sticky='w')

form_spacer1 = Label(form_frame, height=1, bg="#18206F")
form_spacer1.grid(row=1, column=0)

password_label = Label(form_frame, text="Password:", font=("Lato", 16), bg="#18206F", fg="#FFFFFF")
password_label.grid(row=2, column=0, sticky='w')

form_spacer2 = Label(form_frame, width=3, bg="#18206F")
form_spacer2.grid(row=0, column=1, rowspan=2)

email_entry = Entry(form_frame, fg="#656565", font=("Lato", 16), bg="#17255A")
email_entry.grid(row=0, column=2)
email_entry.insert(0, "example@test.com")
email_entry.bind("<FocusIn>", lambda event: clear_entry(event, email_entry))

password_entry = Entry(form_frame, fg="#656565", font=("Lato", 16), bg="#17255A")
password_entry.grid(row=2, column=2)
password_entry.insert(0, "e.g. 123456")
password_entry.bind("<FocusIn>", lambda event: clear_entry(event, password_entry))


# Main loop
window.mainloop()
