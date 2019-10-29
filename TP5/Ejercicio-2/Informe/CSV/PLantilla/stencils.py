import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def get_stencils(ftype,ws,wp,Ap,As,x, y):
        """
        Get the poligons to plot your requirements on screen.
        The function filter type aware.

        Parameters
        ----------
        ws: array_like
            Stop-band frequency
        wp: array_like
            Pass-band frequency
        Ap: float
            pass band max attenuation
        As: float
            stop band min attenuation  
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
#        >>> stencils = filter.get_stencils(x,y)
#        >>> for s in stencils:
#        >>>     plt.fill(s[0],s[s1],lw=0,'0.8',color='orange) #Set line-width=0
#        >>> plt.show()
        """
        if ftype == 'lowpass':
            #Pass  band (left side of bode plot)
            p1x = [[x[0],  np.divide(wp,1),
                    np.divide(wp,1),   x[0]]]
            p1y = [[Ap, Ap, np.max(y), np.max(y)]]
            p = p1x + p1y

            #Stop  band (right side of bode plot)
            s2x = [[np.divide(ws,1), x[-1],
                    x[-1],  np.divide(ws,1)]]
            s2y = [[As, As, 0, 0]]
            s = s2x + s2y

            stencils = [p]+[s]
            return stencils
        elif ftype == 'highpass':
            fs = np.divide(ws,1)
            s1x = [[x[0], fs, fs, x[0]]]
            s1y = [[np.min(y), np.min(y), As, As]]
            s = s1x + s1y

            fp = np.divide(wp,1)
            p2x = [[fp, x[-1], x[-1], fp]]
            p2y = [[Ap, Ap, np.max(y), np.max(y)]]
            p = p2x + p2y
            stencils = [p] + [s]
            return stencils
        elif ftype == 'bandpass':
            #Left stop band
            fsL = np.divide(ws[0],1)
            aLx = [[x[0], fsL, fsL, x[0]]]
            aLy = [[0, 0, As, As]]
            aL = aLx + aLy

            #Pass band
            fpL = np.divide(wp[0],1)
            fpR = np.divide(wp[1],1)
            px = [[fpL, fpR, fpR, fpL]]
            py = [[Ap, Ap, max(y), max(y)]]
            pband = px + py

            #Right stop band
            fsR = np.divide(ws[1],1)
            aRx = [[fsR, x[-1], x[-1], fsR]]
            aRy = [[As, As, 0, 0]]
            aR = aRx + aRy

            stencils = [aL] + [aR] + [pband]
            return stencils
        elif ftype == 'bandstop':
            #Left pass band
            fpL = np.divide(wp[0],1)
            (wp[0], wp[1])
            pLx = [[x[0], fpL, fpL, x[0]]]
            pLy = [[np.max(y), np.max(y), Ap, Ap]]
            pL = pLx + pLy

            #Stop band
            fsL = np.divide(ws[0],1)
            fsR = np.divide(ws[1],1)
            sx = [[fsL, fsR, fsR, fsL]]
            sy = [[0, 0, As, As]]
            sband = sx + sy

            #Right pass band
            fpR = np.divide(wp[1],1)
            pRx = [[fpR, x[-1], x[-1], fpR]]
            pRy = [[np.max(y), np.max(y), Ap, Ap]]
            pR = pRx + pRy

            stencils = [sband]+[pL] + [pR]  # + [sband]
            return stencils



df = pd.read_csv('BodeRauch.csv')
H = np.asarray(df['MAG'])+2.8
f = np.asarray(df['Frequency'])
plt.semilogx(f,-H)
stencils = get_stencils("bandpass",[2600,290000],[26000,29000],3,40,f,-H)
for s in stencils:
    plt.fill(s[0], s[1],'0.8',lw=0,color='orange')  #Set line-width=0
plt.show()