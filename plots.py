import Tkinter as tk
import matplotlib
#matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
#from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from datetime import datetime


def plots(dataSet, window):

		years = mdates.YearLocator()
		months = mdates.MonthLocator()
		yearsFmt = mdates.DateFormatter('%Y-%m')

		fig, ax = plt.subplots()

		time = dataSet.index.to_pydatetime()
		t = "Time"
		x = "Volume"
		y = "Open"
		print list(dataSet.columns.values)
		xValues = dataSet[x]
		#yValues = dataSet[y]
		#ax.scatter(xValues, yValues)
		ax.scatter(time, xValues)

		ax.xaxis.set_major_locator(years)
		ax.xaxis.set_major_formatter(yearsFmt)
		ax.xaxis.set_minor_locator(months)
		ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
		plt.setp(plt.xticks()[1], rotation = 60)
		ax.grid(True)
		ax.set_xlabel(t); ax.set_ylabel(x); ax.set_title(t + " vs " + x)

		# Add the graphic
		canvas = FigureCanvasTkAgg(fig, master = window)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		# Add the (interactive) toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, window)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
