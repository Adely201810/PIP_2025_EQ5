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


    [":/Ejercicios/Archivos/Adobe Express - file (1).png",":/Ejercicios/Archivos/export202502092116429107.png",":/Ejercicios/Archivos/export202502092135328918.png",":/Ejercicios/Archivos/export202502092201258300.png",":/Ejercicios/Archivos/export202502092210045727.png",":/Ejercicios/Archivos/export202502092217592371.png",":/Ejercicios/Archivos/export202502092224352078.png",":/Ejercicios/Archivos/export202502092235269890.png",":/Ejercicios/Archivos/export202502092244329519.png",":/Ejercicios/Archivos/export202502092342196874.png"]