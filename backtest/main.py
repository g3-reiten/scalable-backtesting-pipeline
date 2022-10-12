
from __future__ import (absolute_import, division, print_function,unicode_literals)
import backtrader as bt
import datetime

import yfinance as yf
#from backtrader import plot 
import pandas as pd
import os
from datetime import datetime
import mlflow
from mlflow import log_metric, log_param, log_artifacts, log_params
# current_time = datetime.now().strftime('%a %b %d, %Y %I:%M:%S %p')
# print(current_time)

class BtMain:
    """A class that sets up the cerebro and runs the backtests"""
    # def __init__(self) -> None:
    #     pass
    def main_runner(self, name, strategy, start_date, end_date=None, path=None ): # accepting path to data so as to not download the data if it already exists.
        x=1
        #mlflow.start_run()
        if path==None:
            path=f'./data/{name}.csv'
        if end_date==None:
            end_date= datetime.strftime(datetime.now(),"%Y-%m-%d")
        if True:
            try:
                mlflow.end_run()
            except:
                pass
            mlflow.set_tracking_uri('mlruns') 
            mlflow.set_experiment("strategy")
            mlflow.start_run()  
            mlflow.log_param('name',name)
            mlflow.log_param('start_date', start_date)
            mlflow.log_param('end_date',end_date)
        
        # Check whether the specified
        # path exists or not
        path_exist = os.path.exists(path)
        #print(data_check)  
         
        if not path_exist:
            data_feed = yf.download(name,start_date,end_date)
            data_feed.to_csv(path)
        
        cerebro = bt.Cerebro()
        data = bt.feeds.YahooFinanceCSVData(dataname=path,fromdate=datetime.strptime(start_date,"%Y-%m-%d"),
        todate=datetime.strptime(end_date,"%Y-%m-%d"),reverse=False )    
        cerebro.adddata(data) 
           
         #return data_feed
        return cerebro
    
    def run_backtest(self, cerebro):
        cerebro.broker.setcash(10000.0)
        starting = cerebro.broker.getvalue()
        
        # Print out the starting conditions
        #print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
        
        cerebro.run()
        
        final=cerebro.broker.getvalue()
        
# Test = BtMain()
# run = Test.main_runner("SOL-USD","SMA","2021-1-1","2022-1-1")






