from PyQt5 import uic,QtWidgets

def funcao_principal():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked():
        print("Categoria Eletrônicos foi selecionada")
    elif formulario.radioButton_2.isChecked():
        print("Categoria Informatica foi selecionada") 
    else:
        print("Categoria Alimentos foi selecionada")

    print("código:", linha1)
    print("descrição:", linha2)
    print("preço:", linha3)


app=QtWidgets.QApplication([])
formulario=uic.loadUi("cadastro.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()