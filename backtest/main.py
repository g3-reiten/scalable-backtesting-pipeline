from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import datetime
import os
import sys
from datetime import datetime

import backtrader as bt
import mlflow
import pandas as pd
import yfinance as yf
from backtrader.analyzers import DrawDown, Returns, SharpeRatio, TradeAnalyzer
from MA_strategy import MaStrategy
from mlflow import log_artifacts, log_metric, log_param, log_params


class BtMain:
    """A class that sets up the cerebro and runs the backtests"""
    def main_runner(self, name, strategy, start_date, end_date=None, path=None, cash=600 ): # accepting path to data so as to not download the data if it already exists.
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
            mlflow.set_experiment('MA_strategy')
            mlflow.start_run(run_name=name)  
            log_param('name',name)
            log_param('start_date', start_date)
            log_param('end_date',end_date)
            log_param('starting_cash',cash)
            
   
        path_exist = os.path.exists(path)     # path exists or not
         
        if not path_exist:
            data_feed = yf.download(name,start_date,end_date)
            data_feed.to_csv(path)
        
        cerebro = bt.Cerebro()
        cerebro.broker.setcash(cash)
        cerebro.addstrategy(strategy)
        cerebro.addanalyzer(SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(Returns, _name='returns')
        cerebro.addanalyzer(DrawDown, _name='draw')
        cerebro.addanalyzer(TradeAnalyzer, _name='trade')
        
        data = bt.feeds.YahooFinanceCSVData(dataname=path,fromdate=datetime.strptime(start_date,"%Y-%m-%d"),
        todate=datetime.strptime(end_date,"%Y-%m-%d"),reverse=False )    
        cerebro.adddata(data) 
        
        return cerebro
    
    def run_backtest(self, cerebro):
        
        # cerebro.broker.setcash(10000.0)
        starting_portfolio = cerebro.broker.getvalue()
        cerRun=cerebro.run()
        final_portfolio=cerebro.broker.getvalue()
        
        results = {}
        metrics = cerRun[0]
        sharpe=metrics.analyzers.sharpe.get_analysis()
        trades=metrics.analyzers.trade.get_analysis()
        returns_amount=metrics.analyzers.returns.get_analysis()
        draw_down=metrics.analyzers.draw.get_analysis()
        
        results['start_portfolio']=starting_portfolio
        log_metric('start_portfolio',results['start_portfolio'])
        
        results['final_portfolio']=final_portfolio
        log_metric('final_portfolio',results['final_portfolio'])
        
        results["sharpe_ratio"]=sharpe['sharperatio']
        log_metric('sharpe_ratio',results['sharpe_ratio'])
        
        results["return"]=returns_amount['rtot']
        log_metric('return',results["return"])
        
        results['max_drawdown'] = draw_down['max']['drawdown']
        log_metric('max_drawdown',results['max_drawdown'])
        
        results['total_trade']=trades['total']['total']
        log_metric('total_trade',results['total_trade'])
        
        results['win_trade']=trades['won']['total']
        log_metric('win_trade',results['win_trade'])
        
        results['loss_trade']=trades['lost']['total']
        log_metric('loss_trade',results['loss_trade'])
        #print(results)
        return results
        
t = BtMain()

cerebro = t.main_runner('BTC-USD',MaStrategy,'2021-1-1') 
result = t.run_backtest(cerebro)





