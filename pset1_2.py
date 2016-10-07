import numpy as np
import matplotlib.pyplot as plt

vals = [0., 0.9, 1., 1.1]
x = np.linspace(-10, 10, 50)
fig, ax = plt.subplots()
lines = []
for a in vals:
  y = np.cos(x) - a * x
  lines += ax.plot(x, y, label = 'alpha = ' +str(a))

plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show()
