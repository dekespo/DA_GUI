import Tkinter as tk
import tkFont

def textbox(dataset, window, size):

		# Set font type
		fontType = tkFont.Font(family = "Helvetica", size = 12)

		# Set the size
		t = tk.Text(window, height = size[0], width = size[1] / 3, font = fontType)

		# Write the text and insert it
		strList = [str(var) + "\n" for var in list(dataset.columns.values)]
		names = ""
		for s in strList: names += s + " "
		t.insert(tk.END, "The variables are:\n ")
		t.insert(tk.END, names)
		t.insert(tk.END, "-----------------------")
		t.pack()
