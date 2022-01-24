# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Tela(object):
    def setupUi(self, Tela):
        if not Tela.objectName():
            Tela.setObjectName(u"Tela")
        Tela.resize(585, 336)
        icon = QIcon()
        icon.addFile(u"excel.png", QSize(), QIcon.Normal, QIcon.Off)
        Tela.setWindowIcon(icon)
        Tela.setStyleSheet(u"")
        self.centralwidget = QWidget(Tela)
        self.centralwidget.setObjectName(u"centralwidget")
        self.button_abrir_arquivo = QPushButton(self.centralwidget)
        self.button_abrir_arquivo.setObjectName(u"button_abrir_arquivo")
        self.button_abrir_arquivo.setGeometry(QRect(20, 80, 161, 30))
        self.button_abrir_arquivo.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.button_abrir_arquivo.setFont(font)
        self.txt_texto = QLineEdit(self.centralwidget)
        self.txt_texto.setObjectName(u"txt_texto")
        self.txt_texto.setGeometry(QRect(200, 80, 371, 31))
        self.barra_progresso = QProgressBar(self.centralwidget)
        self.barra_progresso.setObjectName(u"barra_progresso")
        self.barra_progresso.setGeometry(QRect(20, 250, 551, 23))
        self.barra_progresso.setValue(0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 561, 41))
        font1 = QFont()
        font1.setFamily(u"Bernard MT Condensed")
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 160, 551, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setPixmap(QPixmap(u"converter.png"))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.buttonConverter = QPushButton(self.frame)
        self.buttonConverter.setObjectName(u"buttonConverter")
        self.buttonConverter.setMinimumSize(QSize(0, 30))
        self.buttonConverter.setFont(font)

        self.horizontalLayout.addWidget(self.buttonConverter)

        self.button_limpar_campos = QPushButton(self.frame)
        self.button_limpar_campos.setObjectName(u"button_limpar_campos")
        self.button_limpar_campos.setMinimumSize(QSize(0, 30))
        self.button_limpar_campos.setFont(font)

        self.horizontalLayout.addWidget(self.button_limpar_campos)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 130, 121, 16))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_nome_analista = QLineEdit(self.centralwidget)
        self.txt_nome_analista.setObjectName(u"txt_nome_analista")
        self.txt_nome_analista.setGeometry(QRect(200, 120, 371, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 10, 61, 61))
        self.label_5.setPixmap(QPixmap(u"excel.png"))
        Tela.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Tela)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 585, 21))
        Tela.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Tela)
        self.statusbar.setObjectName(u"statusbar")
        Tela.setStatusBar(self.statusbar)

        self.retranslateUi(Tela)

        QMetaObject.connectSlotsByName(Tela)
    # setupUi

    def retranslateUi(self, Tela):
        Tela.setWindowTitle(QCoreApplication.translate("", u"MainWindow", None))
        self.button_abrir_arquivo.setText(QCoreApplication.translate("", u"Procurar Arquivo Excel", None))
        self.label.setText(QCoreApplication.translate("", u"Convers\u00e3o planillha OS", None))
        self.label_6.setText("")
        self.buttonConverter.setText(QCoreApplication.translate("", u"Converter", None))
        self.button_limpar_campos.setText(QCoreApplication.translate("", u"Limpar Campos", None))
        self.label_4.setText(QCoreApplication.translate("", u"Nome Analista: ", None))
        self.label_5.setText("")
    # retranslateUi

