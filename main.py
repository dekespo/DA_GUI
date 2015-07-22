import download_data
import GUI

def main():
	dataCode = 'YAHOO/AAPL' # Desired data can be found via www.quandl.com, check for code name
	#dataCode = 'UGID/POPCHG_TUR' 
	startDate = "2001-01-01"
	finishDate = "2005-03-10"
	#timeRange = "monthly"
	timeRange = "weekly"
	dataType = 'pandas'

	dataset = download_data.get(dataCode, startDate, finishDate, timeRange, dataType)
	#dataset = download_data.get() # default

	GUI.GUI(dataset)

	#print dataset
	#print type(dataset)

if __name__ == "__main__":
	main()
