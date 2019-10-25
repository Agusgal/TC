import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from abc import ABC, abstractclassmethod, abstractmethod
from cusfunc import maprange
from custexcp import *
__aprox__ = {'butterworth', 'bessel', 'chevy1', 'chevy2', 'cauer', 'legendre'}


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

    Ap : float
      The maximum loss in the passband (db).

    As : float
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

        # print(f"stop w:{ws}")
        # print(f"pass w:{wp}")

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
                    f"Stop frequency (ws={ws} was given) must be greater than Passband frequency (wp={wp} was given)")
            elif wp < ws and ftype == 'highpass':
                raise ValueError(
                    f"Passband frequency (wp={wp} was given) must be greater than Stopfrequency (ws={ws} was given)")

        elif ftype in ('bandpass', 'bandstop'):
            if np.size(wp) != 2 and np.size(ws) != 2:
                raise ValueError(
                    'Wn must specify start and stop frequencies for bandpass or bandstop filter')
            # b = Butterworth('bandpass', 'butterworth', [10E3, 20E3], [5E3, 25E3], 20, 50)
           
            #TODO añadir checks faltantes
            if ftype == 'bandpass':
                if ws[0] < ws[1]:
                    raise ValueError("Max limit stop band frequency must be greater than min limit") 
                if ws[0] > ws[1]:
                    raise ValueError("Min limit stop band frequency must be smaller than max limit")

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

    def compute_order(self):
        """
        Compute the minimum order that satisfies the requierements
        """
        if self.N is None:
            self.N, self.Wn = signal.buttord(
                self.wp, self.ws, self.Ap, self.As, analog=True)

    def compute_ba(self):
        # Compute numerator and denominator polynomials
        wcryt = self.get_critical_w(self.k)
        self.b, self.a = signal.butter(
            self.N, wcryt, self.ftype, analog=True, output='ba')
        return wcryt

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

        if self.ftype == 'lowpass':
            # Compute maximum frequency allowed that still might meet requirements
            wcstop = self.ws * (10**(self.As/10) - 1)**(-1/(2*self.N))
            # Compute minimum allowed frequency that still might meet requirements
            wcpass = self.wp * (10**(self.Ap/10) - 1)**(-1/(2*self.N))
            return maprange([0, 1], [wcpass, wcstop], k)
        elif self.ftype == 'highpass':
            # Compute maximum frequency allowed that still might meet requirements
            wcstop = self.ws * (10**(self.As/10) - 1)**(1/(2*self.N))
            # Compute minimum allowed frequency that still might meet requirements
            wcpass = self.wp * (10**(self.Ap/10) - 1)**(1/(2*self.N))
            # print(f"wcstop calculada:{wcstop}")
            # print(f"wcpass calculada: {wcpass}")
            return maprange([0, 1], [wcpass, wcstop], k)

        elif self.ftype == 'bandpass':

            return self.Wn
        elif self.ftype == 'bandstop':
            return self.Wn
            pass

    def compute_zp(self):
        self.zeros, self.poles, _ = signal.butter(
            self.N, self.wp, self.ftype, analog=True, output='zpk')  # Get zeros and poles

    def get_stencil(self, x, y):
        """
        Get the poligons to plot your requirements on screen.
        The function filter type aware.
         
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
            
        - lowpass  --> 2 stencils
        - highpass --> 2 stencils
        - bandpass --> 3 stencils
        - bandstop --> 3 stencils

        Examples
        --------
        >>> stencils = filter.get_stencils(x,y)
        >>> for s in stencils:
        >>>     plt.fill(s[0],s[s1],lw=0,'0.8') #Set line-width=0
        >>> plt.show()
        """
        if self.ftype == 'lowpass':
            #Pass  band (left side of bode plot)
            p1x = [[x[0],  np.divide(self.wp, 2*np.pi),
                    np.divide(self.wp, 2*np.pi),   x[0]]]
            p1y = [[self.Ap, self.Ap, np.max(y), np.max(y)]]
            p = p1x + p1y

            #Stop  band (right side of bode plot)
            s2x = [[np.divide(self.ws, 2*np.pi), x[-1],
                    x[-1],  np.divide(self.ws, 2*np.pi)]]
            s2y = [[self.As, self.As, 0, 0]]
            s = s2x + s2y

            stencils = [p]+[s]
            return stencils
        elif self.ftype == 'highpass':
            fs = np.divide(self.ws, 2*np.pi)
            s1x = [[x[0], fs, fs, x[0]]]
            s1y = [[np.min(y), np.min(y), self.As, self.As]]
            s = s1x + s1y

            fp = np.divide(self.wp, 2*np.pi)
            p2x = [[fp, x[-1], x[-1], fp]]
            p2y = [[self.Ap, self.Ap, np.max(y), np.max(y)]]
            p = p2x + p2y
            stencils = [p] + [s]
            return stencils
        elif self.ftype == 'bandpass':
            #Left stop band
            fsL = np.divide(self.ws[0], 2*np.pi)
            aLx = [[x[0], fsL, fsL, x[0]]]
            aLy = [[0, 0, self.As, self.As]]
            aL = aLx + aLy
            
            #Pass band
            fpL = np.divide(self.wp[0], 2*np.pi)
            fpR = np.divide(self.wp[1], 2*np.pi)
            px = [[fpL, fpR, fpR, fpL]]
            py = [[self.Ap, self.Ap, max(y), max(y)]]
            pband = px + py

            #Right stop band
            fsR = np.divide(self.ws[1], 2*np.pi)
            aRx = [[fsR, x[-1], x[-1], fsR]]
            aRy = [[self.As, self.As, 0, 0]]
            aR = aRx + aRy

            
            stencils = [aL] + [aR] + [pband]
            return stencils

        elif self.ftype == 'bandstop':
            #Left pass band
            fpL = np.divide(self.wp[0], 2*np.pi)
            print(self.wp[0],self.wp[1])
            pLx = [[x[0], fpL, fpL, x[0]]]
            pLy = [[np.max(y), np.max(y), self.Ap, self.Ap]]
            pL = pLx + pLy
            
            #Stop band
            fsL = np.divide(self.ws[0], 2*np.pi)
            fsR = np.divide(self.ws[1], 2*np.pi)
            print(self.ws)
            sx = [[fsL, fsR, fsR, fsL]]
            sy = [[0,0 ,self.As, self.As]]
            sband = sx + sy

            #Right pass band
            fpR = np.divide(self.wp[1], 2*np.pi)
            pRx = [[fpR, x[-1], x[-1], fpR]]
            pRy = [[np.max(y), np.max(y),self.Ap, self.Ap]]
            pR = pRx + pRy

            
            stencils = [sband]+[pL] + [pR]# + [sband]
            return stencils


    def plot(self, show=False, debug=False):
        sys = signal.TransferFunction(self.b, self.a)
        w, mag, pha = signal.bode(sys)
        plt.xlabel("Frequency Hz")
        plt.ylabel("Atenuation (dB)")
        plt.title(
            f"{str.capitalize(self.aprox)} {str.capitalize(self.ftype)} filter of order {self.N} ")
        plt.semilogx(np.divide(w, 2*np.pi), -mag,
                     label=f"$\omega$: {self.wcryt}")
        stencils = self.get_stencil(np.divide(w, 2*np.pi), -mag)

        for s in stencils:
            plt.fill(s[0], s[1], '0.9', lw=0, color="orange")
            

        # plt.text(self.ws[0],self.As,'This text ends at point (8,3)',horizontalalignment='right')
        # http://queirozf.com/entries/add-labels-and-text-to-matplotlib-plots-annotation-examples
        plt.axis('tight')
        if debug:
            plt.axvline(np.divide(self.ws, 2*np.pi), color="green")
            plt.axvline(np.divide(self.wp, 2*np.pi), color="black")
            plt.legend()

        if show:
            plt.show()


for k in np.linspace(0, 1, 10):
    # b = Butterworth("highpass", "butterworth", 300E3, 100E3, 30, 100, k)
    # b = Butterworth("lowpass","butterworth",1E3,4E3,3,40,k) #Funciona
    # b = Butterworth("lowpass","butterworth",200,500,30,120,k)
    # b = Butterworth('bandpass', 'butterworth', [10E3, 20E3], [5E3, 25E3], 20, 50)
    b = Butterworth('bandstop', 'butterworth', [5E3, 30E3], [10E3, 20E3], 10, 100)

    b.plot(debug=False)

plt.grid(which="both", axis="both")
plt.show()
# b2 = Butterworth("bandpass","butterworth",[2E3,3E3],[1E3,4E3],3,40)
# b2.plot()
