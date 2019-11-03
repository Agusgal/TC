import pandas as pd
import numpy as np

class ManualBodeParser:
    def __init__(self):
        self.dfs = []

    def parse(self,path):
        df = pd.read_excel(path)
        print(df.head())
        df.set_index(df.columns[0],inplace = True)
        for column in df.columns:
            if "PHA" in column or "MAG" in column:
               self.dfs.append(pd.DataFrame(df[column].astype(np.float64)).dropna())
            else:
                print(column)
                print("Wrong column name")
        return self.dfs