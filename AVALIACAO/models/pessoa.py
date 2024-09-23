from abc import ABC,abstractmethod 
from models.enums.sexo import Sexo
from models.endereco import Endereco

class Pessoa (ABC):
    def __init__(self, nome: str, idade: str, Sexo: Sexo, endereco: Endereco) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = Sexo
        self.endereco = endereco

    @abstractmethod
    def __str__ (self) -> str:
        return(
                f'\nNome: {self.nome}'
                f'\nIdade: {self.idade}'
                f'\nSexo: {self.sexo}'
                f'\nEndereço: {self.endereco}'            
            )
    