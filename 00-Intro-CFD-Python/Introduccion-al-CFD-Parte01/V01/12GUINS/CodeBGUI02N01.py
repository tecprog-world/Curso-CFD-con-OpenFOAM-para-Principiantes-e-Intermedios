import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QDialog, QApplication
from GUIN02 import *
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.radio01lineal.toggled.connect(self.conveccion1d)
        self.ui.radio02nolineal.toggled.connect(self.conveccion1d)
        self.show()

    def conveccion1d(self):
        fare = 0
        if self.ui.radio01lineal.isChecked()==True:
            #Definimos para convección lineal
            print("Se hizo clic en conveccion lineal")
        if self.ui.radio02nolineal.isChecked()==True:
            #Definimos para convección no lineal
            print("Se hizo clic en conveccion no lineal")
        self.ui.labelResponse01.setText("Respuesta aquí")
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
