import pytest
from projeto.models.principal.engenheiro import Engenheiro
from projeto.models.principal.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def criar_engenheiro():
    endereco = Endereco("Rua C", 789, "Bloco 10", "54321-678", "Cidade C", "MG")
    return Engenheiro(
        id=3, nome="Carlos", telefone="77777-7777", email="carlos@exemplo.com", 
        endereco=endereco, sexo=Sexo.MASCULINO, estadoCivil=Estado_Civil.SOLTEIRO, 
        dataNascimento="03/03/1975", cpf="222.222.222-22", rg="87654321", 
        matricula="5678", setor=Setor.ENGENHARIA, salario=10000.0, crea="654321"
    )

def test_engenheiro_str(criar_engenheiro):
    expected = ("ID: 3\nNome: Carlos\nTelefone: 77777-7777\nEmail: carlos@exemplo.com\n"
                "Endereço: Rua C, 789 - Bloco 10\nSexo: Masculino\nEstado Civil: Solteiro\n"
                "Data de Nascimento: 03/03/1975\nCPF: 222.222.222-22\nRG: 87654321\n"
                "Matricula: 5678\nSetor: Engenharia\nSalário: 10000.0\nCREA: 654321")
    assert str(criar_engenheiro) == expected
