from numpy import arange, sin

import Factorial
import Telecomunication
import random
import cycle
import matplotlib.pyplot as plt
from numpy import *


size = 100



location = [[0 for j in range(size)] for i in range(size)]  # квадратная область 100*100

population = [[random.randint(1, 10) for j in range(size)] for i in range(size)]  # хранит плотность населения

situation = Telecomunication.inputLocation(location)  # хранит координаты вышек связи

print(Telecomunication.countPopulation(population, situation))

size = 15

area = [[0 for j in range(size)] for i in range(size)]

area[2][1] = 555
area[2][12] = 555
area[4][12] = 555
area[4][14] = 555
area[9][14] = 555
area[9][1] = 555
area[2][1] = 555


#Telecomunication.output(area)

#print(cycle.findCoordinats(area))


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

# Load a numpy record array from yahoo csv data with fields date, open, close,
# volume, adj_close from the mpl-data/example directory. The record array
# stores the date as an np.datetime64 with a day unit ('D') in the date column.
price_data = (cbook.get_sample_data('goog.npz', np_load=True)['price_data'].view(np.recarray))
price_data = price_data[-250:]  # get the most recent 250 trading days

delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# Marker size in units of points^2
volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

fig, ax = plt.subplots()
ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

ax.set_xlabel(r'$\Delta_i$', fontsize=15)
ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()