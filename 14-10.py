
#!/usr/bin/env python3

from tkinter import *

root = Tk()
root.title("My GUI application")
root.geometry("500x200+400+200")

label = Label(root, text="Type your name!")
label.pack()

entry = Entry(root)
entry.pack()

def saveName():
	file = open("name.txt",  "a")
	file.write("%s\n" % entry.get())
	entry.delete(0, END)

button = Button(root, text="Save", command = saveName)
button.pack()

root.mainloop()
