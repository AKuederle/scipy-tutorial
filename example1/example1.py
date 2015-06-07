# -*- coding: utf-8 -*-
"""
Created on Tue May 26 11:24:25 2015

@author: arne
"""

import numpy as np
import matplotlib.pyplot as plt

_, data = np.loadtxt("./spec_1", unpack=True) # loading the data

normalised_data = data/data.max() # normalising

x_values = np.linspace(100, 1000, 250)

normalised_data = normalised_data[19:] # cutting the data
x_values = x_values[19:]

fig = plt.figure("My awesome Plot", figsize=(8, 4), dpi=100)
ax = fig.add_subplot(111)
ax.plot(x_values, normalised_data)


ax.set_xlabel("wavenumber $\lambda$ [nm]")
ax.set_ylabel("intesity [V]")

ax.set_xlim(x_values.min(), x_values.max())
ax.set_ylim(0.8*normalised_data.min(), 1.1*normalised_data.max())

ax.grid(True)

fig.tight_layout()
fig.savefig("./example1.pdf")

fig.show()