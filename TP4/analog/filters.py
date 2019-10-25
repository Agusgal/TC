import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

from core import AnalogFilter
from cusfunc import maprange


class Butterworth(AnalogFilter):
    def __init__(self, ftype,  wp, ws, Ap, As, gain=1, rp=0, k=0, N=None):
        print(f"received k: {type(k)}")
        super().__init__(ftype,  wp, ws, Ap, As, k=k, N=N)

    def compute_order(self):
        """
        Compute the minimum order that satisfies the requierements
        """
        if self.N is None:
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


# b = Butterworth("lowpass", 1E3, 4E3, 3, 40, k=0)
# b = Butterworth("lowpass", 10E3, 40E3, 3, 40, k=0)

# b = Butterworth("highpass", 4E3, 1E3, 3, 40, k=0.4)
# b = Butterworth("lowpass", 1E3, 4E3, 3, 40, k=0.9)
# b = Butterworth("lowpass", 10E3*2*np.pi, 40E3*2*np.pi, 3, 40, k=0.9)
# b = Butterworth('bandpass', [7E3, 20E3], [5E3, 25E3], 20, 50) #Can't compute step response
# b = Butterworth('bandstop',[1E3, 30E3], [4E3, 15E3], 20, 50)
# b = Butterworth('bandpass', [10E3, 15E3],[5E3, 25E3], 20, 50)
# print(b.get_order())
# b.plot_mag(show=True, dstencils=True, sc='orange', lc='green')
# b.plot_zp(show=True)
# plt.title(f"step order: {b.get_order()}")
# b.plot_step_response(show=True)
# plt.title(f"impulse order: {b.get_order()}")
# b.plot_impulse_response(show=True,lc='green',name='hola')
# # b.plot_pha(show=True)
# plt.title("group delay")
# b.plot_group_delay(show=True)
# # a.plot_mag(dstencils=True, sc='yellow', lc='green')
# plt.title(f"Butterworth mag {b.get_order()}")
plt.title(f"Butterworth mag")
for i in np.linspace(0, 1, 10):
    b = Butterworth("highpass", 40E3*2*np.pi, 10E3*2*np.pi, 3, 40, k=i)
    # c = Butterworth("highpass", 40E3*2*np.pi,10E3*2*np.pi, 3, 40, N=i)
    b.plot_mag(dstencils=True, sc='blue', name=f'k: {i}')
    # c.plot_mag(dstencils=True, sc='black',name=f'N: {i}')
plt.grid(axis='both', which='both')
plt.legend()
plt.show()
# c.plot_mag(dstencils=True, sc='yellow', lc='green')
# plt.show()
# a.plot_pha(show=True)
