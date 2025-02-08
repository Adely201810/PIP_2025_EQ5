import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "U1_Proyecto_1.ui" #Cambiar el nombre a P00 osea el numero 0, no el O XD
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        # bontes (btn_Cargar, btn_Eliminar, btn_Guardar,btn_Modificar)
        self.btn_Cargar.clicked.connect(self.cargar)
        self.btn_Eliminar.clicked.connect(self.eliminar)
        self.btn_Guardar.clicked.connect(self.guardar)
        self.btn_Modificar.clicked.connect(self.modificar)

    def cargar(self):
        #Leer el archivo desde la carpeta Archivo, con el nombre de datos.txt
        #     ruta = "../../Archivos/datos.txt"
        try:
            ruta = "datos.txt"
            archivo = open(ruta, "r")
            datos = archivo.read()
            archivo.close()
            self.txt_Datos.setText(datos)
        except Exception as e:
            self.msj("Error al cargar el archivo: "+str(e))

    def eliminar(self):
        pass

    def guardar(self):
        pass

    def modificar(self):
        pass

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

    #Area de los Slots

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())