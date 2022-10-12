import backtrader as bt
import datetime
import yfinance as yf
from backtrader import plot 

class MA(bt.Strategy):
    
	def __init__(self):
		self.ma = bt.indicators.SimpleMovingAverage(self.data.close, period=100)
		self.order = None
 
	def next(self):
		if self.order:
			return
		if not self.position: # to check if we already have a position in the market
      
			if (self.data.close[0] > self.ma[0]) & (self.data.close[-1] < self.ma[-1]):
				self.log('Buy Create, %.2f' % self.data.close[0])
				self.order = self.buy(size=10) # buy when closing price today crosses above MA.
    
			if (self.data.close[0] < self.ma[0]) & (self.data.close[-1] > self.ma[-1]):
				self.log('Sell Create, %.2f' % self.data.close[0])
				self.order = self.sell(size=10)  # sell when closing price today below MA
		else:
		# This means we are in a position, and hence you need to define exit strategy here.
			if len(self) >= (self.bar_executed + 4):
				self.log('Position Closed, %.2f' % self.data.close[0])
				self.order = self.close()

	def log(self, txt):
		dt=self.datas[0].datetime.date(0)
		print('%s, %s' % (dt.isoformat(), txt))
		