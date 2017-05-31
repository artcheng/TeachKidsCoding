import numpy as np
import matplotlib.pyplot as plt
import math
from random import randint
from matplotlib.text import TextPath


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)

area = np.pi * (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)


for i in range(0, N):
    num = math.sqrt(area[i]/np.pi)/30
    fs = int(num*13)

    plt.annotate( str(int(area[i])), xy=(x[i], y[i]), fontsize= fs, color='white')
plt.show()
plt.axis('off')
