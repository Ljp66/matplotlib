from matplotlib import pyplot as plt


# 绘图数据
x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 24, 22, 18, 15]

# 设置图片大小
fig = plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 设置坐标轴刻度
plt.xticks(x)
# plt.xticks(range(2, 25))
# xtick_labels = [i/2 for i in range(4, 49)]
# plt.xticks(xtick_labels)
plt.yticks(range(min(y), max(y)+1))

# 保存图片
# plt.savefig("./sig_size.svg")

# 展示图片
plt.show()
