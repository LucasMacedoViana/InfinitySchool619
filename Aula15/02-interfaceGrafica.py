#pyqt,  pip install PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QToolTip, QLabel, QLineEdit

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        #botao
        #self pq ele nasce na prorpia janela
        self.botao = QPushButton("Clique-me", self)
        #posicionamento do botao
        self.botao.move(250,300)
        #tamanho do botao
        self.botao.resize(150,45)
        #botando estilo no botão
        self.botao.setStyleSheet('QPushButton {background-color: #836FF}')
        #concetando o botao
        self.botao.clicked.connect(self.clicou)

        #Label
        self.label = QLabel(self)
        self.label.setText("sou um label")
        self.label.setStyleSheet("QLabel {font: bold; size: 20px; color: #1CD475}")
        #atenção com os tamanhos para nao cobrir nenhum outro componente!
        self.label.move(300,250)
        self.label.resize(100,25)

        #Campo
        self.campo = QLineEdit(self)
        self.campo.move(210,40)
        self.resize(150,254)

        self.carregarJanela()

    def clicou(self):
        valor = self.campo.text()
        self.botao.setText("Valor do campo" + valor)
        self.label.setText("Você clicou2x")
        self.label.setStyleSheet("QLabel {font: bold; size: 20px; color: #0F01B7}")

    def carregarJanela(self):
        #configurar a geometria da janela
        self.setGeometry(500,100,700,600)
        #metodo para exibir a janela
        self.show()


#quando nao tem nenhum comando de interação com o sistema operacional, passamos uma lista vazia
app = QApplication([])
j = Janela()
app.exec_()
