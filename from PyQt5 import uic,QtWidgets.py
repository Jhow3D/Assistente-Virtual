from PyQt5 import uic,QtWidgets


app = QtWidgets.QApplication([])

interface = uic.loadUi("TELA_PRINCIPAL.ui")
interface.show()
app.exec()