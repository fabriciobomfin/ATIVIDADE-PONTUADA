from abc import ABC, abstractmethod

from projeto.models.principal.pessoa import Pessoa
from projeto.models.principal.endereco import Endereco

class PessoaJuridica(Pessoa, ABC):
    @abstractmethod
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str,) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricaoEstadual = inscricaoEstadual

    def _verificar_tamanho_cnpj(self, CNPJ):
            if len(CNPJ) > 14:
                raise TypeError("CNPJ inválido.")
            return CNPJ


    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nCNPJ: {self.cnpj}"
            f"\nInscrição Estadual: {self.inscricaoEstadual}"
        )
#from projeto.models.principal.endereco import Endereco