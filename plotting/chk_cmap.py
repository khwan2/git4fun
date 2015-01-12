import pylab as pl
import numpy as np

import my_cmaps as mcd

dat = np.zeros([100,200])

for i in range(100):
    for j in range(200):
        dat[i,j] = np.sin(2. * pl.pi * i/50.) * np.cos(2. * pl.pi * j/100.)

my_cmap = mcd.get_cmap ('01')
# Define the gray levels, such that the data is within a small range around the zero.
my_levels = np.arange(50)
my_levels = (my_levels- 25)/5.

pl.contourf( dat, 50, cmap = my_cmap, levels = my_levels)
#pl.contourf( dat, cmap = pl.cm.Greens_r)
pl.colorbar()
pl.show()
