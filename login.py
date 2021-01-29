from PyQt5 import uic, QtWidgets

import mysql.connector

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="lilu1920tcc",
    database="cadastro_tcc",
    port=3306
)


def primeira_tela2():
    linha1 = primeira_tela.lineEdit.text()
    linha2 = primeira_tela.lineEdit_2.text()
    print("LOGIN:", linha1)
    print("SENHA:", linha2)


def funcao_principal():
    linha1 = cadastro.lineEdit.text()
    linha2 = cadastro.lineEdit_2.text()
    linha3 = cadastro.lineEdit_3.text()
    linha4 = cadastro.lineEdit_4.text()
    print("NOME:", linha1)
    print("TELEFONE:", linha2)
    print("USUARIO:", linha3)
    print("SENHA:", linha4)

    cursor = banco.cursor()

    comando_SQL = "INSERT INTO 'cadastro_tcc'('nome','telefone','usuario','senha') VALUES ('%s','%s','%s','%s')"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4))
    cursor.execute(comando_SQL, dados)
    banco.comit()


def chama_segunda_tela():
    formulario.show()


def envio_formulario():
    comando_SQL.send()


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
formulario = uic.loadUi("cadastro.ui")
primeira_tela.pushButton.clicked.connect(funcao_principal)
primeira_tela.pushButton_2.clicked.connect(chama_segunda_tela)
formulario.pushButton.clicked.connect(envio_formulario)


primeira_tela.show()
app.exec()
