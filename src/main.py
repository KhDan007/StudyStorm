from tkinter import *

WINDOW_WIDTH = 850
WINDOW_HEIGHT = 600

window = Tk()
window.title("StudyStorm | Login")
window.resizable(False, False)
window.geometry("{}x{}".format(WINDOW_WIDTH, WINDOW_HEIGHT))
window.config(background="#17255A")

frame1 = Frame(window, width=WINDOW_WIDTH-188-188, height=WINDOW_HEIGHT, bg="#18206F",)
frame1.pack(anchor=CENTER, expand=Y, fill="y")



window.mainloop()