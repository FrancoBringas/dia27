from tkinter import *

window = Tk()
window.title("my first gui program")
window.minsize(width=500, height=300)

my_label = Label(text="y am a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print(" y got clicked")
    button.config(text=input.get())


button = Button(text="click Me",command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()

window.mainloop()
