from cadastro import  Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow,QApplication

class Janela(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication([])
janela = Janela()
janela.show()
app.exec()
