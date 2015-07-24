import Tkinter as tk
import tkFont
import plots
import textbox
import download_data

class GUI:
	
	#def __init__(self, dataset, downloadContent):
	def __init__(self, downloadContent):

		# Copy content
		self.downloadContent = downloadContent

		# Start GUI
		self.root = tk.Tk()
		self.root.title("DA_GUI_py")

		# Get dataset
		#self.dataset = dataset
		self.dataset = download_data.get(downloadContent)

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

		stringvars = []
		entries = []
		i = 0
		for key, item in self.downloadContent.items():
			# Add a button to the left up pane
			var = tk.StringVar()
			var.set(item)
			stringvars.append(var)
			label = tk.StringVar()
			label.set(key)
			labelbox = tk.Label(self.subpanes[0], textvariable = label)
			labelbox.grid(row = i, column = 0)
			entry = tk.Entry(self.subpanes[0], textvariable = var)
			entry.grid(row = i, column = 1)
			entries.append(entry)
			i += 1

		def download():
			for i, key in enumerate(self.downloadContent.keys()):
				self.downloadContent[key] = entries[i].get()
				self.dataset = download_data.get(self.downloadContent)
				self.addPlot()
			print self.downloadContent

		b = tk.Button(self.subpanes[0], text = "DOWNLOAD DATA", command = lambda: download())
		b.grid(row = i, column = 0, columnspan = 2)



	def addTextBox(self):
		# Put into the middle pane
		pane = self.panes[1] 
		size = [self.height, self.width]

		textbox.textbox(self.dataset, pane, size)


	def addPlot(self):
		# Put into the right pane
		pane = self.panes[2] 

		plots.plots(self.dataset, pane)
