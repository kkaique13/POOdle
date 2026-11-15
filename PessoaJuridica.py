from Cliente import Cliente

class PessoaJuridica(Cliente):
    def __init__(self, nome:str, endereco:str, cnpj:str) -> None:
        super().__init__(nome, "", endereco)
        self.__cnpj = cnpj
    
    @property
    def cnpj(self) -> str:
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, cnpj:str) -> None:
        self.__cnpj = cnpj
    
    def getDocumento(self) -> str:
        return self.cnpj
    
    def tipoSociedade(self) -> str:
        nomeUp = self.nome.upper().strip()
        if nomeUp.endswith("LTDA"):
            return "Sociedade Limitada"
        if nomeUp.endswith("S/A") or nomeUp.endswith("SA"):
            return "Sociedade Anônima"
        return "Indefinido: Consulte o Gerente para Regularizar a Situação"
    
    def retornaDados(self) -> str:
        return f"Nome: {self.nome}; \n Endereço: {self.endereco}; \n CNPJ: {self.cnpj}; \n Tipo de Sociedade: {self.tipoSociedade()}\U0001F60E \n"