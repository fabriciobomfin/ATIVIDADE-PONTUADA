from projeto.models.principal.pessoa import Pessoa
from projeto.models.principal.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil
from abc import ABC,abstractmethod

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil : EstadoCivil, dataNascimento:str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadoCivil = estadoCivil
        self.dataNascimento = dataNascimento
        
    @abstractmethod
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Sexo: {self.sexo.texto}"
                f"Estado Civil: {self.estadoCivil.value}"
                f"Data de nascimento: {self.dataNascimento}")
    