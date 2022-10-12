
from __future__ import (absolute_import, division, print_function,unicode_literals)
import backtrader as bt
import datetime

import yfinance as yf
#from backtrader import plot 
import pandas as pd
class BtMain:
    
    def __init__(self) -> None:
        pass
    def get_feeds(self, name, start_date, end_date):
        data_feed = yf.download(name,start_date,end_date)
        data_feed.to_csv(f'./data/{name}.csv')
        return data_feed





