from creatEvent import create_event, create_manual, interface, application



interface.pushButton_2.clicked.connect(create_event)


interface.show()
application.exec()