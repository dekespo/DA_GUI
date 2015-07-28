import Tkinter as tk
import matplotlib
#matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def create(dataset, window):

		# Create a figure
		fig = plt.figure()
		ax = fig.gca()

		# Arrange data to use in the figure
		time = dataset.index.to_pydatetime()
		t = "Time"
		x = "Volume"
		y = "Open"
		xValues = dataset[x]
		#yValues = dataset[y]
		#ax.scatter(xValues, yValues)
		ax.scatter(time, xValues)

		# Automatically choose the best dates
		xtick_locator = mdates.AutoDateLocator()
		xtick_formatter = mdates.AutoDateFormatter(xtick_locator)
		ax.xaxis.set_major_locator(xtick_locator)
		ax.xaxis.set_major_formatter(xtick_formatter)
		# Rotate the x ticks
		plt.setp(plt.xticks()[1], rotation = 60)

		# Add grids and the labels
		ax.grid(True)
		ax.set_xlabel(t); ax.set_ylabel(x); ax.set_title(x + " vs " + t)

		# Add the graphic
		canvas = FigureCanvasTkAgg(fig, master = window)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		# Add the (interactive) toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, window)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		return [fig, ax, canvas]

def update(dataset, window, graph):

		fig, ax, canvas = [each for each in graph]
		print "UPDATING NOW"
		print "dataset is now = ", dataset
		# Close the current figure
		#plt.close()
		#global fig
		#fig = graph[0]
		fig.clf()
		ax.clear()
		#graph[0].clf()
		#fig.clf()
		#canvas.clear()

		# Create a figure
		#fig = plt.figure()
		#ax = fig.gca()

		# Arrange data to use in the figure
		time = dataset.index.to_pydatetime()
		t = "Time"
		x = "Volume"
		y = "Open"
		xValues = dataset[x]
		#yValues = dataset[y]
		#ax.scatter(xValues, yValues)
		ax.scatter(time, xValues)

		# Automatically choose the best dates
		xtick_locator = mdates.AutoDateLocator()
		xtick_formatter = mdates.AutoDateFormatter(xtick_locator)
		ax.xaxis.set_major_locator(xtick_locator)
		ax.xaxis.set_major_formatter(xtick_formatter)
		# Rotate the x ticks
		#plt.setp(plt.xticks()[1], rotation = 60)

		## Add grids and the labels
		#ax.grid(True)
		#ax.set_xlabel(t); ax.set_ylabel(x); ax.set_title(x + " vs " + t)

		# Add the graphic
		#canvas = FigureCanvasTkAgg(fig, master = window)
		#canvas.show()
		#canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
		canvas.draw()

		# Add the (interactive) toolbar
		#toolbar = NavigationToolbar2TkAgg(canvas, window)
		#toolbar.update()
		#canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		return [fig, ax, canvas]
		#return fig
	
