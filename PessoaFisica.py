from Cliente import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome:str, dataNascimento:str, endereco:str, cpf:str) -> None:
        super().__init__(nome, dataNascimento, endereco)
        self.__cpf = cpf
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf:str) -> None:
        self.__cpf = cpf

    def getDocumento(self) -> str:
        return self.cpf
    
    def maiorLegal(self) -> bool:
        from datetime import datetime
        data_nascimento = datetime.strptime(self.dataNascimento, "%d/%m/%Y")
        idade = (datetime.now() - data_nascimento).days // 365
        return idade >= 18
    
    def retornaDados(self) -> str:
        return f"Nome: {self.nome};\n Data de Nascimento: {self.dataNascimento}; \n Endereço: {self.endereco}; \n CPF: {self.cpf}; Maior de idade: {self.maiorLegal()}\U0001F60E \n"