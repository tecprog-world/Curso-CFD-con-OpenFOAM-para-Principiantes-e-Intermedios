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
        u = np.ones(nx)
        print(u)
        u[int(x1/dx) : int(x2/dx)] = ue
        print(u)

        plt.plot(np.linspace(0,2,nx), u)
        plt.show()

        # Ecuación de Convección - Discretizada
        un = np.ones(nx)

        for n in range(nt):
            un[:] = u[:]
            for i in range(1,nx):
                u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])



        # Visualización numérica de resultados
        print("-----------------------")
        print(nx)
        print(u)
        plt.plot(np.linspace(0,x,nx),u)

        self.ui.labelResponse01.setText("nx: " + str(nx))
        self.ui.labelResponse02.setText("u : " + str(u))

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
