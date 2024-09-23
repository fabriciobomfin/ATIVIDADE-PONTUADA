from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA = ("Bahia", "BA")
    SÃO_PAULO = ("São Paulo", "SP")
    RIO_DE_JANEIRO = ("Rio de Janeiro", "RJ")
   
    def __init__(self, nome, sigla):
        self._nome = nome
        self._sigla = sigla

    @property
    def nome(self):
        return self._nome

    @property
    def sigla(self):
        return self._sigla
