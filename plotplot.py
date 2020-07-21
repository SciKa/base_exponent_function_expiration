import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_zlabel('real domain')
ax.set_ylabel('imaginarly domain')
ax.set_xlabel('real range')

x_space = np.linspace(-100,+100,10000)
i_space = np.array([])
r_space = np.array([])
a = 5
for p in range(len(x_space)):
    if p == int(len(x_space)/2):
        i = np.inf
        r = np.inf
    elif x_space[p] < 0:
        i = (-x_space[p])**a * np.sin(np.pi * a)
        r = (-x_space[p])**a * np.cos(np.pi * a)
    elif x_space[p] > 0:
        i = 0
        r = x_space[p]**a

    i_space = np.append(i_space, [i])
    r_space = np.append(r_space, [r])
ax.plot(x_space,i_space,r_space,label="a=5")


plt.legend()
plt.show()
