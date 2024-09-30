import pytest
from projeto.models.principal.prestacao_servico import PrestacaoServico
from projeto.models.principal.endereco import Endereco

@pytest.fixture
def criar_prestacao_servico():
    endereco = Endereco("Rua G", 303, "Loja 20", "87654-333", "Cidade G", "MG")
    return PrestacaoServico(
        id=7, nome="Empresa X", telefone="33333-3333", email="empresa@exemplo.com", 
        endereco=endereco, cnpj="55.555.555/0001-55", inscricaoEstadual="543210987", 
        contratoInicio=2022.01, contratoFim=2023.01
    )

def test_prestacao_servico_str(criar_prestacao_servico):
    expected = ("ID: 7\nNome: Empresa X\nTelefone: 33333-3333\nEmail: empresa@exemplo.com\n"
                "Endereço: Rua G, 303 - Loja 20\nCNPJ: 55.555.555/0001-55\n"
                "Inscrição Estadual: 543210987\nInício do Contrato: 2022.01\n"
                "Fim do Contrato: 2023.01")
    assert str(criar_prestacao_servico) == expected
