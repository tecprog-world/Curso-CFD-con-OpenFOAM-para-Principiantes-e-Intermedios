import numpy as np
import matplotlib.pyplot as plt

#Dominio
x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

#Rango
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

#Subgrafico01
plt.subplot(2, 1, 1)
plt.plot(x1, y1, 'o-')
plt.title('Una ventana con 02 dibujos')
plt.ylabel('Altura - Eje Y1')

plt.subplot(2, 1, 2)
plt.plot(x2, y2, '.-')
plt.xlabel('distancia (m)')
plt.ylabel('Altura - Eje Y2')

plt.show()
