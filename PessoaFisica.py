from Cliente import Cliente
from datetime import datetime

class PessoaFisica(Cliente):
    # Método construtor da classe PessoaFisica
    def __init__(self, nome:str, dataNascimento:str, endereco:str, cpf:str) -> None:
        super().__init__(nome, dataNascimento, endereco)
        self.__cpf = cpf
    
    # Propriedade para acessar o CPF
    @property
    def cpf(self) -> str:
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf:str) -> None:
        self.__cpf = cpf
        
    # Método para pegar o documento (CPF) do cliente
    def getDocumento(self) -> str:
        return self.cpf
    
    # Método para verificar se o cliente é maior de idade
    def maiorLegal(self, data:str) -> bool:
        try:
            d, m, a = map(int, data.split("/"))
            dn, mn, an = map(int, self.dataNascimento.split("/"))
        except (ValueError, AttributeError):
            return False
        idade = a - an
        if (m, d) < (mn, dn):
            idade -= 1
        return idade >= 18
    
    # Método para retornar os dados do cliente
    def retornaDados(self) -> str:
        hoje = datetime.now().strftime("%d/%m/%Y")
        return f"Nome: {self.nome};\n Data de Nascimento: {self.dataNascimento}; \n Endereço: {self.endereco}; \n CPF: {self.cpf}; Maior de idade: {self.maiorLegal(hoje)}\U0001F60E \n"