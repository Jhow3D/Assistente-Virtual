from PyQt5 import uic,QtWidgets

def funcao_digitar():
    line_text = interface.lineEdit.text()
    print(line_text)


app = QtWidgets.QApplication([])

interface = uic.loadUi("TELA_PRINCIPAL.ui")
interface.pushButton.clicked.connect(funcao_digitar)

interface.show()
app.exec()