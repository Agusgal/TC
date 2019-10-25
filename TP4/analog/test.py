import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from abc import ABC, abstractclassmethod, abstractmethod
from cusfunc import maprange
from custexcp import *
# __aprox__ = {'butterworth', 'bessel', 'chevy1', 'chevy2', 'cauer', 'legendre'}


class AnalogFilter(ABC):
    """
    Analog Filter
    """

    def __init__(self, ftype, wp, ws, Ap, As, rp=0, k=0, N=None):
        self.filter_types = {'lowpass', 'highpass', 'bandpass', 'bandstop'}
        # self.aprox_types = {'butterworth', 'bessel',
        #                     'chevy1', 'chevy2', 'cauer', 'legendre'}

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
    """
        if ftype not in self.filter_types:
            raise InvalidFilterError(
                ftype, f"'{ftype}' is not an available filter. Check docs for supported filters")

        if Ap > As:
            raise ValueError(
                "Pass band attenuation must be lower than stop band")

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

    def get_ba(self):
        """
        Returns
        -------
            b,a: Numerator and denominator coefficients of the filter transfer function
        """
        return self.b, self.a

    def get_zpk(self, parameter_list):
        raise NotImplementedError

    # @abstractmethod
    # def get_filter_stages(self, parameter_list):
    #     raise NotImplementedError

    #TODO
    # def get_stageQ(self, parameter_list):
    #     pass

    @abstractmethod
    def compute_order(self):
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
        >>>     plt.fill(s[0],s[s1],lw=0,'0.8',color='orange) #Set line-width=0
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
            print(self.wp[0], self.wp[1])
            pLx = [[x[0], fpL, fpL, x[0]]]
            pLy = [[np.max(y), np.max(y), self.Ap, self.Ap]]
            pL = pLx + pLy

            #Stop band
            fsL = np.divide(self.ws[0], 2*np.pi)
            fsR = np.divide(self.ws[1], 2*np.pi)
            print(self.ws)
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
    # @abstractmethod
    # def compute_gdelay(self, parameter_list):
    #     raise NotImplementedError

    # @abstractmethod
    # def compute_step_response(self, parameter_list):
    #     pass

    # @abstractmethod
    # def compute_impulse_response(self, parameter_list):
    #     pass

    def plot_mag(self, dstencils=True, show=False, sc='orange', lc=None):
        """
        Plot the magnitude bode plot of the specified filter

        Parameters
        ----------
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
        sys = signal.TransferFunction(self.b, self.a)
        w, mag, pha = signal.bode(sys)
        stencils = self.get_stencils(np.divide(w, 2*np.pi), -mag)

        if lc:
            plt.semilogx(np.divide(w, 2*np.pi), -mag, color=lc)
        else:
            plt.semilogx(np.divide(w, 2*np.pi), -mag)

        if dstencils:
            for s in stencils:
                plt.fill(s[0], s[1], '0.8', lw=0, color=sc)  # Set line-

        if show:
            print("Hello")
            plt.show()

    def plot_pha(self, show=False, sc='orange', lc=None):
        """
        Plot the magnitude bode plot of the specified filter

        Parameters
        ----------
        stencils: boolean
            True by default to show filter specifications
        show: boolean
            False by default. Helpful to stack plots. 
            Wether or not to perform plt.show(). 
        sc: str
            Choosen color to display stencil
        lc: str
            Choosen line color. If left blank matplotlib will automatically pick a color
        """
        self.sys = signal.TransferFunction(self.b, self.a)
        self.w, self.mag, self.pha = signal.bode(self.sys)
        if lc:
            plt.semilogx(np.divide(self.w, 2*np.pi), self.pha, color=lc)
        else:
            plt.semilogx(np.divide(self.w, 2*np.pi), self.pha)

        if show:
            print("Hello")
            plt.show()

    def plot_zp(self, zc='ro', pc='xb'):
        pass

    # @abstractmethod
    # def plot_step_response(self, parameter_list):
    #     raise NotImplementedError

    # @abstractmethod
    # def plot_impulse_response(self, parameter_list):
    #     raise NotImplementedError

    # @abstractmethod
    # def plot_group_delay(self, parameter_list):
    #     raise NotImplementedError


class Butterworth(AnalogFilter):
    def __init__(self, ftype,  wp, ws, Ap, As, rp=0, k=0, N=None):
        print(f"received k: {type(k)}")
        super().__init__(ftype,  wp, ws, Ap, As, k=k, N=N)

        self.compute_order()
        self.wcryt = self.compute_ba()
        self.sys = signal.TransferFunction(self.b, self.a)
        # REMEMBER! 'mag' is given as GAIN. '-mag' means attenuation
        self.w, self.mag, self.pha = signal.bode(self.sys)
        # self.compute_zpk()

    def compute_order(self):
        """
        Compute the minimum order that satisfies the requierements
        """
        if self.N is None:
            self.N, self.Wn = signal.buttord(
                self.wp, self.ws, self.Ap, self.As, analog=True)

    def compute_ba(self):
        # Compute numerator and denominator polynomials
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        print(f'frecuencia critica {self.wcryt}')
        self.b, self.a = signal.butter(
            self.N, self.wcryt, self.ftype, analog=True, output='ba')

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


print(type(0.4))
# a = Butterworth("lowpass", 1E3, 4E3, 3, 40, k=0)
# b = Butterworth("lowpass", 1E3, 4E3, 3, 40, k=0.4)
# c = Butterworth("lowpass", 1E3, 4E3, 3, 40, k=0.9)
plt.grid(axis='both',which='both')
b = Butterworth('bandpass',[7E3, 20E3], [5E3, 25E3], 20, 50)
b.plot_mag(dstencils=True, sc='yellow', lc='green')

# a.plot_mag(dstencils=True, sc='yellow', lc='green')
# b.plot_mag(dstencils=True, sc='yellow', lc='green')
# c.plot_mag(dstencils=True, sc='yellow', lc='green')
plt.show()
# a.plot_pha(show=True)


# sys = signal.TransferFunction(a.b, a.a)
# w, mag, pha = signal.bode(sys)
# stencils = a.get_stencils(np.divide(w, 2*np.pi), -mag)
# plt.semilogx(np.divide(w, 2*np.pi), -mag)

# for s in stencils:
#    plt.fill(s[0], s[1], '0.8', lw=0, color='orange')  # Set line-
# plt.show()