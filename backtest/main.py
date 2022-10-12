import backtrader as bt
import datetime
import yfinance as yf
from backtrader import plot 
# Instantiate Cerebro engine
cerebro = bt.Cerebro()

# Set data parameters and add to Cerebro
data = bt.feeds.YahooFinanceCSVData(
    dataname='../data/BTC-USD.csv',
    fromdate=datetime.datetime(2021,10, 14),
    todate=datetime.datetime(2021, 10, 24),
)
