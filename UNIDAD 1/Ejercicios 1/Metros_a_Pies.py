import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Metros_a_Pies.ui"  # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los Signals
        self.btn_Pies.clicked.connect(self.Pies)
        self.btn_Metros.clicked.connect(self.Metros)

    # Área de los Slots
    def Pies(self):
        try:
            metros = float(self.txt_Valor.text())  # Convierte el texto a un número decimal
            pies = metros * 3.28084  # Conversión de metros a pies
            self.msj(f"{metros} metros son aproximadamente {pies:.2f} pies.")
        except Exception as error:
            self.msj(f"Error: {error}")

    def Metros(self):
        try:
            pies = float(self.txt_Valor.text())  # Convierte el texto a un número decimal
            metros = pies / 3.28084  # Conversión de pies a metros
            self.msj(f"{pies} pies son aproximadamente {metros:.2f} metros.")
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