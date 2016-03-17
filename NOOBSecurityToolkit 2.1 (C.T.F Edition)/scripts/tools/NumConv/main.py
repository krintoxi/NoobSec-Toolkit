# Binary, Hexadecimal and Denary Converter

# Import Statements
import conversion
from tkinter import *
from tkinter import ttk
from tkinter import font

# Functions
def toDenary():
	num = numberEntry.get()
	base = baseEntry.get()
	numReturned = str(conversion.toDenary(num, base))
	answerLabel.config(text=numReturned)

def fromDenary():
	num = numberEntry.get()
	base = baseEntry.get()
	numReturned = str(conversion.fromDenary(num, base))
	answerLabel.config(text=numReturned)

# Root Setup
root = Tk()
root.title("Number Converter")

# Fonts
s = ttk.Style()
s.configure('.', font=('Helvetica', 18))
s.configure("Title.TLabel", font=" Helvetica 20 bold", anchor=CENTER)
s.configure("TButton", width=18, height=2)
s.configure("Answer.TLabel", anchor=CENTER)

# Frame
frame = ttk.Frame(root, padding=(6,6,24,24))
frame.grid()

# Title Label
title = ttk.Label(frame, text="Denary, Hexadecimal and Binary Converter", style="Title.TLabel")
title.grid(row=0, column=0, columnspan=2)

# Labels
ttk.Label(frame, text="Number to convert:").grid(row=1, column=0, sticky=W)
ttk.Label(frame, text="Base to convert to/from:").grid(row=3, column=0, sticky=W)
ttk.Label(frame, text="Answer:", style="Answer.TLabel").grid(row=5, column=0,columnspan=2)
answerLabel = ttk.Label(frame, text="", style="Answer.TLabel")
answerLabel.grid(row=6, column=0, columnspan=2)

# Text Entries
numberEntry = ttk.Entry(frame)
numberEntry.grid(row=2, column=0, sticky=W)

baseEntry = ttk.Entry(frame)
baseEntry.grid(row=4, column=0, sticky=W)

# Buttons
ttk.Button(frame, text="Convert to Denary", command=toDenary).grid(row=2, column=1, sticky=E)
ttk.Button(frame, text="Convert from Denary", command=fromDenary).grid(row=4, column=1, sticky=E)

# Mainloop
root.mainloop()