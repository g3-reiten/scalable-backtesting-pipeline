import backtrader as bt
import datetime
import yfinance as yf
#from backtrader import plot 
import pandas as pd
class GetFeeds:
    
    def __init__(self) -> None:
        pass
    def get_feeds(self, name, start_date, end_date):
        data_feed = yf.download(name,start_date,end_date)
  
        return data_feed

test = GetFeeds()
    
data = test.get_feeds('TSLA', '2018-01-01', '2019-01-01')
data.to_csv(f'./data/TSLA.csv')




