import matplotlib.pyplot as plt
import numpy as np
#plt.rcParams['axes.facecolor'] = 'black'
data = np.load('data.npy', allow_pickle=True)

plt.scatter(data[:, 2], data[:, 3], c=data[:, 1], cmap='cool')

plt.axis('equal')
plt.show()
