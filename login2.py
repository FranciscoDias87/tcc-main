from PyQt5 import uic, QtWidgets
import mysql.connector


def chama_terceira_tela():
    terceira_tela.show()
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    if nome_usuario == 'joao' and senha == '1234':
        primeira_tela.close()
        terceira_tela.show()


def logout():
    terceira_tela.close()
    primeira_tela.show()


def chama_cadastro():
    primeira_tela.close()
    cadastro.show()


def chama_quarta_tela():
    terceira_tela.close()
    quarta_tela.show()


def volta_terceira_tela():
    quarta_tela.close()
    terceira_tela.show()


def cadastrar():
    cadastro.close()
    nome = cadastro.lineEdit.text()
    telefone = cadastro.lineEdit_2.text()
    usuario = cadastro.lineEdit_3.text()
    senha = cadastro.lineEdit_4.text()
    csenha = cadastro.lineEdit_5.text()

    if (senha == csenha):
        try:
            banco = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="lilu1920tcc",
                database="cadastroTCC",
                port=3306
            )

            cursor = banco.cursor()
            cursor.execute(
                "INSERT INTO cadastro VALUES ('"+nome+"', '"+telefone+"', '"+usuario+"', '"+senha+"', '"+csenha+"')")

            banco.commit()
            banco.close()

        except AttributeError as erro:
            print("erro ao inserir banco de dados", erro)

    else:
        print('Senhas incorretas')


app = QtWidgets.QApplication([])
primeira_tela = uic.loadUi("primeira_tela.ui")
cadastro = uic.loadUi("cadastro.ui")
terceira_tela = uic.loadUi("terceira_tela.ui")
quarta_tela = uic.loadUi("quarta_tela.ui")

primeira_tela.pushButton.clicked.connect(chama_terceira_tela)
primeira_tela.pushButton_2.clicked.connect(chama_cadastro)
primeira_tela.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

cadastro.pushButton.clicked.connect(cadastrar)
cadastro.pushButton.clicked.connect(chama_terceira_tela)

terceira_tela.pushButton_2.clicked.connect(logout)
terceira_tela.pushButton.clicked.connect(chama_quarta_tela)

quarta_tela.pushButton.clicked.connect(logout)
quarta_tela.pushButton_2.clicked.connect(volta_terceira_tela)


primeira_tela.show()
app.exec()
