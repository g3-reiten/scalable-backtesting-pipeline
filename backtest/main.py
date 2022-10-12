
from __future__ import (absolute_import, division, print_function,unicode_literals)
import backtrader as bt
import datetime

import yfinance as yf
#from backtrader import plot 
import pandas as pd
import os
from datetime import datetime
# current_time = datetime.now().strftime('%a %b %d, %Y %I:%M:%S %p')
# print(current_time)

class BtMain:
    
    def __init__(self) -> None:
        pass
    def main_runner(self, name, start_date, end_date=None, path=None ): # accepting path to data so as to not download the data if it already exists.
        
        if path==None:
            path=f'./data/{name}.csv'
        if end_date==None:
            end_date= datetime.strftime(datetime.now(),"%Y-%m-%d")
            
        # Check whether the specified
        # path exists or not
        path_exist = os.path.exists(path)
        #print(data_check)  
         
        if not path_exist:
            data_feed = yf.download(name,start_date,end_date)
            data_feed.to_csv(f'./data/{name}.csv')
        
        cerebro = bt.Cerebro()
        data = bt.feeds.YahooFinanceCSVData(dataname=data_feed,fromdate=datetime.strptime(start_date,"%Y-%m-%d"),
        todate=datetime.strptime(end_date,"%Y-%m-%d"),reverse=False )    
        cerebro.adddata(data) 
           
         #return data_feed
        return cerebro





