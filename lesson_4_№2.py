import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(16, 9))

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

values = np.random.normal(0, 10, 100)
ax1.hist(values, 50)
ax1.grid()
ax1.set_title('N = 100')

values = np.random.normal(0, 10, 1000)
ax2.hist(values, 50)
ax2.grid()
ax2.set_title('N = 1000')

values = np.random.normal(0, 10, 10000)
ax3.hist(values, 50)
ax3.grid()
ax3.set_title('N = 10000')

values = np.random.normal(0, 10, 100000)
ax4.hist(values, 50)
ax4.grid()
ax4.set_title('N = 100000')

plt.tight_layout()

plt.show()