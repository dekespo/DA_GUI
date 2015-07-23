import Tkinter as tk
import tkFont
import plots
import textbox

class GUI:
	
	def __init__(self, dataset):
		# Start GUI
		self.root = tk.Tk()
		self.root.title("DA_GUI_py")

		# Get dataset
		self.dataset = dataset

		# Initial given size
		self.width = self.root.winfo_screenwidth() * 5 / 6
		self.height = self.root.winfo_screenheight() * 5 / 6
		self.root.geometry(str(self.width) + "x" + str(self.height))

		# Add Window Panes	
		self.addPanes()

		# Add Left Panes	
		self.designLeftPane()

		# Add buttons on Left Panes
		self.addLeftButtons()

		# Add Plot
		self.addPlot()

		# Add Textbox for datasset
		self.addTextBox()
		
		# Keep showing the GUI
		self.root.mainloop() 
	

	def addPanes(self):
		window = tk.PanedWindow(self.root, showhandle = True, bd = 1)
		# Gives flexible size arragenment in the window (not event listener is used)
		window.pack(fill = tk.BOTH, expand = 1) 

		div = self.width / 3
		self.panes = [] # 0 = Left, 1 = Center, 2 Right
		self.panes.append(tk.Label(window, text = "LEFT"))
		self.panes.append(tk.Label(window, text = "CENTER"))
		self.panes.append(tk.Label(window, text = "RIGHT"))

		for pane in self.panes:
			window.paneconfig(pane, minsize = div / 2, width = div)
			window.add(pane)

		window.pack()

	def designLeftPane(self):
		# Divide the left into two subpanes
		window = tk.PanedWindow(self.panes[0], showhandle = True,
								bd = 1, orient = tk.VERTICAL)
		# Gives flexible size arragenment in the window (not event listener is used)
		window.pack(fill = tk.BOTH, expand = 1) 
		self.subpanes = []
		self.subpanes.append(tk.Label(window, text = "UP"))
		self.subpanes.append(tk.Label(window, text = "DOWN"))
		
		div = self.height / 3
		for pane in self.subpanes:
			window.paneconfig(pane, minsize = div / 3, height = div)
			window.add(pane)

		window.pack()

	def addLeftButtons(self):
		# Add button to the left up pane
		v = tk.StringVar()
		v.set("deneme")
		e = tk.Entry(self.subpanes[0], textvariable = v)
		e.pack()

		def callback():
			print e.get()

		b = tk.Button(self.subpanes[0], text = "JUST DO IT",  command = lambda: callback())
		b.pack()



	def addTextBox(self):
		# Put into the middle pane
		pane = self.panes[1] 
		size = [self.height, self.width]

		textbox.textbox(self.dataset, pane, size)


	def addPlot(self):
		# Put into the right pane
		pane = self.panes[2] 

		plots.plots(self.dataset, pane)
