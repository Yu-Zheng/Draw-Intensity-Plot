#!/usr/local/bin/python3
import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir("path")
file_name = 'file_name.txt'

data=np.loadtxt(file_name,delimiter=',')
plt.imshow(data, cmap='jet', interpolation='spline36')
plt.colorbar()
plt.title("Test")
plt.show()
