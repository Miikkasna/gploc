import matplotlib.pyplot as plt
import numpy as np


data = np.load('positions.npy', allow_pickle=True)
start = 500
time, x, y = data[start:, 0], data[start:, 1], data[start:, 2]
time = (time - time.min()) / 50.0
weights = [0]
speed = 0
disp = 0
for i in range(1, x.shape[0]):
    disp = np.sqrt((x[i-1]-x[i])**2 + (y[i-1]-y[i])**2)
    speed = disp/(1.0/50.0)
    weights.append(speed)
weights = np.array(weights)
#weights = np.power(weights, 2)
data = np.vstack((time, weights, x/10, y/10)).T
weights = 1-(weights/weights.max()) # normalize

print(data.shape)
np.save('data.npy', data)
#plt.scatter(x, y, c=weights, alpha=1, s=5)
plt.plot(time, y)
plt.show()

