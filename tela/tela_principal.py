import time

from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from tela.ui_tela_principal import Ui_Tela
import pandas as pd


class TelaPrincipal(QMainWindow, Ui_Tela):
    def __init__(self):
        super(TelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Conversão de Planilhas OS")
        self.setFixedSize(585, 336)

        self.button_abrir_arquivo.clicked.connect(self.abrir_arquivo)
        self.buttonConverter.clicked.connect(self.converter_planilha)
        self.button_limpar_campos.clicked.connect(self.limpar_campos)

    def abrir_arquivo(self):
        arquivo = QFileDialog.getOpenFileName(self, 'Abrir Arquivo')
        self.txt_texto.setText(arquivo[0])

    def converter_planilha(self):
        if self.txt_texto.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("img/information.png"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alerta")
            msg.setText('Informe um caminho!')
            msg.exec_()
        elif self.txt_nome_analista.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("img/information.png"))
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alerta")
            msg.setText('Informe o nome completo do Analista!')
            msg.exec_()
        else:
            self.valor = 0
            while self.valor < 100:
                self.valor += 10
                time.sleep(0.50)
                self.barra_progresso.setValue(self.valor)
            tabela = pd.read_excel(self.txt_texto.text(), 'BASE')

            tabela = tabela.drop(["Oc."], axis=1)
            tabela = tabela.drop(["Status OS"], axis=1)
            tabela = tabela.drop(['Status Ocorrencia'], axis=1)
            tabela = tabela.drop(['Congelado'], axis=1)
            tabela = tabela.drop(['Equipe'], axis=1)
            tabela = tabela.drop(['Início Agendamento'], axis=1)
            tabela = tabela.drop(['Término Agendamento'], axis=1)

            tabela["Tempo Agendada"] = tabela["Tempo Agendada"].astype(int)

            saida = QFileDialog.getSaveFileName()

            nome_analista = self.txt_nome_analista.text().upper()
            filtro = tabela["Técnico"].str.contains(nome_analista)
            # filtro = tabela["Técnico"] == nome_analista
            print(nome_analista)

            tabela[filtro].to_excel(saida[0]+'.xlsx', index=False)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Alerta")
            msg.setText('Arquivo salvo com sucesso!')
            msg.exec_()

            self.limpar_campos()
            self.barra_progresso.setValue(0)

    def limpar_campos(self):
        self.txt_nome_analista.setText("")
        self.txt_texto.setText("")
