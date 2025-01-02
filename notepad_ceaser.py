from tkinter.filedialog import *
import tkinter as tk
import math

# File functions
def saveFile():
    new_file = asksaveasfile(mode='w', defaultextension='.txt', filetypes=[('Text files', '*.txt')])
    if new_file is None:
        return
    text = str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()

def openFile():
    file = askopenfile(mode='r', filetype=[('Text files', '*.txt')])
    if file is not None:
        content = file.read()
        entry.insert(tk.INSERT, content)
    else:
        content = ""

def clearFile():
    entry.delete(1.0, tk.END)

def encryption():
    shift = 3  # Set value 1-26 (same as decryption)
    text = entry.get(1.0, tk.END)
    result = []
    for char in text:
        if char.isalpha():
            if char.islower():
                result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
            else:
                result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    entry.delete(1.0, tk.END)
    entry.insert(tk.INSERT, ''.join(result))

def decryption():
    shift = 3  #Set value 1-26 (same as encryption)
    text = entry.get(1.0, tk.END)
    result = []
    for char in text:
        if char.isalpha():
            if char.islower():
                result.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
            else:
                result.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
        else:
            result.append(char)
    entry.delete(1.0, tk.END)
    entry.insert(tk.INSERT, ''.join(result))

# Background and title
canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="light blue")

# Create frame for buttons
top = tk.Frame(canvas)
top.pack(padx=10, pady=5, anchor='nw')

# Buttons
b1 = tk.Button(canvas, text="Open", bg="white", command=openFile)
b1.pack(in_=top, side="left")

b2 = tk.Button(canvas, text="Save", bg="white", command=saveFile)
b2.pack(in_=top, side="left")

b3 = tk.Button(canvas, text="Clear", bg="white", command=clearFile)
b3.pack(in_=top, side="left")

b4 = tk.Button(canvas, text="Exit", bg="white", command=exit)
b4.pack(in_=top, side="left")

b5 = tk.Button(canvas, text="Encrypt", bg="white", command=encryption)
b5.pack(in_=top, side="left")

b6 = tk.Button(canvas, text="Decrypt", bg="white", command=decryption)
b6.pack(in_=top, side="left")

# Create entry
entry = tk.Text(canvas, wrap=tk.WORD, bg="#F9DDA4", font=("Arial Baltic", 15))
entry.pack(padx=10, pady=5, expand=True, fill="both")

canvas.mainloop()
