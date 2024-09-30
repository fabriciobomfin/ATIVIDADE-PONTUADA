from projeto.models.principal import Fisica
from abc import ABC,abstractmethod

from projeto.models.principal.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo

class Cliente(Fisica,ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadoCivil: EstadoCivil, dataNascimento: str, protocoloAtendimento: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadoCivil, dataNascimento)

        self.protocoloAtendimento = protocoloAtendimento
    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"Protocolo de Atendimento: {self.protocoloAtendimento}")
    