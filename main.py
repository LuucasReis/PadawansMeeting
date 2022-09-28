from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Interfaces.login import *
from Interfaces.cadastro import Ui_MainWindow2
from Interfaces.padawansproject import Ui_MainWindow3


from Interfaces.pictures import Ui_MainWindow4

class Login(QMainWindow,Ui_MainWindow1):
    def __init__(self, parent= None):
        super().__init__(parent)
        super().setupUi(self)
        self.__cadastro = []
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton_cadastrar.clicked.connect(self.Cadastrar)
        self.pushButton_login.clicked.connect(self.Entrar)
        self.checkBox.stateChanged.connect(self.checked)
        

    @property
    def cadastro(self):
        return self.__cadastro
    
    def checked(self):
        if self.checkBox.isChecked():
            self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Normal)

        else:
            self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)

    def Cadastrar(self):
        self.close()
        self.lineEdit_login.setText("")
        self.lineEdit_senha.setText("")
        self.label_message.setText("")
        tela_cadastro.show()
    
    def Entrar(self):
        self.user = self.lineEdit_login.text()
        self.senha = self.lineEdit_senha.text()

        if self.__cadastro == []:
            self.label_message.setText("VOCÊ NÃO POSSUI CADASTRO!!")
            return
        for dados in self.__cadastro:
            if dados[0] == self.user and dados[1] == self.senha:
                self.close()
                self.lineEdit_login.setText("")
                self.lineEdit_senha.setText("")
                self.label_message.setText("")
                global padawans_project
                padawans_project = Padawans(dados[2])
                padawans_project.show()
            
            else:
                
                self.label_message.setText("LOGIN INCORRETO!!")

        
class Cadastro(QMainWindow, Ui_MainWindow2):
    def __init__ (self, parent = None):
        super(). __init__(parent)
        super().setupUi(self)
        self.lineEdit_senha1.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_senha2.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.pushButton_cfcadastro.clicked.connect(self.FazerCadastro)
        self.pushButton_voltar.clicked.connect(self.Voltar)
        
    
    def FazerCadastro(self):
        self.login = self.lineEdit_user.text()
        self.senha= self.lineEdit_senha1.text()
        self.cf_senha = self.lineEdit_senha2.text()
        self.nome = self.lineEdit_nome.text()
        self.sobrenome = self.lineEdit_sobrenome.text()

        if not self.senha == self.cf_senha:
            self.label_error.setText("SENHA DIFERENTE DA CONFIRMAÇÃO!!")

        else:
            tela_login.cadastro.append((self.login, self.senha, self.nome, self.sobrenome))
            self.close()
            self.lineEdit_user.setText("")
            self.lineEdit_senha1.setText("")
            self.lineEdit_senha2.setText("")
            self.lineEdit_nome.setText("")
            self.lineEdit_sobrenome.setText("")
            self.label_error.setText("")
            tela_login.label_message.setText("Cadastro Concluído com sucesso!")
            tela_login.show()


            
    def Voltar(self):
        self.close()
        self.lineEdit_user.setText("")
        self.lineEdit_senha1.setText("")
        self.lineEdit_senha2.setText("")
        self.lineEdit_nome.setText("")
        self.lineEdit_sobrenome.setText("")
        self.label_error.setText("")
        tela_login.show()    


class Padawans(QMainWindow, Ui_MainWindow3):
    def __init__(self,nome, parent= None):
        super().__init__(parent)
        super().setupUi(self)
        self.label_welcome.setText(f"  Bem vindo, {nome}!!")
        self.pushButton_t1.clicked.connect(self.FotoIrma)
        self.pushButton_t2.clicked.connect(self.FotoFamilia)
        self.pushButton_t3.clicked.connect(self.Descontracao)
        self.pushButton_logout.clicked.connect(self.Logout)
        
    def FotoIrma(self):
        self.picture_irma = Pictures(r"Interfaces\fotoirma.jpg")
        self.picture_irma.label_estagio.setText("")
        self.picture_irma.label_estagio.setGeometry(QtCore.QRect(0,0,0,0))
        self.picture_irma.show()

    def FotoFamilia(self):
        self.picture_familia = Pictures(r"Interfaces\fotofamilia.jpg")
        self.picture_familia.label_estagio.setText("")
        self.picture_familia.label_estagio.setGeometry(QtCore.QRect(0,0,0,0))
        self.picture_familia.show()

    def Descontracao(self):
        self.picture_descontracao = Pictures(r"Interfaces\lukeskywalker.jpg")
        self.picture_descontracao.resize(320,450)
        self.picture_descontracao.show()

    def Logout(self):
        self.close()
        self.label_welcome.setText("")
        tela_login.label_message.setText("")
        tela_login.show()              


class Pictures(QMainWindow, Ui_MainWindow4):
    def __init__(self, caminho, parent = None):
        super().__init__(parent)
        super().setupUi(self)
        self.img = caminho
        self.img= QtGui.QPixmap(self.img)
        self.resize(self.img.width(), self.img.height())
        self.label_photo.setGeometry(QtCore.QRect(0,0,self.img.width(), self.img.height()))
        
        self.label_photo.setPixmap(self.img)

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    tela_login = Login()
    tela_cadastro= Cadastro()
    tela_fotos = Ui_MainWindow4()
    tela_login.show()
    qt.exec_()