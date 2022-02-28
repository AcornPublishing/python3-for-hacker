
#!/usr/bin/env python3

from tkinter import *

root = Tk()

root.title("My GUI application")
root.geometry("500x100+200+100")

def clickMe():
	print("I have just been clicked!")

b = Button(root, text = "Click Me!", command = clickMe)
b.pack()

root.mainloop()
