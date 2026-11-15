from abc import ABC, abstractmethod
class Conta(ABC):
    # Método construtor da classe Conta
    def __init__(self, numero:str, titular:str, saldo:float) -> None:
        self.__numero = numero;
        self.__titular = titular;
        self.__saldo = saldo;
    
    # Propriedade para acessar o número da conta
    @property
    def numero(self) -> str:
        return self.__numero
    
    # Propriedade para acessar o nome do titular (primeiro e último nome)
    @property
    def titular(self) -> str:
        partesNomes = self.__titular.split(" ");
        tamanho = len(partesNomes);
        if tamanho == 1:
            return partesNomes[0]
        return partesNomes[0] + " " + partesNomes[tamanho - 1]
    @titular.setter
    def titular(self, titular:str) -> None:
        self.__titular = titular;
    
    # Propriedade para acessar o saldo da conta
    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo) -> None:
        if (saldo < 0):
            print("Não foi possível alterar o saldo! \U0001FAE4");
        else:
            self.__saldo = saldo;
    
    # Método abstrato para sacar um valor da conta
    @abstractmethod
    def sacar(self, valor:float) -> None:
        pass;
    
    # Método para depositar um valor na conta
    def depositar(self, valor:float) -> None:
        if (valor < 0):
            print("Não foi possível realizar o depósito! \U0001FAE4");
        else:
            self.__saldo += valor;
    
    # Método para retornar os dados da conta
    def retornaDados(self) -> str:
        return f"Número: {self.numero};\n Nome do titular: {self.titular}; \n Saldo da conta: {self.saldo}; \U0000263A \n"