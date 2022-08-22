import matplotlib.pyplot as plt
import numpy as np
#plt.rcParams['axes.facecolor'] = 'black'
data = np.load('data.npy', allow_pickle=True)
plt.plot(data[:, 2], data[:, 3], 'grey')

f_sim = 50
sample_rate = 1
noise = 0.15

data[:, 2] += np.random.normal(0, noise, data.shape[0])
data[:, 3] += np.random.normal(0, noise, data.shape[0])

data = data[::int(f_sim/sample_rate)]

np.save('tof_1hz.npy', data)

plt.scatter(data[:, 2], data[:, 3], marker='x', c='red')

plt.legend(['Real location', '1 Hz ToF data'])
plt.title('ToF')
plt.axis('equal')
plt.show()
