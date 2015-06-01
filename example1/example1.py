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


plt.plot(x_values, normalised_data)