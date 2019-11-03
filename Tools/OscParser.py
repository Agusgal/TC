import pandas as pd
import numpy as np

class OscParser:
  def __init__(self):
    self.oscSignals = None #DataFrame placeholder
    self.parsed_signals = []   #Will hold all singnals in the desired format
  def parse(self,path):
    df = pd.read_csv(path)
    df = df.loc[1:,:].astype(np.float64)
    new_columns = df.columns.values
    new_columns[0] = "time"
    df.columns = new_columns
    df.set_index("time",inplace = True)
    for col in df.columns:
        self.parsed_signals.append(pd.DataFrame(df.loc[:,col]))
        
    return self.parsed_signals