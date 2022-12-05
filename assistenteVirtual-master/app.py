from PyQt5 import uic,QtWidgets
from creatEvent import create_event, create_manual

def funcao_digitar():
    line_text = interface.lineEdit.text()
    interface.label_2.setText(line_text)

app = QtWidgets.QApplication([])

interface = uic.loadUi("TELA_PRINCIPAL.ui")

interface.pushButton_2.clicked.connect(create_event) # acionamento através do botão fale
interface.pushButton.clicked.connect(funcao_digitar)#botão pra acionar por texto


interface.show()
app.exec()