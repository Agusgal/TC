import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
# from .custom_exceptions import *


class AnalogFilter:
    """
    Parameters
    ----------
    ftype: {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}
      Choosen filter type
    wp, ws : float
      wp: pass frequency(ies)
      ws: stop frequency(ies)
      Lowpass: wp = 0.2, ws = 0.3
      Highpass: wp = 0.3, ws = 0.2
      Bandpass: wp = [0.2, 0.5], ws = [0.1, 0.6]
      Bandstop: wp = [0.1, 0.6], ws = [0.2, 0.5]
      For analog filters, wp and ws are angular frequencies (e.g. rad/s).
    aprox: str
    apass : float
      The maximum loss in the passband (db).
    astop : float
      The minimum attenuation in the stopband (dB)
    k: float 
      By default give minimum.
      Selectivity factor. Ranges from 0 to 1.
    N: int
      Order filter. If this N is None the order will be calculated (recommended)
      """

    def __init__(self, ftype, aprox, wp, ws, Ap, As, k=0, N=None):
        self.filter_types = {'lowpass', 'highpass', 'bandpass', 'bandstop'}
        self.aprox_types = {'butterworth', 'bessel',
                            'chevy1', 'chevy2', 'cauer', 'legendre'}

        #Filter typer error checking
        if ftype not in self.filter_types:
          raise InvalidFilterError(
              ftype, f"'{ftype}' is not an available filter. Check docs for supported filters")
        #Aproximation selection error checking
        if aprox not in self.aprox_types:
              raise InvalidAproxError(
                  aprox, f"'{aprox}' is not an available aproximation. Check docs for supported aproximation")

        if ftype in ('lowpass', 'highpass'):
          if np.size(wp) != 1 or np.size(ws) != 1:
            raise ValueError(
                'Must specify a only two critical frequencies ws and wp for lowpass or highpass filter')
          if wp > ws:
            raise ValueError("Pass frecuecny")
        elif ftype in ('bandpass', 'bandstop'):
            if np.size(wp) != 2 and np.size(ws) != 2:
              raise ValueError(
                  'Wn must specify start and stop frequencies for bandpass or bandstop filter')

        if type(k) is not float and type(k) is not int:
          raise TypeError(f"k must be numerical. {type(k)} was given")
        if not 0 <= k <= 1:
          raise ValueError(f"{k} Must be between 0 and 1")
        else:
          self.k = k
        if N is not None and N < 0:
          raise ValueError("Filter order must be greater than 0")
        else:
          self.N = N

        #If no exceptions raised then store the filter specifications
        self.ftype = ftype
        self.aprox = aprox
        self.wp = wp
        self.ws = ws
        self.Ap = Ap
        self.As = As
        self.k = k
#TODO documentar. Esta es la frecuencia limite en banda antenuada
    def get_critical_w(self):
      self.ws * ( 10**(-self.As/10) - 1)**(-1/(2*self.N))

    def lowpass(self):
      #Filter order not defined
      if self.N is None:
        self.N = signal.buttord(self.wp, self.ws, self.Ap, self.As, analog=True)[0]
      #We use the denormalization factor 'k' to get the transfer function

      self.b, self.a = signal.butter(self.N, self.wp, 'lowpass', analog=True, output='ba') #Compute numerator and denominator polynomials

      self.zeros, self.poles, _ = signal.butter(self.N, self.wp, 'lowpass', analog=True, output='zpk') #Get zeros and poles

