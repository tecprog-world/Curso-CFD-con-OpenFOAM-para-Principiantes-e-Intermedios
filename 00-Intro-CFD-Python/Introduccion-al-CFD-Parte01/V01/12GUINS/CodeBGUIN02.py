# -*- coding: utf-8 -*-

import sys
import numpy as np
import matplotlib.pyplot as plt
from IPython.core.display import clear_output
from PyQt5.QtWidgets import QDialog, QApplication
from GUIN01 import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.push02Graficar.clicked.connect(self.dispsolvegraphic)
        self.show()
    def dispsolvegraphic(self):
        nx = int(self.ui.line01nx.text())
        x = float(self.ui.line02x.text())
        dx = x/(nx-1)
        nt = int(self.ui.line03nt.text())
        dt = float(self.ui.line04dt.text())
        c  = float(self.ui.line05c.text())

        ue = float(self.ui.line06u.text())
        x1 = float(self.ui.line07x1.text())
        x2 = float(self.ui.line08x2.text())


        # Ecuación de Convección - Función sombrero
        print("Ecuación de convección - Función sombrero")
        u = np.ones(nx)
        u[int(x1/dx) : int(x2/dx)] = ue #Y

        #plt.plot(np.linspace(0,2,nx), u)
        #plt.show()

        #Dominio01
        x1 = np.linspace(0,x, nx)
        print("Dominio01 x1:")
        print(x1)


        #Rango01
        print("Rango01 u:")
        print(u)

        y1 = u
        print("Rango01 y1:")
        print(y1)

        #Grafico
        plt.subplot(2,1,1)
        plt.plot(x1, y1, 'o-')
        plt.title('Resolviendo la ecuación de convección')
        plt.ylabel('Altura - Eje Y1')

        self.ui.labelResponse01.setText("uini: " + str(y1))



        # Ecuación de Convección - Discretizada
        print("Ecuación de convección - Discretizada")
        un = np.ones(nx)

        for n in range(nt):
            un[:] = u[:]
            for i in range(1,nx):
                u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])



        # Visualización numérica de resultados
        #print("-----------------------")
        #print(nx)
        #print(u)
        #plt.plot(np.linspace(0,x,nx),u)

        #Dominio02
        print("Dominio02 x2:")
        x2 = np.linspace(0,x,nx)
        print(x2)

        #Rango02
        print("Rango02 u:")
        print(u)
        y2 = u
        print("Rango02 y2:")
        print(y2)


        #Grafico
        #plt.subplot(2,1,1)
        #plt.plot(x1, y1, 'o-')
        #plt.title('Resolviendo la ecuación de convección')
        #plt.ylabel('Altura - Eje Y1')

        plt.subplot(2,1,2)
        plt.plot(x2, y2, '.-')
        plt.xlabel('distancia (m)')
        plt.ylabel('Altura - Eje Y2')

        plt.show()






        #self.ui.labelResponse01.setText("uini: " + str(y1))
        self.ui.labelResponse02.setText("ufin : " + str(y2))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
