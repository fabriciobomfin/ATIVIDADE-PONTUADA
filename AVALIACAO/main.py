from models.advogado import Advogado
from models.endereco import Endereco
from models.enums.estado_civil import Estado_Civil
from models.enums.setor import Setor
from models.enums.sexo import Sexo

def main():
    # Criando um endereço para o advogado
    endereco = Endereco("Rua A", 123, "Apto 101", "12345-678", "Cidade A", "SP")
    
    # Criando um advogado
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
    
    # Exibindo informações do advogado
    print(str(advogado))

if __name__ == "__main__":
    main()
