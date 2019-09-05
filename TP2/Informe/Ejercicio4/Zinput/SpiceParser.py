import pandas as pd
import numpy as np
class SpiceParser:
  def __init__(self):
    pass
  
  def parse(self,path, togheter=False,acsplit=True):
    """
    Returns signals from LTspice file.
    Paramas:
    togheter: 
     -False(default): Returns an 'array!' of DataFrames with one signal per df 
     -True: All signals in one single 'DataFrame!'
    acsplit:
    -True(default): Returns an array of indivudual signal. Phase and Magnitude
    -False: Return an array of 'pair' of signals. Phase and Magnitude in a single DataFrame per signal
    If DC simulation a dataframe per signal is returned. If AC simulation then a DataFrame with magnitude and phase is returned

    """
    signals_thogheter = self.read_ltspice(path) #Single DataFrame with all signal available

    if togheter == True:
      return signals_thogheter
    elif togheter == False:
      splitted = self.split_signals(signals_thogheter,acsplit=acsplit)
      return splitted
  
  def split_signals(self,df,acsplit=True):
    """"
    This method spits a Signals DataFrame into indivdual Signals
    Returns an array of signals
    acsplit:
    -True(default): Returns an array of indivudual signal. Phase and Magnitude
    -False: Return an array of 'pair' of signals. Phase and Magnitude in a single DataFrame per signal

    """
    dfs = [] #Placeholder to store signals
    
    #If AC Sim then take columns by pairs (MAG & PHA)
    if df.index.name == "frequency":
      if acsplit == False:
        for i in range(0,len(df.columns),2):
          dfs.append(pd.DataFrame(df.iloc[:,i:i+2]))
      elif acsplit == True:
        for i in range(0,len(df.columns)):
          dfs.append(pd.DataFrame(df.iloc[:,i]))
          
    #If DC create individual DataFrames for each measurement
    elif df.index.name == "time":
      for col in df.columns:
        dfs.append(pd.DataFrame(df.loc[:,col]))
    return dfs
      
  
  def read_ltspice(self,path):
    
    """
    Receives path name from LTSpice and return ready to use DataFrame
    DC simulation --> index represents "time". Not real time, only for graphical porpouses
    AC simulation --> index represents "frequency" in Hz
    """
    #Read data
    print(f'Este es el path recibido: {path}')
    data = open(path,encoding="latin-1")
    df = pd.read_csv(data,sep="\t")
    #If it is a DC simulation. Just add a time column for graphing. Cast to float and return
    if 'Freq.' not in df.columns:
      for column in df.columns:
        df[column] = df[column].astype(np.float64) #Cast to float
      #Adding a series of time
      time = np.arange(0,len(df.index))
      df["time"] = time
      df.set_index("time",inplace=True)
      return df

    #If it is an AC simulation
    else:
      df.set_index(df.columns[0],inplace=True) 
      df.index.names = ["frequency"]
      for column in df.columns:
        #Removing dB and ° symbols using Regex
        df[column].replace('[°|dB|\(|\)]','', inplace=True, regex = True) #Getting rid of non-wanted symbols
        #Spliting magnitude and phase into independent Pandas Series
        splitted_df = df[column].str.split(pat=",", expand=True)
        #We assign the series to the dataframe
        df[f'{column} MAG'] = splitted_df[0].astype(np.float64)
        df[f'{column} PHA'] = splitted_df[1].astype(np.float64)
        #Drop the original ugly column
        df.drop(column,axis=1,inplace=True)
    return df