from Cliente import Cliente

class PessoaJuridica(Cliente):
    def __init__(self, nome:str, dataNascimento:str, endereco:str, cnpj:str) -> None:
        super().__init__(nome, dataNascimento, endereco)
        self.__cnpj = cnpj
    
    @property
    def cnpj(self) -> str:
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj:str) -> None:
        self.__cnpj = cnpj
    
    def cadastrarCarteira(self, carteira) -> None:
        self.listaCarteiras.append(carteira)
    
    def tipoSociedade(self) -> str:
        pass
    
    def retornaDados(self) -> str:
        return f"Nome: {self.nome}; \n Data de nascimento: {self.dataNascimento}; \n Endereço: {self.endereco}; \n CNPJ: {self.cnpj}; \U0001F60E \n"