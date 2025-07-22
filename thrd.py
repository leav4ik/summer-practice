import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    term = np.abs(100 - np.sqrt(x1**2 + x2**2) / np.pi)
    return -0.0001 * ((np.abs(np.sin(x1) * np.sin(x2) * np.exp(term)) + 1)**0.01)

x10, x20 = 1.3491, 1.3491
x1_range = [-2.0, 2.0]
x2_range = [-2.0, 2.0]
step = 0.05

x1 = np.arange(x1_range[0], x1_range[1] + step, step)
x2 = np.arange(x2_range[0], x2_range[1] + step, step)
X1, X2 = np.meshgrid(x1, x2)
Y = f(X1, X2)

fig = plt.figure(figsize=(14, 10))
fig.suptitle(f'Графики функции f(x1, x2)\nТестовая точка: ({x10}, {x20}), f({x10}, {x20}) = {f(x10, x20):.6f}', fontsize=14)

ax1 = fig.add_subplot(221, projection='3d')
surf1 = ax1.plot_surface(X1, X2, Y, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.set_zlabel('y = f(x1, x2)')
ax1.set_title('3D поверхность (изометрический вид)')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X1, X2, Y, cmap=cm.coolwarm, linewidth=0, antialiased=False)
ax2.view_init(elev=90, azim=-90)
ax2.set_xlabel('x1')
ax2.set_ylabel('x2')
ax2.set_zlabel('y = f(x1, x2)')
ax2.set_title('Вид сверху (проекция на XOY)')
fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

ax3 = fig.add_subplot(223)
y_x2_fixed = f(x1, x20)
ax3.plot(x1, y_x2_fixed)
ax3.set_xlabel('x1')
ax3.set_ylabel('y = f(x1, x2=const)')
ax3.set_title(f'График при x2 = {x20}')
ax3.grid(True)

ax4 = fig.add_subplot(224)
y_x1_fixed = f(x10, x2)
ax4.plot(x2, y_x1_fixed)
ax4.set_xlabel('x2')
ax4.set_ylabel('y = f(x1=const, x2)')
ax4.set_title(f'График при x1 = {x10}')
ax4.grid(True)

plt.tight_layout()
plt.show()
