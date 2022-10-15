import uuid
import pandas as pd

class DataLoader:
    """A class for loading the data
    """
    def read_csv(self, path):
        """
        Read csv file and return dataframe
        Args:
            path: The path of the file
        Return:
            df: dataframe
        """
        df = pd.read_csv(path)
        return df
        
    
    
        
    