import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco

@pytest.fixture
def criar_fornecedor():
    endereco = Endereco("Rua D", 101, "Loja 3", "54321-000", "Cidade D", "SP")
    return Fornecedor(
        id=4, nome="Fornecedor A", telefone="66666-6666", email="fornecedor@exemplo.com", 
        endereco=endereco, cnpj="33.333.333/0001-33", inscricaoEstadual="987654321", 
        produto="Eletrônicos"
    )

def test_fornecedor_str(criar_fornecedor):
    expected = ("ID: 4\nNome: Fornecedor A\nTelefone: 66666-6666\nEmail: fornecedor@exemplo.com\n"
                "Endereço: Rua D, 101 - Loja 3\nCNPJ: 33.333.333/0001-33\n"
                "Inscrição Estadual: 987654321\nProduto: Eletrônicos")
    assert str(criar_fornecedor) == expected
