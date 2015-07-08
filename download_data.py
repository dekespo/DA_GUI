import Quandl # www.github.com/quandl/Python

def get(dataCode = 'YAHOO/AAPL', startDate = "2001-01-01", finishDate = "2010-01-01", timeRange = "annual", dataType = 'pandas'):
	
	return Quandl.get(dataCode, trim_start = startDate,
						 trim_end = finishDate, collapse = timeRange,
						 transformation = 'rdiff', returns = dataType) # Warning: Uses Internet Connection
