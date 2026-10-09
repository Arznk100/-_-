import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x_c = [0.218, 0.229, 0.237, 0.246, 0.255, 0.266, 0.273]
a = [0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31]
T = [1.54, 1.527, 1.53, 1.53, 1.53, 1.530, 1.53]

y = np.array([x_c[i]*T[i]**2 for i in range(len(x_c))])
x = np.array([a[i]**2 for i in range(len(a))])

plt.figure(figsize=(8,5), dpi=100)
plt.plot(x,y,'o', label='График зависимости $x_cT^2$ от $a^2$', color='blue', marker='o',markersize=3)
plt.xlabel('a^2')
plt.ylabel('T^2*x_c')
plt.grid(True)

k, b = np.polyfit(x, y, 1)
x_fit = np.linspace(min(x), max(x), 100)
y_fit = k * x_fit + b

plt.plot(x_fit, y_fit, 'r-', label=f'Линейная аппроксимация: y = {k:.2f}x + {b:.2f}')
plt.legend()   
plt.show()