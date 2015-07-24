import download_data
import GUI

def main():
	downloadContent = {'dataCode': 'YAHOO/AAPL', 'startDate':
	'2001-01-01', 'finishDate' : '2005-03-10', 'timeRange' : 'monthly',
	'dataType' : 'pandas'}

	#dataCode = 'YAHOO/AAPL' # Desired data can be found via www.quandl.com, check for code name
	##dataCode = 'UGID/POPCHG_TUR' 
	#startDate = "2001-01-01"
	#finishDate = "2005-03-10"
	##timeRange = "monthly"
	#timeRange = "weekly"
	#dataType = 'pandas'

	#dataset = download_data.get() # default
	#dataset = download_data.get(downloadContent)
	#dataset = download_data.get({})

	#GUI.GUI(dataset, downloadContent)
	GUI.GUI(downloadContent)

	#print dataset
	#print type(dataset)

if __name__ == "__main__":
	main()
