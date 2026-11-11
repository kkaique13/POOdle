from abc import ABC, abstractmethod
class Cliente(ABC):
    def __init__(self, nome:str, dataNascimento:str, endereco:str) -> None:
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__endereco = endereco
        self.listaCarteiras = []
    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, nome:str) -> None:
        self.__nome = nome
    
    @property
    def dataNascimento(self) -> str:
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento:str) -> None:
        self.__dataNascimento = dataNascimento
    
    @property
    def endereco(self) -> str:
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco:str) -> None:
        self.__endereco = endereco
    
    @abstractmethod
    def cadastrarCarteira(self, carteira) -> None:
        self.listaCarteiras.append(carteira)