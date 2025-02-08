import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P02_EjemploMensajeEmeregenteBasico.ui" # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_Saludar.clicked.connect(self.Saludar)

    #Area de los Slots
    def Saludar(self):
        self.msj("¡Hola! es un gusto, ¿Comó estás?")

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())