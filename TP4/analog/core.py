from abc import ABC, abstractclassmethod, abstractmethod

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from cusfunc import maprange
from custexcp import *

# __aprox__ = {'butterworth', 'bessel', 'chevy1', 'chevy2', 'cauer', 'legendre'}

#TODO tener cuidado con las unidades de las frecuencias.


class Cell:
    """
    Circuit mimimun unit.  
    
    Parameters:
    den: array_like
    num: array_like
    """

    def __init__(self, den, num):
        print("Hola")
        self.num = num
        self.den = den
        self.sys = signal.TransferFunction(self.den, self.num)
        self.w, self.mag, self.pha = signal.bode(self.sys)
        whd = np.linspace(self.w[0], self.w[-1], len(self.w)*20)
        self.w, self.mag, self.pha = signal.bode(self.sys, w=whd)
        self.zeros, self.poles, self.kZP = signal.tf2zpk(self.den, self.num)
        self.Q = self.compute_q()
        plt.title(f"etapa con Q={self.Q}")
        self.plot_mag(show=True)
        # self.plot_zp(show=True)

    def plot_mag(self, name=None, show=False, lc=None):
        """
        Plot the magnitude bode plot of the specified filter

        Parameters
        ----------
        name: str
            Name to display on plot.
        show: boolean
            False by default. Helpful to stack plots.
            Wether or not to perform plt.show().
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """

        if lc:
            plt.semilogx(np.divide(self.w, 2*np.pi), -
                         self.mag, color=lc, label=name)
        else:
            plt.semilogx(np.divide(self.w, 2*np.pi), -self.mag, label=name)

        if name:
            plt.legend()

        if show:
            plt.show()

    def plot_pha(self, name=None, show=False, lc=None):
        """
        Plot the magnitude bode plot of the specified filter

        Parameters
        ----------
        name: str
            Name to display on plot.
        show: boolean
            False by default. Helpful to stack plots.
            Wether or not to perform plt.show().
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """
        if lc:
            plt.semilogx(np.divide(self.w, 2*np.pi),
                         self.pha, color=lc, label=name)
        else:
            plt.semilogx(np.divide(self.w, 2*np.pi), self.pha, label=name)
        plt.xlabel(f"$Frecuencia Hz$")
        if name:
            plt.legend()
        if show:
            plt.show()

    def plot_zp(self, colorz='red', colorp='blue', zc='o', pc='x', show=False):

        for z in self.zeros:
            plt.scatter(z.real, z.imag, c=colorz, marker=zc)
        for p in self.poles:
            plt.scatter(p.real, p.imag, c=colorp, marker=pc)

        if show:
            plt.show()

    def plot_step_response(self, name=None, show=False, lc=None):
        """
        Plot the step response of the specified filter

        Parameters
        ----------
        name: str
            Name to display on plot.
        show: boolean
            False by default. Helpful to stack plots.
            Wether or not to perform plt.show().
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """
        T, yout = signal.step(self.sys)

        if lc:
            plt.plot(T, yout, color=lc, label=name)
        else:
            plt.plot(T, yout, label=name)
        if show:
            if name:
                plt.legend()
            plt.show()

    def plot_impulse_response(self, name=None, show=False, lc=None):
        T, yout = signal.impulse(self.sys)
        if lc:
            plt.plot(T, yout, color=lc, label=name)
        else:
            plt.plot(T, yout, label=name)
        if show:
            if name:
                plt.legend()
            plt.show()

    def plot_group_delay(self, name=None, show=False, lc=None):
        if lc:
            plt.semilogx(np.divide(
                self.w[1:], 2*np.pi), -np.diff(self.mag)/np.diff(self.w), label=name, color=lc)
        else:
            plt.semilogx(
                np.divide(self.w[1:], 2*np.pi), -np.diff(self.mag)/np.diff(self.w), label=name)
        if show:
            if name:
                plt.legend()
            plt.show()

    def compute_q(self):
        w = self.poles[0].imag
        sigma = self.poles[0].real
        q = np.abs(w/(2*sigma))
        return q

