from PySide2.QtWidgets import QApplication
from tela.tela_principal import TelaPrincipal
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = TelaPrincipal()
    janela.show()

    app.exec_()
