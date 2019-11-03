import pandas as pd
from scipy import signal
import numpy as np


class HsParser:
  def __init__(self):
    self.transferFunctions = None #DataFrame placeholder
    self.parsed_signals = []   #Will hold all singnals in the desired format
    
  def parse(self,path):
    self.transferFunctions = pd.read_json(path) #Parse Json
    self.generate_signals()                     #Using the transfer functions given construct the signal
    return self.parsed_signals    
  
  
  def generate_signals(self):
    self.parsed_signasl = []
    for h in self.transferFunctions.columns:
      
      #Retrieve denominator and numerator of the transfer function
      den = self.transferFunctions[h]["den"]
      num = self.transferFunctions[h]["num"]
      
      #Create LTI system and run bode
      sys = signal.TransferFunction(num,den)
      w, mag, phase = signal.bode(sys)
      
      #Convert to Hz
      f = np.divide(w,2*np.pi)
      
      #Generate the dataframes containing the signals
      df_p = pd.DataFrame(index = f, columns=[f'{h} PHA'])
      df_p[f'{h} PHA'] = phase
      df_p.index.names = ["frequency"]
      df_m = pd.DataFrame(index = f, columns=[f'{h} MAG'])
      df_m[f'{h} MAG'] = mag
      df_m.index.names = ["frequency"]

      #Add cooked signals
      self.parsed_signals.append(df_p)
      self.parsed_signals.append(df_m)


    #   """
    # Calculate Bode magnitude and phase data of a continuous-time system.

    # Parameters
    # ----------
    # system : an instance of the LTI class or a tuple describing the system.
    #     The following gives the number of elements in the tuple and
    #     the interpretation:

    #         * 1 (instance of `lti`)
    #         * 2 (num, den)
    #         * 3 (zeros, poles, gain)
    #         * 4 (A, B, C, D)

    # w : array_like, optional
    #     Array of frequencies (in rad/s). Magnitude and phase data is calculated
    #     for every value in this array. If not given a reasonable set will be
    #     calculated.
    # n : int, optional
    #     Number of frequency points to compute if `w` is not given. The `n`
    #     frequencies are logarithmically spaced in an interval chosen to
    #     include the influence of the poles and zeros of the system.

    # Returns
    # -------
    # w : 1D ndarray
    #     Frequency array [rad/s]
    # mag : 1D ndarray
    #     Magnitude array [dB]
    # phase : 1D ndarray
    #     Phase array [deg]

    # Notes
    # -----
    # If (num, den) is passed in for ``system``, coefficients for both the
    # numerator and denominator should be specified in descending exponent
    # order (e.g. ``s^2 + 3s + 5`` would be represented as ``[1, 3, 5]``).

    # .. versionadded:: 0.11.0

    # Examples
    # --------
    # >>> from scipy import signal
    # >>> import matplotlib.pyplot as plt

    # >>> sys = signal.TransferFunction([1], [1, 1])
    # >>> w, mag, phase = signal.bode(sys)

    # >>> plt.figure()
    # >>> plt.semilogx(w, mag)    # Bode magnitude plot
    # >>> plt.figure()
    # >>> plt.semilogx(w, phase)  # Bode phase plot
    # >>> plt.show()

    # """