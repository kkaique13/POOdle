from Conta import Conta

class ContaCorrente(Conta):
    
    contador = 0;
    
    def __init__(self, numero: str, titular: str, saldo: float) -> None:
        super().__init__(numero, titular, saldo);
        self.__limite = 2000.0;
        ContaCorrente.contador += 1;
        
    @property
    def limite(self) -> float:
        return self.__limite
    @limite.setter
    def limite(self, limite:float) -> None:
        if (limite < 0):
            print("Não foi possível alterar o limite! \U0001FAE4");
        else:
            self.__limite = limite;

    def saldoTotal(self) -> float:
        return self.saldo + self.__limite

    def sacar(self, valor:float) -> None:
        if (valor > self.saldoTotal()):
            print("Não foi possível sacar esse valor! \U0001F641");
        else:
            if (valor <= self.saldo):
                self.saldo -= valor;
            else:
                self.limite = (valor - self.saldo);
                self.saldo = 0;