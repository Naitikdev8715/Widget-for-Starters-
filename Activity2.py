from tkinter import *
from datetime import date

window = Tk()
window.title("Getting Started with widgets")
window.geometry("400x300")

label1 = Label(text = "Hey There!", fg = "white", bg = "black", height = 1, width = 300)
label2 = Label(text = "Full name:", bg = "black")

name_entry = Entry()

text_box = Text(height = 3)

def display():
    name = name_entry.get()
    global message
    message = "Welcome To the Application \n Today's date is "
    greet = "Hello! " + name + "\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

button1 = Button(text = "Click Me!", command=display, height = 1, bg = "black", fg = "white")

label1.pack()
label2.pack()
name_entry.pack()
text_box.pack()
button1.pack()

window.mainloop()