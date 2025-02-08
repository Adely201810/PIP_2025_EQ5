import sys
import time as t
from PyQt5 import uic, QtWidgets, QtCore
qtCreatorFile = "P10_SegundoPlanoTimer.ui" # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.controlSegundoPlano)
        self.btn_temporizador.clicked.connect(self.temporizador2doPlano)
        self.valorN=-1

    #Area de los Slots
    def controlador2doPlano(self):
        self.self.txt_temporizador.setText(str(self.valorN))
        self.valorN-=1
        if self.valorN==-1:
            self.segundoPlano.stop()

    def temporizador(self):
        self.valorN=int (self.txt_temporizador.text())
        self.segundoPlano.start(500)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())