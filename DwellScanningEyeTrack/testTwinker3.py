
import tkinter as tk
from tkinter import ttk,Button
from tkinter import *

root = Tk()
root.title("Medicine database")
def add():
    data = tree.insert("",END,values=("",e1.get()))
    sort()

def sort():
    rows = [(tree.set(item, 'two').lower(), item) for item in tree.get_children('')]
    rows.sort()

    for index, (values, item) in enumerate(rows):
        tree.move(item, '', index)

e1=Entry(root,width=15)
e1.grid(row=0,column=1,padx=10,pady=10,sticky=E,rowspan=1)

btn1 = Button(root,text="add",width=10,command=add)
btn1.grid(row =1,column=0,padx=10,pady=10,rowspan=2)


#treeview
tree = ttk.Treeview(root,height=25)
tree["columns"]=("one","two","three","four")
tree.column("one",width=120)
tree.column("two",width=160)
tree.column("three",width=130)
tree.column("four",width=160)
tree.heading("one", text="Numer seryjny leku")
tree.heading("two", text="Nazwa Leku")
tree.heading("three", text="Ampułki/Tabletki")
tree.heading("four",text="Data ważności")
tree["show"]="headings"
tree.grid(row=0,column=2,rowspan=6,pady=20)

root.geometry("840x580")
root.mainloop()