from projeto.models.principal.juridica import PessoaJuridica
from projeto.models.principal.endereco import Endereco


class PrestacaoServico(PessoaJuridica):
    def __init__(self, contratoInicio: str, contratoFim: str, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoEstadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoEstadual)
        self.contratoInicio = contratoInicio
        self.contratoFim = contratoFim

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\nInicio do contrato: {self.contratoInicio}"
            f"\nFim do contrato: {self.contratoFim}"
            )