from abc import ABC, abstractmethod
class Cliente(ABC):
    # Método construtor da classe Cliente
    def __init__(self, nome:str, dataNascimento:str, endereco:str) -> None:
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__endereco = endereco
        self.listaCarteiras = []
        
    # Propriedade para acessar o nome do cliente
    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome
    
    # Propriedade para acessar a data de nascimento do cliente
    @property
    def dataNascimento(self) -> str:
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento:str) -> None:
        self.__dataNascimento = dataNascimento
    
    # Propriedade para acessar o endereço do cliente
    @property
    def endereco(self) -> str:
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco:str) -> None:
        self.__endereco = endereco
    
    # Método abstrato para obter o documento do cliente (CPF ou CNPJ)
    @abstractmethod
    def getDocumento(self) -> str:
        pass
    
    # Método para cadastrar uma carteira no cliente
    def cadastrarCarteira(self, carteira) -> None:
        self.listaCarteiras.append(carteira)
    
    # Método abstrato para retornar os dados do cliente
    @abstractmethod
    def retornaDados(self) -> str:
        pass