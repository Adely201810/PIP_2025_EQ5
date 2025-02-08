import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P07_Componente_HorizontallSlider.ui" # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(1)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1)
        self.selectorImagen.valueChanged.connect(self.CambiaValor)

        self.diccionarioDatos={
            0: (":/Logos/2547138d-151e-4651-ae8e-9c4830f6d1d4.jpeg",["gato","5 meses","estambre"]),

            1: (":/Logos/2547138d-151e-4651-ae8e-9c4830f6d1d4.jpeg", ["persona", "19 años", "armas"])

        }
        self.indice=0
        self.obtenerDato()


    #Area de los Slots
    def otenerDatos (self):
        nombre=self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        jugete = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_nombre.setText(edad)
        self.txt_nombre.setText(jugete)

    def CambiaValor(self):
        value=self.selectorImagen.value()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())