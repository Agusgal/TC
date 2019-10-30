import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from core import AnalogFilter
from core import Cell
from cusfunc import maprange


class Butterworth(AnalogFilter):
    def __init__(self, ftype,  wp, ws, Ap, As, gain=6, rp=0, k=0, N=None):
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
        super().__init__(ftype,  wp, ws, Ap, As, k=k, N=N)

    def compute_order(self):
        """
        Must return optimal filter order
        """
        self.N, self.Wn = signal.buttord(
            self.wp, self.ws, self.Ap, self.As, analog=True)

    def compute_ba(self):
        """
        Calculates transfer function coefficients

        Stores 
        """
        # Compute numerator and denominator polynomials
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        return signal.butter(
            self.N, self.wcryt, self.ftype, analog=True, output='ba')

    def compute_zpk(self):
        """
        Computes zeros, poles and gain of a determined filter

        Returns
        -------
        z,p,k: array_like
            zeros, poles and gain
        """
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        return signal.butter(
            self.N, self.wcryt, self.ftype, analog=True, output='zpk')


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
            # # Compute maximum frequency allowed that still might meet requirements
            # wcstop = self.ws * (10**(self.As/10) - 1)**(-1/(2*self.N))
            # # Compute minimum allowed frequency that still might meet requirements
            # wcpass = self.wp * (10**(self.Ap/10) - 1)**(-1/(2*self.N))


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
            return maprange([0, 1], [wcpass, wcstop], k)

        elif self.ftype == 'bandpass':
            return self.Wn
        elif self.ftype == 'bandstop':
            return self.Wn
            pass


class Chebyshev1(AnalogFilter):
    def __init__(self, ftype,  wp, ws, Ap, As, gain=1, rp=0, k=0, N=None):
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
        super().__init__(ftype,  wp, ws, Ap, As, rp=Ap, k=k, N=N)

    def compute_order(self):
        """
        Must return optimal filter order
        """
        self.N, self.Wn = signal.cheb1ord(
            self.wp, self.ws, self.Ap, self.As, analog=True)

    def compute_ba(self):
        """
        Calculates transfer function coefficients

        Stores 
        """
        # Compute numerator and denominator polynomials
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        return signal.cheby1(
            self.N, self.rp, self.wcryt, self.ftype, analog=True, output='ba')

    def compute_zpk(self):
        """
        Computes zeros, poles and gain of a determined filter

        Returns
        -------
        z,p,k: array_like
            zeros, poles and gain
        """
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        return signal.butter(self.N, self.wcryt, self.ftype, analog=True, output='zpk')

    def compute_filter_stages(self):
        """
        Split the obtained filter into second and first order units
        
        Returns
        -------
            den: array-like
                Array of shape (n-sections,3) containing the denominator coefficients of the units
            num: array-like
                Array of shape (n-sections,3) containing the numerator coefficients of the units
        """
        sos = signal.butter(self.N, self.wcryt, self.ftype,
                            analog=True, output='sos')
        num = sos[:, :3]
        den = sos[:, 3:]
        return den, num

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
            wcstop = self.ws* np.cosh(np.arccosh(1 / np.sqrt(np.power(10, self.Ap/10) - 1)) / self.N)
            # Compute minimum allowed frequency that still might meet requirements
            wcpass = self.wp * np.cosh(np.arccosh(1 / np.sqrt(np.power(10, self.Ap/10) - 1)) / self.N)
            print(f"wcstop:{wcstop}")
            print(f"wcpass:{wcpass}")

            return maprange([0, 1], [wcpass, wcstop], k)
        elif self.ftype == 'highpass':
            # Compute maximum frequency allowed that still might meet requirements
            wcstop = self.ws * (10**(self.As/10) - 1)**(1/(2*self.N))
            # Compute minimum allowed frequency that still might meet requirements
            wcpass = self.wp * (10**(self.Ap/10) - 1)**(1/(2*self.N))
            return maprange([0, 1], [wcpass, wcstop], k)

        elif self.ftype == 'bandpass':
            return self.Wn
        elif self.ftype == 'bandstop':
            return self.Wn
            pass


