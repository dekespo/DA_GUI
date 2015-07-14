import Tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import sys

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

		self.root.mainloop() # Keep showing the GUI
	
	def addPanes(self):

		self.window = tk.PanedWindow(self.root, showhandle = True, bd = 1)
		self.window.pack(fill = tk.BOTH, expand = 1) # Gives felxible size 
													 # arragenment in
													 # the window (not
													 # event listener
													 # is used)

		div = self.width / 3
		self.panes = [] # 0 = Left, 1 = center, 2 right
		self.panes.append(tk.Label(self.window, text = "LEFT"))
		self.panes.append(tk.Label(self.window, text = "CENTER"))
		self.panes.append(tk.Label(self.window, text = "RIGHT"))

		for pane in self.panes:
			self.window.paneconfig(pane, minsize = div / 3, width = div)
			self.window.add(pane)

		self.window.pack()


	def addTextBox(self):
		t = tk.Text(self.panes[1], height = self.height, width = self.width / 3)
		t.insert(tk.END, self.dataSet)
		t.pack()

	def addPlot(self):
		fig = Figure(figsize = None, dpi = None) # Do not use plt
										         #instead of Figure,
												 #it creates some
												 #problem whwn the GUI
												 #is being close
		a = fig.add_subplot(111)
		x = "Volume"
		y = "Open"
		#t = self.dataSet["Date"]
		t = self.dataSet[x]
		s = self.dataSet[y]
		a.scatter(t,s)
		a.set_xlabel(x); a.set_ylabel(y); a.set_title(y + " vs " + x)

		pane = self.panes[2] # the right pane

		canvas = FigureCanvasTkAgg(fig, master = pane)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		toolbar = NavigationToolbar2TkAgg(canvas, pane)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

