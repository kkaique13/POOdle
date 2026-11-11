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
    
    def retornaDados(self) -> str:
        return f"Nome: {self.nome}, Data de Nascimento: {self.dataNascimento}, Endereço: {self.endereco}, CPF: {self.cpf}"
    
    def cadastrarCarteira(self, carteira) -> None:
        self.listaCarteiras.append(carteira)

    def maiorLegal(self) -> bool:
        pass