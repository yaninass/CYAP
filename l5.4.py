#coding: utf-8
import numpy as np
from matplotlib import pyplot as plt

x = 1.21


def func(a):
    return np.arcsin(x / 3) + 1.2 * a


a_val = np.arange(3.5, 25.6, 1.5)
f_val = func(a_val)
for a, fx in zip(a_val, f_val):
    print(f"x = {a:.2f}, f(x) = {fx:.4f}")
max_v = np.max(f_val)
min_v = np.min(f_val)
mean_v = np.mean(f_val)
num = len(f_val)
print(max_v)
print(min_v)
print(mean_v)
print(num)
sorted = np.sort(f_val)[::-1]
print(sorted)
plt.plot(a_val, f_val, marker='o', label='f(x)')
plt.axhline(y=mean_v, color='r', linestyle='--', label='Mean Line')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('График функции f(x) и график прямой')
plt.legend()
plt.show()