# Biblliotecas
import matplotlib.pyplot as plt
import numpy as np

a = np.array([2, 3, 1])
b = np.array([0, 5, 4])
#a = np.array([3, 5, -7])
#b = np.array([2, -6, 4])

# i - j + k
resultado = np.cross(a, b)
print(resultado)

fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.xaxis.set_label_text('x', color = 'b')
ax.yaxis.set_label_text('y', color = 'b')
ax.zaxis.set_label_text('z', color = 'b')

ax.set_xlim([-1, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([0, 10])

ax.quiver(0, 0, 0, a[0], a[1], a[2], label = 'a')
ax.quiver(0, 0, 0, b[0], b[1], b[2], color = 'g', label = 'b')
ax.quiver(0, 0, 0, resultado[0], resultado[1],resultado[2], color = 'r', label = 'a × b')

plt.legend()
plt.show()