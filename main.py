from gui_design import *


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
# Se define le contructor con todos los atributos necesarios y asociacion de metodos
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Se definen los eventos:
        self.BTN_ESCRIBIR.clicked.connect(self.escribir)
        self.BTN_BORRAR.clicked.connect(self.borrar)

        self.borrar()

    # Se definen los metodos
    def escribir(self):
        self.LABEL_TEXTO.setText("Hola PyQt5")

    def borrar(self):
        self.LABEL_TEXTO.clear()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyApp()
    window.show()
    app.exec_()