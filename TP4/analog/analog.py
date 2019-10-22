import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from abc import ABC, abstractclassmethod, abstractmethod
from cusfunc import maprange
from custexcp import *
__aprox__ = {'butterworth', 'bessel', 'chevy1', 'chevy2', 'cauer', 'legendre'}

def prueba():
    print("Hola")
    
class AnalogFilter(ABC):
    """
    Analog Filter
    """
    # self.filter_types = {'lowpass', 'highpass', 'bandpass', 'bandstop'}
    # self.aprox_types = {'butterworth', 'bessel','chevy1', 'chevy2', 'cauer', 'legendre'}
    
    def __init__(self, parameter_list):
        raise NotImplementedError

    def get_ba(self):
        """
        Returns
        -------
        b,a:
        """
        return self.b, self.a
    def make_stencil(self, parameter_list):
        raise NotImplementedError
    
    def plot_mag(self, parameter_list):
        raise NotImplementedError

    def plot_pha(self, parameter_list):
        raise NotImplementedError

    def plot_zp(self, parameter_list):
        raise NotImplementedError

    def plot_step_response(self, parameter_list):
        raise NotImplementedError

    def plot_impulse_response(self, parameter_list):
        raise NotImplementedError

    def plot_group_delay(self, parameter_list):
        raise NotImplementedError


