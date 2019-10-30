import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

mu, sigma = 30*10**3, 1*10**3 # mean and standard deviation
s = np.random.normal(mu, sigma, 5000)
plt.xlabel("Frecuancia [Hz]")
count, bins, ignored = plt.hist(s, 20, density=True)
#plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')
plt.show()