from tkinter import *

root = Tk()

def Change1():
    butt1.set("Auto - Slow")
    buttontwo.place(x=100, y=0)

def Dischange1():
    butt1.set("S")
    buttontwo.place(x=35, y=0)

def OnHoverOne(button):
    button.bind("<Enter>", func=lambda e: Change1())
    button.bind("<Leave>", func=lambda e: Dischange1())


butt1 = StringVar()
butt1.set("S")
buttonone = Button(root, textvariable=butt1, bg="dark green", fg="white")
buttonone.place(x=0, y=0)
OnHoverOne(buttonone)

butt2 = StringVar()
butt2.set("F")
buttontwo = Button(root, textvariable=butt2, bg="dark orange", fg="white")
buttontwo.place(x=35, y=0)


root.mainloop()