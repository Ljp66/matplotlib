import matplotlib
import matplotlib.pyplot as plt

# 设置中文
SimSun = matplotlib.font_manager.FontProperties(fname="SimSun.ttf")

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数",fontsize=12,fontproperties=SimSun)
ax.set_xlabel("值",fontsize=12,fontproperties=SimSun)
ax.set_ylabel("值的平方",fontsize=12,fontproperties=SimSun)
# 设置刻度标记的大小
ax.tick_params(axis="both", labelsize=14)
# 显示坐标表格
ax.grid()

fig.savefig("mpl_squares.png")
plt.show()