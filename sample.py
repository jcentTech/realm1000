from cProfile import label
from cgitb import text
import tkinter as tk
from tkinter import *
import psutil
import os
p = psutil.Process()

root = tk.Tk()
def myClick():
    myLabel = Label(root, text="CPU Core: " + str(psutil.cpu_count())).pack()

#Creating Label widget



myButton = Button(root, text="Click Me!", bg='blue', fg="white", command=myClick)
myButton.pack()

















root.mainloop()