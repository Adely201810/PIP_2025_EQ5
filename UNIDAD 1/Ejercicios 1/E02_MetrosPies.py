import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E02_MetrosPies.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
metros = True

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #La accion de convertir se puso para ambos botones para no tener que incluir un boton extra

        #Acciones del boton mp (metros a pies)
        self.btn_mp.clicked.connect(self.metros_pies)
        self.btn_mp.clicked.connect(self.convertir)
        # Acciones del boton pm (pies a metros)
        self.btn_pm.clicked.connect(self.pies_metros)
        self.btn_pm.clicked.connect(self.convertir)

    def convertir(self):
        #valor 1 es el valor que se ingresa en el txt_1, que es el valor que se va a convertir a otra unidad
        #valor 2 es el resultado del valor 1 convertido.

        #valor 1 SIEMPRE estara en txt_1
        #valor 2 SIEMPRE se mostrara en Lbl_2

        try:
            try:
                valor1 = float(self.txt_1.text())
            except:
                self.msj("Por favor, ingrese un valor numerico")
                return

            if metros:
                valor2 = valor1 * 3.28084
                #redondear valor2 a 2 decimales
                valor2 = round(valor2, 2)
                self.Lbl_2.setText(str(valor2)+" Pies")
                self.changeStyleSheet(self.Lbl_2)

            else:
                valor2 = valor1 / 3.28084
                #redondear valor2 a 2 decimales
                valor2 = round(valor2, 2)
                self.Lbl_2.setText(str(valor2)+" Metros")
                self.changeStyleSheet(self.Lbl_2)
        except Exception as error:
            #esto, es para que si al hacer cualquier cosa de estas, hay un error, se muestre en la etiqueta Lbl_2
            print(error)
            self.Lbl_2.setText("Error")

    #Para cambiarle el styleshet a la etiqueta, pero en metodo para que sea bonito
    def changeStyleSheet(self, label):
        label.setStyleSheet("""
           QLabel {
               font-family: Arial;
               font-size: 20px;
               color: black;
               border-radius: 10px;
               font-weight: bold;
               font-style: italic;
           }
           """)


    def metros_pies(self):
        global metros
        metros = True
        self.Lbl_2.setText("0 Pies")
        self.changeStyleSheet(self.Lbl_1)
        self.Lbl_1.setText("Metros: ")
        self.changeStyleSheet(self.Lbl_2)



    def pies_metros(self):
        global metros
        metros = False
        self.Lbl_2.setText("0 Metros")
        self.changeStyleSheet(self.Lbl_1)
        self.Lbl_1.setText("Pies: ")
        self.changeStyleSheet(self.Lbl_2)

    def msj(self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.setStyleSheet("""
                QMessageBox QLabel {
                    font-family: Arial;
                    font-size: 20px;
                    color: #123456;
                    font-weight: bold;
                }
            """)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())