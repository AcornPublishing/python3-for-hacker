
#!/usr/bin/env python3

from tkinter import *

root = Tk()

root.title("My GUI application")
root.geometry("500x100+200+100")

b = Button(root, text = "Click Me!")
b.pack()

root.mainloop()