class Butterworth:
    """
    General analog filter designer tool
    Parameters
    ----------
    ftype: {‘lowpass’, ‘highpass’, ‘bandpass’, ‘bandstop’}
      Choosen filter type
    
    wp, ws : float
      wp: pass frequency(ies) in (rads/seg)
      ws: stop frequency(ies) in (rads/seg)
      - Lowpass: wp = 0.2, ws = 0.3
      - Highpass: wp = 0.3, ws = 0.2
      - Bandpass: wp = [0.2, 0.5], ws = [0.1, 0.6]
      - Bandstop: wp = [0.1, 0.6], ws = [0.2, 0.5]
      For analog filters, wp and ws are angular frequencies (e.g. rad/s).
    aprox: str
    apass : float
      The maximum loss in the passband (db).
    astop : float
      The minimum attenuation in the stopband (dB).
    k: float 
      By default give minimum.
      Selectivity factor. Ranges from 0 to 1.
    N: int
      Order filter. If this N is None the order will be calculated (recommended)

    Examples
    --------
    b1 = Butterworth()
      """

    def __init__(self, ftype, aprox, wp, ws, Ap, As, k=0, N=None):
        self.filter_types = {'lowpass', 'highpass', 'bandpass', 'bandstop'}
        self.aprox_types = {'butterworth', 'bessel',
                            'chevy1', 'chevy2', 'cauer', 'legendre'}
        # Filter typer error checking
        if ftype not in self.filter_types:
            raise InvalidFilterError(
                ftype, f"'{ftype}' is not an available filter. Check docs for supported filters")
        # Aproximation selection error checking
        if aprox not in self.aprox_types:
            raise InvalidAproxError(
                aprox, f"'{aprox}' is not an available aproximation. Check docs for supported aproximation")

        if ftype in ('lowpass', 'highpass'):
            if np.size(wp) != 1 or np.size(ws) != 1:
                raise ValueError(
                    'Must specify a only two critical frequencies ws and wp for lowpass or highpass filter')
            if wp > ws and ftype == 'lowpass':
                raise ValueError(
                    "Stop frequency (ws) must be greater than Passband frequency (wp)")
            elif wp < ws and ftype == 'highpass':
                raise ValueError(
                    "Passband frequency (wp) must be greater than Stopfrequency (ws)")

        elif ftype in ('bandpass', 'bandstop'):
            if np.size(wp) != 2 and np.size(ws) != 2:
                raise ValueError(
                    'Wn must specify start and stop frequencies for bandpass or bandstop filter')

        if type(k) is not np.float64 and type(k) is not np.int:
            raise TypeError(f"k must be numerical. {type(k)} was given")
        if not 0 <= k <= 1:
            raise ValueError(f"{k} Must be between 0 and 1")
        else:
            self.k = k
        if N is not None and N < 0:
            raise ValueError("Filter order must be greater than 0")
        else:
            self.N = N

        # If no exceptions raised then store the filter specifications
        self.ftype = ftype
        self.aprox = aprox
        self.wp = wp
        self.ws = ws
        self.Ap = Ap
        self.As = As
        self.k = k

        # Filter data
        # Computes numerator and denominator of the transfer function
        self.compute_order()
        self.wcryt = self.compute_ba()
        self.compute_zp()

    def get_critical_w(self, k):
        """
        Calculates new crytical frequency given a certain denormalization degree 
        Parameters
        ----------
        k: float
          Mandatory frequency (rads/seg) where we want our filter to pass trough.

        Returns
        -------
        wlimit: float
          Lowpass or highpass new crytical frequency (not cutoff) to generate the new filter

        """

        # Compute maximum frequency allowed that still might meet requirements
        wcstop = self.ws * (10**(self.As/10) - 1)**(-1/(2*self.N))
        # Compute minimum allowed frequency that still might meet requirements
        wcpass = self.wp * (10**(self.Ap/10) - 1)**(-1/(2*self.N))
        if self.ftype == 'lowpass':
            return maprange([0, 1], [wcpass, wcstop], k)
        elif self.ftype == 'highpass':
            return maprange([0, 1], [wcstop, wcpass], k)
    def compute_order(self):
        """
        Compute the minimum order that satisfies the requierements
        """
        if self.N is None:
            self.N = signal.buttord(
                self.wp, self.ws, self.Ap, self.As, analog=True)[0]

    def compute_ba(self):
        # Compute numerator and denominator polynomials
        wcryt = self.get_critical_w(self.k)
        self.b, self.a = signal.butter(
            self.N, wcryt, self.ftype, analog=True, output='ba')
        return wcryt

    def compute_zp(self):
        self.zeros, self.poles, _ = signal.butter(
            self.N, self.wp, self.ftype, analog=True, output='zpk')  # Get zeros and poles

    def get_stencil(self, x, y):
        """
        Get the poligons to plot your requirements on screen.
        The function is aware of the filter.
         
        Parameters
        ----------
        x: array_like
            Array containing the x values where the functions was evaluated
        y: array_like
            Array containing y(x) values
        Returns
        --------
        stencils: array_like
            An array of arrays containig the poligons needed to show the stencil
            -lowpass --> 2 stencils
            -highpass --> 2 stencils
            -bandass --> 3 stencils
            -highpass --> 3 stencils

        Examples
        --------
        >>>stencils = filter.get_stencils(x,y)
        >>>for s in stencils:
        >>> plt.fill(s[0],)
        """
        if self.ftype == 'lowpass':
            p1x = [[x[0],  np.divide(self.wp, 2*np.pi),
                    np.divide(self.wp, 2*np.pi),   x[0]]]
            p1y = [[self.Ap, self.Ap, np.max(y), np.max(y)]]
            p = p1x + p1y

            s2x = [[np.divide(self.ws, 2*np.pi), x[-1],
                    x[-1],  np.divide(self.ws, 2*np.pi)]]
            s2y = [[self.As, self.As, 0, 0]]
            s = s2x + s2y
            stencils = [p]+[s]
            return stencils
        elif self.ftype == 'highpass':
            s1x = [[x[0],  np.divide(self.ws, 2*np.pi),
                    np.divide(self.ws, 2*np.pi),   x[0]]]
            s1y = [[np.min(y), np.min(y), self.As, self.As]]
            s = s1x + s1y

            p2x = [[np.divide(self.wp, 2*np.pi), x[-1],
                    x[-1],  np.divide(self.wp, 2*np.pi)]]
            p2y = [[self.Ap, self.Ap, np.max(y), np.max(y)]]
            p = p2x + p2y
            stencils = [p] + [s]
            return stencils

    def plot(self, show=False, debug=False):
        sys = signal.TransferFunction(self.b, self.a)
        w, mag, pha = signal.bode(sys)
        plt.xlabel("Frequency Hz")
        plt.ylabel("Atenuation (dB)")
        if debug:
            plt.axvline(np.divide(self.ws, 2*np.pi), color="green")
            plt.axvline(np.divide(self.wp, 2*np.pi), color="black")
        plt.title(
            f"{str.capitalize(self.aprox)} {str.capitalize(self.ftype)} filter of order {self.N} ")
        plt.semilogx(np.divide(w, 2*np.pi), -mag,
                     label=f"$\omega$: {self.wcryt}")
        stencils = self.get_stencil(np.divide(w, 2*np.pi), -mag)
        for s in stencils:
            plt.fill(s[0], s[1], '0.9', lw=0, color="orange")
        # plt.legend()
        if show:
            plt.show()


for k in np.linspace(0, 1, 10):
    # b = Butterworth("highpass", "butterworth", 10E3, 5E3, 3, 40, k)
    b = Butterworth("lowpass","butterworth",1E3,3E3,3,40,k)

    # butters.append(b)
    b.plot()

plt.grid(which="both", axis="both")
plt.show()
# b2 = Butterworth("bandpass","butterworth",[2E3,3E3],[1E3,4E3],3,40)
# b2.plot()
