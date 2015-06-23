# -*- coding: utf-8 -*-

import sys
sys.path.append('../Modelos')
from auto import *


class MainControlador():

    def __init__(self, una_ventana):
        self.auto = Auto()
        self.ventana = una_ventana

    def handler_subir_persona(self):
        self.auto.subirPersonas()
        self.actualizar_label()

    def handler_bajar_persona(self):
        self.auto.bajarPersonas()
        self.actualizar_label()

    def handler_bajar_persona5(self):
        i = 1
        while i <= 5:
            i += 1
            self.handler_bajar_persona()

    def handler_subir_persona5(self):
        i = 1
        while i <= 5:
            i += 1
            self.handler_subir_persona()

    def handler_subir_personax(self):
        x = self.ventana.entrada_texto.text()
        y = int(x)
        while y > 0:
            y -= 1
            self.handler_subir_persona()

    def handler_bajar_personax(self):
        x = self.ventana.entrada_texto.text()
        y = int(x)
        while y > 0:
            y -= 1
            self.handler_bajar_persona()

    def actualizar_label(self):
        self.ventana.label.setText(str(self.auto.cantidad_personas))