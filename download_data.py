import Quandl # www.github.com/quandl/Python

def get(content):
	if bool(content):
		print "try works"
		return Quandl.get(content['dataCode'], trim_start =	content['startDate'],
		trim_end = content['finishDate'], collapse = content['timeRange'],
		transformation = 'rdiff', returns = content['dataType']) # Warning: Uses Internet Connection
	else:
		print "except works"
		return Quandl.get('YAHOO/AAPL', trim_start = '2001-01-01',
						  trim_end = '2010-01-01', collapse = 'annual',
						  returns = 'pandas')
