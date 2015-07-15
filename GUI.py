import Tkinter as tk
import tkFont
import plots

class GUI:
	
	def __init__(self, dataSet):
		# Start GUI
		self.root = tk.Tk()
		self.root.title("DA_GUI_py")

		# Get dataset
		self.dataSet = dataSet

		# Initial given size
		self.width = self.root.winfo_screenwidth() * 5 / 6
		self.height = self.root.winfo_screenheight() * 5 / 6
		self.root.geometry(str(self.width) + "x" + str(self.height))

		# Add Window Panes	
		self.addPanes()

		# Add Plot
		self.addPlot()

		# Add Textbox for datasset
		self.addTextBox()
		
		# Keep showing the GUI
		self.root.mainloop() 
	

	def addPanes(self):
		self.window = tk.PanedWindow(self.root, showhandle = True, bd = 1)
		# Gives flexible size arragenment in the window (not event listener is used)
		self.window.pack(fill = tk.BOTH, expand = 1) 

		div = self.width / 3
		self.panes = [] # 0 = Left, 1 = Center, 2 Right
		self.panes.append(tk.Label(self.window, text = "LEFT"))
		self.panes.append(tk.Label(self.window, text = "CENTER"))
		self.panes.append(tk.Label(self.window, text = "RIGHT"))

		for pane in self.panes:
			self.window.paneconfig(pane, minsize = div / 3, width = div)
			self.window.add(pane)

		self.window.pack()


	def addTextBox(self):
		fontType = tkFont.Font(family = "Helvetica", size = 20)
		t = tk.Text(self.panes[1], height = self.height, width = self.width / 3, font = fontType)
		t.insert(tk.END, self.dataSet)
		t.pack()

	def addPlot(self):
		# Put into the right pane
		pane = self.panes[2] 

		plots.plots(self.dataSet, pane)
