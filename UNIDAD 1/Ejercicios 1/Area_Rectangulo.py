import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Area_Rectangulo.ui"  # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_Calcular.clicked.connect(self.Calcular)

    # Área de los Slots
    def Calcular(self):
        try:
            largo = float(self.txt_Largo.text())
            ancho = float(self.txt_Ancho.text())
            area = largo*ancho
            self.msj(f"El área del Rectangulo es: {area}")
        except Exception as error:
            self.msj(f"Error: {error}")

    def msj(self, txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())