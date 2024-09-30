import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

@pytest.fixture
def criar_medico():
    endereco = Endereco("Rua F", 203, "Consultório 101", "76543-222", "Cidade F", "RJ")
    return Medico(
        id=6, nome="Dra. Silva", telefone="44444-4444", email="silva@exemplo.com", 
        endereco=endereco, sexo=Sexo.FEMININO, estadoCivil=Estado_Civil.CASADO, 
        dataNascimento="05/05/1970", cpf="444.444.444-44", rg="6543210", 
        matricula="3456", setor=Setor.SAUDE, salario=12000.0, crm="123456-RJ"
    )

def test_medico_str(criar_medico):
    expected = ("ID: 6\nNome: Dra. Silva\nTelefone: 44444-4444\nEmail: silva@exemplo.com\n"
                "Endereço: Rua F, 203 - Consultório 101\nSexo: Feminino\nEstado Civil: Casado\n"
                "Data de Nascimento: 05/05/1970\nCPF: 444.444.444-44\nRG: 6543210\n"
                "Matricula: 3456\nSetor: Saúde\nSalário: 12000.0\nCRM: 123456-RJ")
    assert str(criar_medico) == expected
