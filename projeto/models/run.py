from projeto.models.principal.advogado import Advogado
from projeto.models.principal.endereco import Endereco
from projeto.models.enums.estado_civil import Estado_Civil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo

# Criar um endereço
endereco = Endereco("Rua A", 123, "Apto 101", "12345-678", "Cidade A", "SP")

# Criar um advogado
advogado = Advogado(
    id=1,
    nome="João",
    telefone="99999-9999",
    email="joao@exemplo.com",
    endereco=endereco,
    sexo=Sexo.MASCULINO,
    estadoCivil=Estado_Civil.SOLTEIRO,
    dataNascimento="01/01/1980",
    cpf="111.111.111-11",
    rg="12345678",
    matricula="1234",
    setor=Setor.JURIDICO,
    salario=8000.0,
    oab="123456"
)

# Imprimir informações do advogado
print(advogado)
