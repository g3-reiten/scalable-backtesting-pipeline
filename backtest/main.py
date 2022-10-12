import backtrader as bt
import datetime
import yfinance as yf
#from backtrader import plot 


def get_feeds(name, start_date, end_date):
    data_feed = bt.feeds.PandasData(dataname=yf.download(name,start_date,end_date))
    return data_feed
# Instantiate Cerebro engine


# Set data parameters and add to Cerebro
data = get_feeds("ALGO-USD",'2021-6-25','2022-6-25')
cerebro = bt.Cerebro()
cerebro.adddata(data)
