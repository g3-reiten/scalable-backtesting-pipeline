
import os
import sys
import unittest
import pandas as pd

# sys.path.append(os.path.abspath(os.path.join('./scripts')))
# sys.path.append(os.path.abspath(os.path.join('../scripts/')))
# sys.path.insert(1, '..')
sys.path.append("..")
# sys.path.append(".")
from scripts import helper
class TestFiles(unittest.TestCase):
        
  def test_read_csv(self):
  
    df = helper.read_df('./data/test.csv')
    df1 = pd.read_csv('./data/test.csv')
    self.assertEqual(df.shape, df1.shape)
    
    
if __name__ == '__main__':
  unittest.main()