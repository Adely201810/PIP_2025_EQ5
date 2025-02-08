import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P08_PromedioNumeros-Load_V2.ui" # Nombre del archivo ".ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Area de los Signals
        self.btn_Cargar.clicked.connect(self.Cargar)
        self.btn_Agregar.clicked.connect(self.Agregar)
        self.btn_Guardar.clicked.connect(self.Guardar)
        self.calificaciones =[]

    #Area de los Slots
    def Cargar (self):
        #Tarea como compruevo si el archivo existe
        #ejercicio 10
        # tarea ej 11 en lugar de sobre escribir, concadenar
        #tarea ej 12 asegurarse de que solo se pueda cargar hasta antes de
        #agregar la prmera calificacion    enables y/o codigo
        archivo = open("../Archivos/calificaciones.csv")
        contenido = archivo.readlines()
        print(contenido)
        datos = [int(x) for x in contenido]
        print(datos)
        self.calificaciones = datos
        self.promedio()
        try:
            self.txt_listacalificaciones.setText(str(self.calificaciones))
        except Exception as error:
            print(error)
        self.txt_listacalificaciones.setText(str(self.calificaciones))

    def Agregar (self):
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        prom = sum(self.calificaciones)/len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def promedio(self):
        prom = round(sum(self.calificaciones) / len(self.calificaciones), 2)
        self.txt_promedio.setText(str(prom))

    def Guardar(self):
        archivo = open("../Archivos/calificaciones.csv", "w")  # w = write, a = append
        for c in self.calificaciones:
            archivo.write(str(c))
            archivo.write("\n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo guardado bien")

    def msj(self,txt):
        m=QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())