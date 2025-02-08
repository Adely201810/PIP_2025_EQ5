import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P06_Componente_VerticalSlider.ui" # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.dial.setMinimum(-50)
        self.dial.setMaximum(50)
        self.dial.setSingleStep(5)
        self.dial.setValue(-50)
        self.dial.valueChanged.connect(self.CambiaValor)
        self.txt_Valor.setText(str("-50"))


    #Area de los Slots
    def CambiaValor(self):
        value=self.dial.value()

        self.txt_Valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())