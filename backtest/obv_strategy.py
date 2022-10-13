import backtrader as bt
import numpy as np
import matplotlib.pyplot as plt

#import backtrader.indicators as btind
#btind.AroonOscillator

class OBVStrategy(bt.Strategy):
    """
    Apply the OBV strategy in trading
    """

    def __init__(self, dataframe):
        self.dataframe = dataframe
        pass
    
    def next(self):
        # Calculate the On Balance Volume using closing values
        # the obv line builds on the previous value
        # Parameter: dataframe
        OBVs = []
        OBVs.append(0) 
        for i in range(1, len(self.dataframe.Close)):
            if self.dataframe.Close[i] > self.dataframe.Close[i-1]:
                # If the closing price is above the prior close price 
                # then: Current OBV = Previous OBV + Current Volume
                OBVs.append(OBVs[-1] + self.dataframe.Volume[i]) 
            elif self.dataframe.Close[i] < self.dataframe.Close[i-1]:
                OBVs.append( OBVs[-1] - self.dataframe.Volume[i])
            else:
                OBVs.append(OBVs[-1])
        return OBVs
    
    def calculate_OBV_EMA(self, OVMs):
        # Store the OBV and OBV EMA into new columns
        # exponential moving average (EMA)
        EMAs = []
        for i in range(len(OVMs)):
            EMAs.append(OVMs[i].ewm(com=20).mean())
        return EMAs
    
    def generate_trading_signal(self, df, obv, obv_ema):
        """
        Create a function to signal when to buy and sell an asset
        If OBV > OBV_EMA Then Buy
        If OBV < OBV_EMA Then Sell
        Else Do nothing

        PARAMETERS: list of obv values, list of ema values
        """
        # lists to store values of buying or selling signals
        sigPriceBuy = []
        sigPriceSell = []
        # A flag to set the trend upward/downward
        flag = -1 
        for i in range(0,len(obv)):
            # if OBV > OBV_EMA  and flag != 1 then buy
            if obv[i] > obv_ema and flag != 1:
                sigPriceBuy.append(df['Close'][i])
                sigPriceSell.append(np.nan)
                # upward trend
                flag = 1
            elif obv[i] < obv_ema and flag != 0:
                # else  if OBV < OBV_EMA  and flag != 0 then sell
                sigPriceSell.append(df['Close'][i])
                sigPriceBuy.append(np.nan)
                # downward trend
                flag = 0
            else:
                # else OBV == OBV_EMA so append NaN
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        return (sigPriceBuy, sigPriceSell)

    def plot_signals(self, df):
        # Visually Show The Stock buy and sell signals
        #Create and plot the graph
        plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
        plt.scatter(df.index, df['Buy_Signal_Price'], color = 'green', label='Buy Signal', marker = '^', alpha = 1)
        plt.scatter(df.index, df['Sell_Signal_Price'], color = 'red', label='Sell Signal', marker = 'v', alpha = 1)
        plt.plot( df['Close'],  label='Close Price', alpha = 0.35)#plt.plot( X-Axis , Y-Axis, line_width, alpha_for_blending,  label)
        plt.xticks(rotation=45)
        plt.title('The Stock Buy / Sell Signals')
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Close Price USD ($)',fontsize=18)
        plt.legend( loc='upper left')
        plt.show()
    
    def plot_ovm_ema(self, df):
        #Create and plot the graph
        plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
        #plt.plot( df['Close'],  label='Close')#plt.plot( X-Axis , Y-Axis, line_width, alpha_for_blending,  label)
        plt.plot( df['OBV'],  label='OBV', color= 'orange')
        plt.plot( df['OBV_EMA'],  label='OBV_EMA', color= 'purple')
        plt.xticks(rotation=45) 
        plt.title('OBV/OBV_EMA')
        plt.xlabel('Date',fontsize=18)
        plt.ylabel('Price USD ($)',fontsize=18)
        plt.show()
