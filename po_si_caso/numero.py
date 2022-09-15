from expreciones import *

class numero(Expresion):

    def __init__(self,valor,fila,columna):
        self.valor=valor
        super().__init__(fila,columna)

    def ejecutar(self):
        return self.valor


        