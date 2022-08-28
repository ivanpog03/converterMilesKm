from tkinter import *

import action as action

def convert():
    miles=float(inputt.get())
    km=miles*1.609
    labelll.config(text=km)


window= Tk()
window.title("Converter")


inputt=Entry()
inputt.grid(column=1, row=0)

label = Label(text="Miles")
label.grid(column=2, row=0)

labell=Label(text="are equial to ")
labell.grid(column=0, row=1)

labelll=Label()
labelll.grid(column=1, row=1)

labellll=Label(text="km")
labellll.grid(column=2, row=1)

button=Button(text="Click Me", command=convert)
button.grid(column=1, row=2)

window.mainloop()