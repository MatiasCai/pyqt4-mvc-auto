# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui
sys.path.append('../Controladores')
from main_controller import *


class MainWindow(QtGui.QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.controlador = MainControlador(self)
        self.init_ui()

    def init_ui(self):
        self.label = QtGui.QLabel('cantidad de personas')
        h_layout = QtGui.QHBoxLayout()
        h_layout.addWidget(self.label)
        self.entrada_texto = QtGui.QLineEdit()
        button_subir = QtGui.QPushButton('Subite capo')
        button_bajar = QtGui.QPushButton('Bajate o te bajo')
        button_bajar5 = QtGui.QPushButton('Bajar 5 capos')
        button_subir5 = QtGui.QPushButton('Subir 5 capos')
        button_subirx = QtGui.QPushButton('Subir x capos')
        button_bajarx = QtGui.QPushButton('Bajar x capos')
        h_layout.addWidget(button_subir)
        h_layout.addWidget(button_bajar)
        h_layout.addWidget(button_bajar5)
        h_layout.addWidget(button_subir5)
        h_layout.addWidget(self.entrada_texto)
        h_layout.addWidget(button_subirx)
        h_layout.addWidget(button_bajarx)

        button_subir.clicked.connect(self.controlador.handler_subir_persona)
        button_bajar.clicked.connect(self.controlador.handler_bajar_persona)
        button_bajar5.clicked.connect(self.controlador.handler_bajar_persona5)
        button_subir5.clicked.connect(self.controlador.handler_subir_persona5)
        button_subirx.clicked.connect(self.controlador.handler_subir_personax)
        button_bajarx.clicked.connect(self.controlador.handler_bajar_personax)

        self.setLayout(h_layout)
        self.setWindowTitle('Proyecto del auto')
        self.setGeometry(200, 200, 200, 200)
        self.show()

app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())