class AnalogFilter(ABC):
    """
    Analog Filter base class
    """

    def __init__(self, ftype, wp, ws, Ap, As, gain=1, rp=0, k=0, N=None):
        self.filter_types = {'lowpass', 'highpass', 'bandpass', 'bandstop'}
        # self.aprox_types = {'butterworth', 'bessel',
        #                     'chevy1', 'chevy2', 'cauer', 'legendre'}

        """
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
    """
        if ftype not in self.filter_types:
            raise InvalidFilterError(
                ftype, f"'{ftype}' is not an available filter. Check docs for supported filters")

        if Ap > As:
            raise ValueError(
                "Pass band attenuation must be lower than stop band")
        if Ap < 0:
            raise ValueError(
                "Passband attenuation must be a non negative number")
        if As < 0:
            raise ValueError(
                "Passband attenuation must be a non negative number")

        if ftype in ('lowpass', 'highpass'):
            if np.size(wp) != 1 or np.size(ws) != 1:
                raise ValueError(
                    'Must specify a only two critical frequencies ws and wp for lowpass or highpass filter')
            if wp > ws and ftype == 'lowpass':
                    raise ValueError(
                        f"Stop frequency (ws={ws} was given) must be greater than Passband frequency (wp={wp} was given)")
            if wp < ws and ftype == 'highpass':
                    raise ValueError(
                        f"Passband frequency (wp={wp} was given) must be greater than Stopfrequency (ws={ws} was given)")
        elif ftype in ('bandpass', 'bandstop'):
            if np.size(wp) != 2 and np.size(ws) != 2:
                raise ValueError(
                    'Wn must specify start and stop frequencies for bandpass or bandstop filter')

            if ftype == 'bandpass':
                if ws[0] > ws[1]:
                    raise ValueError(
                        "Max limit stop band frequency must be greater than min limit")
                if wp[0] > wp[1]:
                    raise ValueError(
                        "Max limit pass band frequency must be greater than min limit")
                if not ws[0] < wp[0] < ws[1]:
                    raise ValueError("Lower pass frequency out of bounds")
                if not ws[0] < wp[1] < ws[1]:
                    raise ValueError("Upper pass frequency out of bounds")
            #TODO comentar bandstop

        if not isinstance(k, float) and not isinstance(k, int):
            raise TypeError(f'k must be numerical. {type(k)} was given')
        if not 0 <= k <= 1:
            raise ValueError(f"{k} Must be between 0 and 1")
        else:
            self.k = k
        if N is not None and N < 0:
            raise ValueError("Filter order must be greater than 0")

        # If no exceptions raised then store the filter specifications
        self.ftype = ftype
        self.wp = wp
        self.ws = ws
        self.Ap = Ap
        self.As = As
        self.k = k
        self.N = N  # Filter order
        self.rp = rp

        # dict that stores if a certain graph is already on the screen and is selecetd
        # controls if filter is going to be graphed
        self.is_graphed = {'Template': 0, 'Magnitude': 0, 'Phase': 0, 'Group Delay': 0,
                           'Maximun Q': 0, 'Impulse Response': 0, 'Step Response': 0, 'Poles and Zeroes': 0}
        self.is_selected = False

        # Step 1: Compute filter order
        self.compute_order()
        # Step 2: Compute the filter coefficients
        self.b, self.a = self.compute_ba()
        # Step 3: Construct Transfer function
        self.sys = signal.TransferFunction(self.b, self.a)

        self.w, self.mag, self.pha = signal.bode(self.sys)
        whd = np.linspace(self.w[0], self.w[-1], len(self.w)*20)
        self.w, self.mag, self.pha = signal.bode(self.sys, w=whd)

        # kZP will denote de gain returned by the compute_zpk method
        self.zeros, self.poles, self.kZP = self.compute_zpk()
        #Step 4: Split high order filter into first and second order cells
        self.stages = self.compute_filter_stages()
        print(f"Hay {len(self.stages)} etapas")

    def pair_singularities(self, zp):
        """
        Return an array containing singularities paired if they are complex conjugates
        
        Parameters
        ----------
        zp: array_like
            Zeros or poles in array format.
        
        Returns
        -------
        out: array_like
            Array containing the singularities paired if they complex conjugates
        
        Examples
        --------

        >>> pair_singularities([1+4j,1-4j,3,58,5+3.24342j,5+3.24342j])
            [[(1-4j), (1+4j)], [3], [58], [(5+3.24342j), (5+3.24342j)]]

        Notes
        -----
        This method relies on 'allclose' by numpy to compare between floating point numbers. 
        """
        result = []
        prev = None
        results = []
        done = []
        array = zp
        for x in array:
            if not prev and x not in done:
                prev = x
            else:
                continue
            for y in array:
                if x.real == y.real and abs(x.imag)==abs(y.imag) and not np.allclose(x,y):
                    results.append([x,y])
                    done.append(x)
                    done.append(y)
                    prev = None
        return results

    def compute_filter_stages(self):
        print(f"el orden del filtro es: {self.N}")
        """
        Split the obtained filter into second and first order units
        
        Returns
        -------
            den: array-like
                Array of shape (n-sections,3) containing the denominator coefficients of the units
            num: array-like
                Array of shape (n-sections,3) containing the numerator coefficients of the units
        """
        #Check if it is an all poles filter
        stages = []
        print(f'hola:{len(self.zeros)}')
        print(f"los polos son{self.poles}")
        if len(self.zeros) == 0:
            ordered_poles = self.pair_singularities(self.poles)
            print(f"Los polos ordenados son {ordered_poles}")
            for poles in ordered_poles:
                print(poles)
                d, n = signal.zpk2tf([], poles, self.kZP)
                stages.append(Cell(d, n))
        else:
            sos = signal.sos(self.zeros, self.poles, self.kZP)
            num = sos[:, :3]
            den = sos[:, 3:]
            for d, n in zip(den, num):
                stages.append(Cell(d, n))
        
        #TODO fix!!
        stages = sorted(stages,key=lambda x:x.Q,reverse=True)
        return stages

    @abstractmethod
    def compute_order(self):
        raise NotImplementedError

    @abstractmethod
    def compute_ba(self):
        raise NotImplementedError

    @abstractmethod
    def compute_zpk(self, parameter_list):
        raise NotImplementedError

    def get_stencils(self, x, y):
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
        >>>     plt.fill(s[0],s[1],'0.8',lw=0,color='orange) #Set line-width=0
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
            (self.wp[0], self.wp[1])
            pLx = [[x[0], fpL, fpL, x[0]]]
            pLy = [[np.max(y), np.max(y), self.Ap, self.Ap]]
            pL = pLx + pLy

            #Stop band
            fsL = np.divide(self.ws[0], 2*np.pi)
            fsR = np.divide(self.ws[1], 2*np.pi)
            sx = [[fsL, fsR, fsR, fsL]]
            sy = [[0, 0, self.As, self.As]]
            sband = sx + sy

            #Right pass band
            fpR = np.divide(self.wp[1], 2*np.pi)
            pRx = [[fpR, x[-1], x[-1], fpR]]
            pRy = [[np.max(y), np.max(y), self.Ap, self.Ap]]
            pR = pRx + pRy

            stencils = [sband]+[pL] + [pR]  # + [sband]
            return stencils

    def plot_mag(self, name=None, dstencils=True, show=False, sc='orange', lc=None):
        """
        Plot the magnitude bode plot of the specified filter

        Parameters
        ----------
        name: str
            Name to display on plot.
        dstencils: boolean
            True by default to display filter stencils
        show: boolean
            False by default. Helpful to stack plots.
            Wether or not to perform plt.show().
        sc: str
            Choosen color to display stencil
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """
        stencils = self.get_stencils(np.divide(self.w, 2*np.pi), -self.mag)
        if lc:
            plt.semilogx(np.divide(self.w, 2*np.pi), -
                         self.mag, color=lc, label=name)
        else:
            plt.semilogx(np.divide(self.w, 2*np.pi), -self.mag, label=name)

        if dstencils:
            for s in stencils:
                plt.fill(s[0], s[1], '1', lw=0, color=sc)  # Set line-

        if name:
            plt.legend()

        if show:
            plt.show()

    def plot_pha(self, name=None, show=False, lc=None):
        """
        Plot the magnitude bode plot of the specified filter

        Parameters
        ----------
        name: str
            Name to display on plot.
        show: boolean
            False by default. Helpful to stack plots.
            Wether or not to perform plt.show().
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """
        if lc:
            plt.semilogx(np.divide(self.w, 2*np.pi),
                         self.pha, color=lc, label=name)
        else:
            plt.semilogx(np.divide(self.w, 2*np.pi), self.pha, label=name)

        if name:
            plt.legend()

        if show:

            plt.show()

    #TODO comentar

    def plot_zp(self, colorz='red', colorp='blue', zc='o', pc='x', show=False):
        for z in self.zeros:
            plt.scatter(z.real, z.imag, c=colorz, marker=zc)
        for p in self.poles:
            plt.scatter(p.real, p.imag, c=colorp, marker=pc)

        if show:
            plt.show()

    def plot_step_response(self, name=None, show=False, lc=None):
        """
        Plot the step response of the specified filter

        Parameters
        ----------
        name: str
            Name to display on plot.
        show: boolean
            False by default. Helpful to stack plots.
            Wether or not to perform plt.show().
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """
        T, yout = signal.step(self.sys)

        #If a color is specifed for the given plot
        if lc:
            plt.plot(T, yout, color=lc, label=name)
        else:
            plt.plot(T, yout, label=name)

        if name:
            plt.legend()
        #Would you like to show your plot.
        if show:
            plt.show()

    #TODO comentar
    def plot_impulse_response(self, name=None, show=False, lc=None):
        T, yout = signal.impulse(self.sys)
        if lc:
            plt.plot(T, yout, color=lc, label=name)
        else:
            plt.plot(T, yout, label=name)

        if name:
            plt.legend()

        if show:
            plt.show()

    #TODO comentar
    def plot_group_delay(self, name=None, show=False, lc=None):
        if lc:
            plt.semilogx(np.divide(
                self.w[1:], 2*np.pi), -np.diff(self.mag)/np.diff(self.w), label=name, color=lc)
        else:
            plt.semilogx(
                np.divide(self.w[1:], 2*np.pi), -np.diff(self.mag)/np.diff(self.w), label=name)

        if name:
            plt.legend()

        if show:
            plt.show()

    #Getters
    def get_order(self):
        return self.N

    def get_w(self):
        return self.w

    def get_mag(self):
        return self.mag

    def get_pha(self):
        return self.pha

    def get_impulse_response(self):
        """
        Returns
        -------
        T: time axis
        yout: amplitude of the impulse response
        
        Examples
        --------
        >>> T, yout = my_filter.get_impulse(self.sys)
        """
        return signal.impulse(self.sys)

    def get_step(self):
        """
        Returns
        -------
        T: time axis
        yout: amplitude of the impulse response
        
        Examples
        --------
        >>> T, yout = my_filter.get_step(self.sys)
        """
        return signal.step(self.sys)

    def get_gdelay(self):
        """
        Returns
        -------
        w-1: frequency axis in hertz
        magnitude
        
        Examples
        --------
        >>> w, gdelay = my_filter.get_gdelay()
        """
        return np.divide(self.w[1:], 2*np.pi), -np.diff(self.mag)/np.diff(self.w)

    # Return True if name is already graphed and False if not
    def isgraphed(self, name):
        if self.is_graphed[name]:
            return True
        else:
            return False

    def mark_graphed(self, name):
        self.is_graphed[name] = 1

    def mark_not_graphed(self, name):
        self.is_graphed[name] = 0

    def select_filter(self):
        self.is_selected = True

    def deselect_filter(self):
        self.is_selected = False
