import sys
from  PyQt6.QtWidgets import *

def funcao_apertou():
    print("Você apertou o botão")
    texto1.setText('senaiii')

app= QApplication(sys.argv)

janela= QWidget()
janela.resize(400,400) #(x,y)

#funções
def funcao_apertou():
    print("Você apertou o botão")
    # texto1.setText('senaiii')
    
    texto= linha_de_texto.text()
    texto1.setText(texto)
#css
with open('estilo.css','r') as file:
    app.setStyleSheet(file.read())    

# #inserindo elementos na tela
texto1= QLabel ("curso de python" , janela) #(oq é escrito e onde é escrito)
texto1.setGeometry(10,5,380,20) #1- onde ele fica 2-altura e largura do negocio
texto1.setStyleSheet (
                      'background-color: blue;'+
                      'color:white;'+
                      'font 14pt "MS Shell Dlg 2";' +
                      'qprotperty-alignment: AlignCenter;'
                      )

linha_de_texto= QLineEdit('', janela)
linha_de_texto.setGeometry(10,25,380,50)

botao= QPushButton('enviar', janela)
botao.setGeometry(160,200,80,80)
botao.clicked.connect(funcao_apertou)
# botao.setStyleSheet(
#                     'background-color: black;'+
#                     'color:white;'+
#                     'border-style: solid;'+
#                     'border-color: red;'+
#                     'border-width: 2px;'+
#                     'border-radius: 30px;'+
#                     'font-size: 20px'


janela.show()
app.exec()

