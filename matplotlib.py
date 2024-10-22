import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.ticker import MultipleLocator

# 定义x和y坐标
x = [0, 0, -32.0, 32.0, 23.0, 22.0, -23.0, -24.0]
y = [32.0, -32.1, 0, 0, 23.0, -23.0, -22.0, 24.0]

# 设置坐标轴范围
plt.xlim(-40, 40)
plt.ylim(-40, 40)

# 设置主刻度间隔为10
ax = plt.gca()  # 获取当前轴
ax.xaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_major_locator(MultipleLocator(10))

# 设置副刻度间隔为1
ax.xaxis.set_minor_locator(MultipleLocator(1))
ax.yaxis.set_minor_locator(MultipleLocator(1))

# 隐藏主刻度和副刻度的线
ax.tick_params(axis='both', which='both', length=0)

# 隐藏主刻度和副刻度的标签
ax.tick_params(axis='x', which='both', labelbottom=False)
ax.tick_params(axis='y', which='both', labelleft=False)

# 添加网格线
plt.grid(True, which='both', linestyle='-', linewidth=0.5)

# 添加x轴和y轴
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)

# 绘制一个以原点为中心，半径为32.2的圆
circle = Circle((0, 0), 32.2, edgecolor='blue', facecolor='none', linewidth=1)
ax.add_patch(circle)

# 绘制点
ax.scatter(x, y, color='red',s=10)

# 设置图形的比例为等比例，确保圆看起来是圆而不是椭圆
ax.set_aspect('equal')

# 显示图形
plt.show()