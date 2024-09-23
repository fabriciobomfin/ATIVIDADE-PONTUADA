from enum import Enum

class Sexo(Enum):
    MASCULINO = ("Masculino","M")
    FEMININO = ("Feminino","F")
    NEUTRO = ("Neutro","N")

def __init__(self, texto: str, caracter: str) -> None:
        self._texto = texto
        self._caracter = caracter

@property
def texto(self) -> str:
        return self._texto

@property
def caracter(self) -> str:
        return self._caracter