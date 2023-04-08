from tkinter import *
from PIL import Image, ImageTk, ImageDraw

WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600
FRAME_WIDTH = WINDOW_WIDTH-188-188

window = Tk()
window.title("StudyStorm | Login")
window.resizable(False, False)
window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
window.config(background="#17255A")

frame1 = Frame(window, width=FRAME_WIDTH, height=WINDOW_HEIGHT, bg="#18206F")
frame1.place(x=188, y=0)

try:
    logo_photo = PhotoImage(file="./img/StudyStorm.png")
except TclError:
    print("File not found!")
else:
    logo_label = Label(frame1, text="", image=logo_photo,
                       bg="#17255A", width=163, height=44, compound=CENTER)
    logo_label.place(x=156, y=72)


window.mainloop()
