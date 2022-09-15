from abc import ABC, abstractmethod
from fileinput import filename

class Expresion(ABC):
    
    def __init__(self,fila,columna):
        self.fila=fila
        self.coluumna=columna

    @abstractmethod
    def ejecutar(self):
        pass
    

    
