import backtrader as bt 

class CerebroBT:
    """
    create a cerebro instance
    
    feed data to the cerebro instance
    """
    def __init__(self):
        pass

    def create_cerebro(self):
        """
        creates a cerebro instance
        """
        cerebro = bt.Cerebro()
        return cerebro
    
    def feed_cerebro(self, finance_data,  cerebro):
        """
        feeds the data to the cerebro
        """
        cerebro.adddata(finance_data)