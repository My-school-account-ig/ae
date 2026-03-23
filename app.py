from tkinter import*
import tkinter as tk

root = Tk()

class GUI(Canvas):
    '''inherits Canvas class (all Canvas methodes, attributes will be accessible)
       You can add your customized methods here.
    '''
    def __init__(self,master,*args,**kwargs):
        Canvas.__init__(self, master=master, *args, **kwargs)

tk.Label(root, text="test").pack()
root.configure(background="black")

polygon = GUI(root)
polygon.create_polygon([0, 0, 100, 0, 100, 100, 0, 100], outline="Yellow", width=2)
polygon.pack()
root.mainloop()
