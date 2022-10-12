
from __future__ import (absolute_import, division, print_function,unicode_literals)
import backtrader as bt
import datetime

import yfinance as yf
#from backtrader import plot 
import pandas as pd

from datetime import datetime
# current_time = datetime.now().strftime('%a %b %d, %Y %I:%M:%S %p')
# print(current_time)
class BtMain:
    
    def __init__(self) -> None:
        pass
    def main_runner(self, name, start_date, end_date=None, path=None ): # accepting path to data so as to not download the data if it already exists.
        
        if path==None:
            pass
        if end_date==None:
            end_date= datetime.strftime(datetime.now(),"%Y-%m-%d")
            
        data_feed = yf.download(name,start_date,end_date)
        data_feed.to_csv(f'./data/{name}.csv')
        return data_feed





