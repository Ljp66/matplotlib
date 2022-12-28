import numpy as np
import matplotlib.pyplot as plt

N = 400
t = np.linspace(0, 2*np.pi, N)
r = 0.5 + np.cos(t)
x, y = r * np.cos(t), r * np.sin(t)

fig, ax = plt.subplots()
ax.plot(x, y, "k")
ax.set(aspect=1)
fig.savefig("curve_error_band.png")
plt.show()