from tkinter.filedialog import *
import tkinter as tk

#file functions

def saveFile():
    new_file= asksaveasfile(mode= 'w', defaultextension='.txt', filetypes=[('Text files', '*.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode= 'r', filetype= [('text files','*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(tk.INSERT, content)
    else:
        content = ""

def clearFile():
    entry.delete(1.0, tk.END)

#background and title

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "light blue")
#create frame for buttons
top = tk.Frame(canvas)
top.pack(padx = 10, pady = 5, anchor= 'nw')

#buttons

b1 = tk.Button(canvas, text="Open", bg="white", command = openFile)
b1.pack(in_ = top, side="left")

b2 = tk.Button(canvas, text="Save", bg="white", command = saveFile)
b2.pack(in_ = top, side="left")

b3 = tk.Button(canvas, text="Clear", bg="white", command = clearFile)
b3.pack(in_ = top, side="left")

b4 = tk.Button(canvas, text="Exit", bg="white", command = exit)
b4.pack(in_ = top, side="left")

#create entry

entry = tk.Text(canvas,wrap = tk.WORD, bg= "#F9DDA4", font = ("Arial Baltic",15))
entry.pack(padx = 10, pady=5, expand= True, fill = "both")

canvas.mainloop()