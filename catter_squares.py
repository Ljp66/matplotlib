import matplotlib
import matplotlib.pyplot as plt

SimSun = matplotlib.font_manager.FontProperties(fname="SimSun.ttf")

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=200)

ax.set_title("平方数", fontsize=12, fontproperties=SimSun)
ax.set_xlabel("值", fontsize=12, fontproperties=SimSun)
ax.set_ylabel("值的平方", fontsize=12, fontproperties=SimSun)

ax.tick_params(axis="both", which="major", labelsize=14)

fig.savefig("catter_squares.png",dpi=200)
plt.show()