import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def criar_cliente():
    endereco = Endereco("Rua B", 456, "Casa 5", "98765-432", "Cidade B", "RJ")
    return Cliente(
        id=2, nome="Maria", telefone="88888-8888", email="maria@exemplo.com", 
        endereco=endereco, sexo=Sexo.FEMININO, estadoCivil=Estado_Civil.CASADO,
        dataNascimento="02/02/1990", protocoloAtendimento=123
    )

def test_cliente_str(criar_cliente):
    expected = ("ID: 2\nNome: Maria\nTelefone: 88888-8888\nEmail: maria@exemplo.com\n"
                "Endereço: Rua B, 456 - Casa 5\nSexo: Feminino\nEstado Civil: Casado\n"
                "Data de Nascimento: 02/02/1990\nProtocolo de Atendimento: 123")
    assert str(criar_cliente) == expected
