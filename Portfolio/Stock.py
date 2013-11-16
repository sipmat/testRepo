class Stock(object):
	#prices is list of stock prices for specific time period   
	def __init__(self, name, prices):
		self.name = name
		self.prices = prices
		self.MDD = 0

	def maximal_drawdown(self):
		DD = list()
		peak = -99999
		for price in self.prices:
			if(price > peak):
				peak = price
  			DD.append(100.0 * (peak - price) / peak)
  			if (DD[len(DD) - 1] > self.MDD):
    				self.MDD = DD[len(DD) - 1]
		print self.MDD

	#def maximal_drawup(self):

Test1 = Stock("SMTH", [2, 3, 5, 7, 3, 4, 1, 4])
Test1.maximal_drawdown()
