import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.arange(-10, 11, 1)
y = np.arange(-10, 11, 1)
X, Y = np.meshgrid(x, y)


def func1(x, y):
    return np.sqrt(np.abs(x)) + np.sqrt(np.abs(y))


def func2(x, y):
    return x ** 2 + y ** 2


def func3(x, y):
    return 2 * x + 3 * y


def func4(x, y):
    return x ** 2 - y ** 2


def func5(x, y):
    return 2 + 2 * x + 2 * y - x ** 2 - y ** 2

fig, ax = plt.subplots(2, 3, figsize=(15, 10), subplot_kw={'projection': '3d'}, sharex=True, sharey=True)
ax = ax.flatten()

Z1 = func1(X, Y)
Z2 = func2(X, Y)
Z3 = func3(X, Y)
Z4 = func4(X, Y)
Z5 = func5(X, Y)

ax[0].plot_surface(X, Y, Z1, cmap='pink')
ax[0].set_title('z = x^0.25 + y^0.25')

ax[1].plot_surface(X, Y, Z2, cmap='PuRd')
ax[1].set_title('z = x^2 + y^2')

ax[2].plot_surface(X, Y, Z3, cmap='OrRd')
ax[2].set_title('Z = 2x + 3y')

ax[3].plot_surface(X, Y, Z4, cmap='spring')
ax[3].set_title('z = x^2 - y^2')

ax[4].plot_surface(X, Y, Z5, cmap='cool')
ax[4].set_title('z = 2 + 2x + 2y - x^2 - y^2')
plt.show()