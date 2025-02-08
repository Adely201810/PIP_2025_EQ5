import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P04_SumaDosNumeros.ui" # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_Sumar.clicked.connect(self.Sumar)

    #Area de los Slots
    def Sumar(self):
        try:
            a=int(self.txt_Aa.text())
            b = int(self.txt_Bb.text())
            r= a+b
            self.msj("La suma es:" +str(r))
        except Exception as error:
            print(error)

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())