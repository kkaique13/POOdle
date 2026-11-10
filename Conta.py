from abc import ABC, abstractmethod
class Conta(ABC):
    def __init__(self, numero:str, titular:str, saldo:float) -> None:
        self.__numero = numero;
        self.__titular = titular;
        self.__saldo = saldo;
    
    @property
    def numero(self) -> str:
        return self.__numero
    
    @property
    def titular(self) -> str:
        partesNomes = self.__titular.split(" ");
        tamanho = len(partesNomes);
        return partesNomes[0] + " " + partesNomes[tamanho - 1]
    @titular.setter
    def titular(self, titular:str) -> None:
        self.__titular = titular;
        
    @property
    def saldo(self) -> float:
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo) -> None:
        if (saldo < 0):
            print("Não foi possível alterar o saldo! \U0001FAE4");
        else:
            self.__saldo = saldo;
    
    @abstractmethod
    def sacar(self, valor:float) -> None:
        pass;
    
    def depositar(self, valor:float) -> None:
        if (valor < 0):
            print("Não foi possível realizar o depósito! \U0001FAE4");
        else:
            self.__saldo += valor;
    
    def retornaDados(self) -> str:
        return f"Número: {self.numero};\n Nome do titular: {self.titular}; \n Saldo da conta: {self.saldo}; \U0000263A \n"