import pytest
from projeto.models.principal.funcionario import Funcionario
from projeto.models.principal.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def criar_funcionario():
    endereco = Endereco("Rua E", 102, "Apto 202", "65432-111", "Cidade E", "ES")
    return Funcionario(
        id=5, nome="Ana", telefone="55555-5555", email="ana@exemplo.com", 
        endereco=endereco, sexo=Sexo.FEMININO, estadoCivil=Estado_Civil.SOLTEIRO, 
        dataNascimento="04/04/1985", cpf="333.333.333-33", rg="7654321", 
        matricula="9012", setor=Setor.RH, salario=5000.0
    )

def test_funcionario_str(criar_funcionario):
    expected = ("ID: 5\nNome: Ana\nTelefone: 55555-5555\nEmail: ana@exemplo.com\n"
                "Endereço: Rua E, 102 - Apto 202\nSexo: Feminino\nEstado Civil: Solteiro\n"
                "Data de Nascimento: 04/04/1985\nCPF: 333.333.333-33\nRG: 7654321\n"
                "Matricula: 9012\nSetor: RH\nSalário: 5000.0")
    assert str(criar_funcionario) == expected
