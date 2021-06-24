import tkinter as tk
import pandas as pd

# --- functions ---

def showdata():
    global table

    # destroy old frame with table
    if table:
        table.destroy()

    # create new frame with table
    table = tk.Frame(frame_data)
    table.grid(row=0, column=0)

    # fill frame with table
    row, column = df2.shape
    for r in range(row):
        for c in range(column):
            e1 = tk.Entry(table)
            e1.insert(1, df2.iloc[r, c])
            e1.grid(row=r, column=c, padx=2, pady=2)
            e1.config(state='disabled')

def on_click():
    global df2

    val = selected.get()

    if val == 'all':
        df2 = df
        #next_button.grid_forget()
    else:
        df2 = df[ df['TIME'] == val ]
        #next_button.grid(row=1, column=0)

    print(df2)
    showdata()
    next_button.grid(row=1, column=0)

def on_select(val):
    global df2

    if val == 'all':
        df2 = df
        #next_button.grid_forget()
    else:
        df2 = df[ df['TIME'] == val ]
        #next_button.grid(row=1, column=0)

    print(df2)
    showdata()
    next_button.grid(row=1, column=0)

# --- main ---

frame_data = None

df = pd.DataFrame({
    'TIME': ['00:00','00:00','01:00','01:00','02:00','02:00'],
    'A': ['a','b','c','d','e','f'],
    'B': ['x','x','y','y','z','z'],
})

root = tk.Tk()

values = ['all'] + list(df['TIME'].unique())
selected = tk.StringVar()

options = tk.OptionMenu(root, selected, *values, command=on_select)
options.pack()

button = tk.Button(root, text='OK', command=on_click)
button.pack()

# frame for table and button "Next Data"
frame_data = tk.Frame(root)
frame_data.pack()

exit_button = tk.Button(root, text="EXIT", command=root.destroy)
exit_button.pack()

# table with data - inside "frame_data" - without showing it
table = tk.Frame(frame_data)
#table.grid(row=0, column=0)

# buttom "Next Data" - inside "frame_data" - without showing it
next_button = tk.Button(frame_data, text="Next Data", command=showdata)
#next_button.grid(row=1, column=0)

root.mainloop()