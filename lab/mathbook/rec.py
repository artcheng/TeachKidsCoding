import numpy as np
import matplotlib.pyplot as plt

N = 36

xs=0.0
x = []
y = []
colors = []
for w in range(2, N):
    if N%w != 0:
       continue

    ys = 0
    for i in range(0, N):
        if i%w == 0:
            ys = ys + 1
        x.append(xs + i%w)
        y.append(ys)

        if w == 6:
            colors.append('r')
        else:
            colors.append('C0')
    xs = xs + w + 2



area = np.pi * 2**2  # 0 to 15 point radii

plt.scatter(x, y, c=colors, s=area, alpha=0.9)

plt.axis('equal')
plt.axis('off')
plt.show()
