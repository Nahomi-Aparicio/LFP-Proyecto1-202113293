import math
from expreciones import *
from operador import Operaciones

class operacionesari(Expresion):
    
        def __init__(self,izquierda,derecha,tipo,fila,columna):
            self.izquierda=izquierda
            self.derecha=derecha
            self.tipo=tipo
            super().__init__(fila,columna)
    
        def ejecutar(self):
            izq=self.ejecutar(self.izquierda)
            der=self.ejecutar(self.derecha)
            if self.tipo==Operaciones.SUMA:
                return izq+der
            elif self.tipo==Operaciones.RESTA:
                return izq-der
            elif self.tipo==Operaciones.MULTIPLICACION:
                return izq*der
            elif self.tipo==Operaciones.DIVISION:
                return izq/der
            elif self.tipo==Operaciones.POTENCIA:
                return izq**der
            elif self.tipo==Operaciones.RAIZ:
                return izq**(1/der)
            elif self.tipo==Operaciones.INVERSO:
                return 1/izq
            elif self.tipo==Operaciones.SENO:
                return math.sin(izq)
            elif self.tipo==Operaciones.COSENO:
                return math.cos(izq)
            elif self.tipo==Operaciones.TANGENTE:
                return math.tan(izq)
            elif self.tipo==Operaciones.MOD:
                return izq%der
            else:
                return ('error')
