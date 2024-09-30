import pytest
from projeto.models.principal.endereco import Endereco
from projeto.models.enums.sexo import Sexo
from projeto.models.principal.pessoa import Pessoa

@pytest.fixture
def criar_pessoa():
    endereco = Endereco("Rua Exemplo", 123, "Apto 1", "12345-678", "Cidade Exemplo", "SP")
    return Pessoa(id=1, nome="João", telefone="123456789", email="joao@example.com", endereco=endereco)

def test_inicializacao_pessoa(criar_pessoa):
    assert criar_pessoa.id == 1
    assert criar_pessoa.nome == "João"
    assert criar_pessoa.telefone == "123456789"
    assert criar_pessoa.email == "joao@example.com"

def test_verificacao_id_invalido():
    with pytest.raises(TypeError):
        Pessoa(id="um", nome="João", telefone="123456789", email="joao@example.com", endereco=None)

def test_verificacao_telefone_invalido():
    with pytest.raises(TypeError):
        Pessoa(id=1, nome="João", telefone="um", email="joao@example.com", endereco=None)

def test_telefone_negativo():
    with pytest.raises(ValueError):
        Pessoa(id=1, nome="João", telefone=-123456789, email="joao@example.com", endereco=None)

def test_str_representation(criar_pessoa):
    expected_str = (f"ID: 1\nNome: João\nTelefone: 123456789\nEmail: joao@example.com\nEndereco: Rua Exemplo, 123 - Apto 1")
    assert str(criar_pessoa) == expected_str
