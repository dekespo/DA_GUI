import Tkinter as tk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import sys

class GUI():
	
	def __init__(self, dataSet):
		self.root = tk.Tk()
		self.root.title("DA_GUI_py")
		self.dataSet = dataSet


		self.width = self.root.winfo_screenwidth() * 5 / 6
		self.height = self.root.winfo_screenheight() * 5 / 6

		self.root.geometry(str(self.width) + "x" + str(self.height))

		#self.window = tk.Canvas(self.root, width = self.width, height = self.height)
		#self.window.pack()
		#self.w = tk.Canvas(self.root)
		
		self.addFrames()
		#self.w.create_window(100,100, a)
		self.addPlot()
		self.addTextBox()


		self.root.mainloop()
	
	def addFrames(self):
		#tk.Frame.__init__(self, self.root)
		#self.grid()
		#for r in range(6):
		#	self.root.rowconfigure(r, weight = 1)
		#for c in range(2):
		#	self.root.columnconfigure(c, weight = 1)

		#Frame1 = tk.Frame(self.root, bg = "red")
		#Frame1.grid(row = 0, column = 0, rowspan = 5, columnspan = 1, sticky = tk.W + tk.N)

		#Frame2 = tk.Frame(self.root, bg = "blue")	
		#Frame2.grid(row = 0, column = 1, rowspan = 5, columnspan = 1, sticky = tk.E + tk.N)

		#Frame3 = tk.Frame(self.root, bg = "green")	
		#Frame3.grid(row = 5, column = 0, rowspan = 1, columnspan = 2, sticky = tk.W + tk.S + tk.E)
		#Tk.Label(self.root,)

		#Frame1 = tk.Frame(self.root, bg = "red").grid(row = 0, column = 0, rowspan = 5, columnspan = 1, sticky = tk.W + tk.N)

		#Frame2 = tk.Frame(self.root, bg = "blue").grid(row = 0, column = 1, rowspan = 5, columnspan = 1, sticky = tk.E + tk.N)

		#Frame3 = tk.Frame(self.root, bg = "green").grid(row = 5, column = 0, rowspan = 1, columnspan = 2, sticky = tk.W + tk.S + tk.E)
		#a = tk.Frame(self.root, bg = "red", height = self.root.winfo_reqheight(), width = self.root.winfo_reqwidth()).grid(row = 0, column = 0, rowspan = 1, columnspan = 1, sticky = tk.W)
		
		#window = tk.Canvas(self.root)
		#coor1 = 0, 0,  self.width / 2, self.height * 5 / 6
		#self.window.create_rectangle(coor1, fill = "blue")
		#coor2 = self.width / 2, 0, self.width, self.height * 5 / 6
		#self.window.create_rectangle(coor2, fill = "red")
		#coor3 = 0, self.height * 5 / 6#,  self.width , self.height 
		#self.window.create_text(coor3, text = "I AM HERE", width = self.width, anchor = tk.SE)
		#window.pack()
		#a.pack(fill = tk.BOTH, expand = 1)

		self.window = tk.PanedWindow(self.root, showhandle = True, bd = 1)
		self.window.pack(fill = tk.Y, expand = 1)
		div = self.width / 3
		self.left = tk.Label(self.window, text = "LEFT")
		self.center = tk.Label(self.window, text = "MIDDLE")
		self.right = tk.Label(self.window, text = "RIGHT")
		self.window.paneconfig(self.left, minsize = 10, width = div)
		self.window.paneconfig(self.center, minsize = 10, width = div)
		self.window.paneconfig(self.right, minsize = 10, width = div)
		self.window.add(self.left)
		self.window.add(self.center)
		self.window.add(self.right)
		self.window.pack()


	def addTextBox(self):
		t = tk.Text(self.center, height = self.height, width = self.width / 3)
		t.pack()
		#t.insert(tk.END, "deneme")
		t.insert(tk.END, self.dataSet)

	def addStdout(self):
		self.textBox = Text(self.root, wrap = 'word', height = 11, width= 50)
		self.textBox.grid(column = 0, row = 0, columnspan = 2, sticky = 'NSWE', padx = 5, pady = 5)
		sys.stdout = StdoutRedirector(self.textBox)
		
	def readDataset(self):
		print self.dataSet
		print type(self.dataSet)
	
	def addPlot(self):
		f = Figure(figsize = (5,4), dpi = 100)
		a = f.add_subplot(111)
		t = np.arange(0.0, 3.0, 0.01)
		s = np.sin(2 * np.pi * t)
		a.plot(t,s)

		#canvas = FigureCanvasTkAgg(f, master = self.root)
		canvas = FigureCanvasTkAgg(f, master = self.right)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		#toolbar = NavigationToolbar2TkAgg(canvas, self.root)
		toolbar = NavigationToolbar2TkAgg(canvas, self.right)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		def on_key_event(event):
			print "you pressed %s" % event.key
			key_press_handler(event, canvas, toolbar)
		canvas.mpl_connect('key_press_event', on_key_event)
		
