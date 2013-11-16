import datetime
import urllib

class RetrieveStock(object):
	
	base_url = "http://ichart.finance.yahoo.com/table.csv?s="

	def __init__(self, ID, startDate, endDate, interval):
		self.ID = ID
		self.startDate = startDate
		self.endDate = endDate
		self.interval = interval
		self.dt_url = '%s&a=%d&b=%d&c=%d&d=%d&e=%d&f=%d&g=%s&ignore=.csv'% (ID, startDate.month-1, startDate.day, startDate.year, endDate.month-1, endDate.day, endDate.year, interval)

	def pull_historical_data(self):
		try:
        		print (self.base_url + self.dt_url)
			return urllib.urlretrieve(self.base_url + self.dt_url)
		except urllib.ContentTooShortError as e:
			print "Wrong URL"

newRetrieveStock = RetrieveStock('csco', datetime.date(2012,1,1), datetime.date(2013,1,1), "d")
print newRetrieveStock.pull_historical_data()
#s = datetime.date(2012,1,1)
#e = datetime.date(2013,1,1)
