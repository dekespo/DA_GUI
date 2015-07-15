import Tkinter as tk
import matplotlib
#matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import pandas as pd
from datetime import datetime


def plots(dataSet, window):
		# Do not use plt instead of Figure, it creates some problem when the GUI is being closed
		fig = Figure(figsize = None, dpi = None) 
		ax = fig.add_subplot(111)

		x = "Volume"
		y = "Open"
		z = "High"
		#t = dataSet["Date"]
		print list(dataSet.columns.values)
		#dates = pd.to_datetime(dataSet["Date"])
		#print dates
		t = dataSet[x]
		s = dataSet[y]
		#ax.scatter(t,s)
		ax.scatter(dataSet.index.to_pydatetime(),s)
		#ax.xaxis.set_minor_locator(dates.WeekdayLocator(byweekday=(5),interval=5))
		#ax.xaxis.set_minor_formatter(dates.DateFormatter("%d\n%a"))
		ax.set_xlabel(x); ax.set_ylabel(y); ax.set_title(y + " vs " + x)
		ax.grid(True)
		#ax.plot_date(dates, t)
		t = dataSet[x]
		s = dataSet[z]
		#ax.scatter(t,s)
		#ax.set_xlabel(x); ax.set_ylabel(z); ax.set_title(z + " vs " + x)
		#ax.grid(True)

		# Add the graphic
		canvas = FigureCanvasTkAgg(fig, master = window)
		canvas.show()
		canvas.get_tk_widget().pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

		# Add the (interactive) toolbar
		toolbar = NavigationToolbar2TkAgg(canvas, window)
		toolbar.update()
		canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
