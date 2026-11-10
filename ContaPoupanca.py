from Conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, numero: str, titular: str, saldo: float, rendimento:float) -> None:
        super().__init__(numero, titular, saldo);
        self.__rendimento = rendimento;
    
    @property
    def rendimento(self) -> float:
        return self.__rendimento
    @rendimento.setter
    def rendimento(self, rendimento:float) -> None:
        if (rendimento < 0):
            print("Não foi possível alterar o rendimento! \U0001FAE4");
        else:
            self.__rendimento = rendimento;
    
    def sacar(self, valor:float) -> None:
        if (valor > self.saldo):
            print("Não foi possível sacar esse valor! \U0001F641");
        else:
            self.saldo -= valor;
    
    def acaoRendimento(self) -> None:
        self.saldo *= self.__rendimento;