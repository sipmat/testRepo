class Stock(object):
	#prices is list of stock prices for specific time period   
	def __init__(self, name, prices):
		self.name = name
		self.prices = prices
		self.MDD = 0
		self.MDU = 0

	def maximal_drawdown(self):
		DD = 0
		peak = -99999
		for price in self.prices:
			if(price > peak):
				peak = price
  			DD = (100.0 * (peak - price) / peak)
  			if (DD > self.MDD):
    				self.MDD = DD
		print self.MDD

	def maximal_drawup(self):
		DU = 0
                bottom = 99999
                for price in self.prices:
                        if(price < bottom):
                                bottom = price
                        DU = (100.0 * (price - bottom) / price)
                        if (DU > self.MDU):
                                self.MDU = DU
                print self.MDU

Test1 = Stock("SMTH", [2, 3, 5, 7, 3, 4, 1, 4])
Test1.maximal_drawdown()
Test1.maximal_drawup()
