import tkinter as tk
from tkinter import dnd

import tkinterDnD
import ttkwidgets


def drop(event):
    print("DROP EVENT:", event)


root = tkinterDnD.Tk()
root.register_drop_target("*")
root.bind("<<Drop>>", drop)
root.mainloop()

