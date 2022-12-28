import numpy as np
import matplotlib.pyplot as plt

x_values = np.arange(1, 1001)
y_values = x_values**2

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c="red", s=10)

ax.set_title("square")
ax.set_xlabel("value")
ax.set_ylabel("square")
# 设置坐标值取值范围
ax.axis([0, 1100, 0, 1100000])

plt.savefig("scatter_squares.png", bbox_inches="tight")
plt.show()