class Chebyshev2(AnalogFilter):
    def __init__(self, ftype,  wp, ws, Ap, As, gain=1, rp=0, k=0, N=None):
        """
        Chebyshev 2 analog filter
        
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
        super().__init__(ftype,  wp, ws, Ap, As, rp=Ap, k=k, N=N)

    def compute_order(self):
        """
        Must return optimal filter order
        """
        self.N, self.Wn = signal.cheb2ord(
            self.wp, self.ws, self.Ap, self.As, analog=True)

    def compute_ba(self):
        """
        Calculates transfer function coefficients

        Stores 
        """
        # Compute numerator and denominator polynomials
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        return signal.cheby2(
            self.N, self.rp, self.wcryt, self.ftype, analog=True, output='ba')

    def compute_zpk(self):
        """
        Computes zeros, poles and gain of a determined filter

        Returns
        -------
        z,p,k: array_like
            zeros, poles and gain
        """
        self.wcryt = self.get_critical_w(self.k)  # Compute cut-off frequencies
        return signal.butter(self.N, self.wcryt, self.ftype, analog=True, output='zpk')

    def compute_filter_stages(self):
        """
        Split the obtained filter into second and first order units
        
        Returns
        -------
            den: array-like
                Array of shape (n-sections,3) containing the denominator coefficients of the units
            num: array-like
                Array of shape (n-sections,3) containing the numerator coefficients of the units
        """
        sos = signal.butter(self.N, self.wcryt, self.ftype,
                            analog=True, output='sos')
        num = sos[:, :3]
        den = sos[:, 3:]
        return den, num

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
            wcstop = self.ws * np.cosh(np.cosh(1 / (np.sqrt(np.power(10, -self.As/10) - 1))) / self.N)
            # Compute minimum allowed frequency that still might meet requirements
            wcpass = self.wp * np.cosh(np.arccosh(1 / np.sqrt(np.power(10, self.Ap/10) - 1)) / self.N)
            print(f"wcstop:{wcstop}")
            print(f"wcpass:{wcpass}")

            return maprange([0, 1], [wcpass, wcstop], k)
        elif self.ftype == 'highpass':
            # Compute maximum frequency allowed that still might meet requirements
            wcstop = self.ws * (10**(self.As/10) - 1)**(1/(2*self.N))
            # Compute minimum allowed frequency that still might meet requirements
            wcpass = self.wp * (10**(self.Ap/10) - 1)**(1/(2*self.N))
            return maprange([0, 1], [wcpass, wcstop], k)

        elif self.ftype == 'bandpass':
            return self.Wn
        elif self.ftype == 'bandstop':
            return self.Wn
            pass

# plt.grid(axis='both', which='both')
# for i in np.linspace(0, 1, 1):
    # b = Chebyshev1("highpass", 40E3, 10E3, 3, 40,rp=3, k=i)
    # b = Butterworth("lowpass", 20E3, 50E3, 3, 40, k=i)
    # b.plot_mag(name=f'{i}')
# b = Chebyshev1("bandpass", [10E3,15E3], [5E3,20E3], 10, 40, rp=3, k=0)
# b1= Chebyshev1("highpass", 40E3, 20E3, 10, 40,rp=3, k=0)
# b2 = Chebyshev1("highpass", 40E3, 20E3, 10, 40,N=5,rp=3, k=0)
# b1.plot_mag()
# b2.plot_mag()

b = Butterworth("lowpass", 20E3, 50E3, 3, 40, k=0)
plt.title(f"Magnintud Butterworth orden {b.N}")
# mag = 0
# for s in b.stages:
#     mag += s.mag
# plt.semilogx(b.w,-mag+b.kZP,label="sumada")
b.plot_mag(show=True)

plt.title("Polos y ceros")
b.plot_zp(show=True)


# try:
#     b = Butterworth("highpass", 10E3,20E3, 3, 40)
# except ValueError as e:
#     print(e)
# b.plot_mag(show=True)
# print(b.compute_filter_stages())

# plt.title("Polos y ceros")
# b.plot_zp(show=True)
# c = Butterworth("highpass", 40E3*2*np.pi,10E3*2*np.pi, 3, 40, N=i)
# c.plot_mag(dstencils=True, sc='black',name=f'N: {i}')
# c.plot_mag(dstencils=True, sc='yellow', lc='green')
# plt.show()
# a.plot_pha(show=True)
# https://dsp.stackexchange.com/questions/1966/how-can-i-break-a-filter-down-into-second-order-sections
# https://gist.github.com/endolith/c80f9e6bf3b407c2f567
# https://d1.amobbs.com/bbs_upload782111/files_32/ourdev_573166.pdf
# http://www.matheonics.com/Tutorials/Specification.html
# http://www.matheonics.com/Tutorials/Butterworth.html#Paragraph_3.1
