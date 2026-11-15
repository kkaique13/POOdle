from Conta import Conta

class ContaCorrente(Conta):
    
    contador = 0;
    
    # Método construtor da classe ContaCorrente
    def __init__(self, numero: str, titular: str, saldo: float) -> None:
        super().__init__(numero, titular, saldo);
        self.__limite = 2000.0;
        ContaCorrente.contador += 1;
    
    # Propriedade para acessar o limite da conta
    @property
    def limite(self) -> float:
        return self.__limite
    @limite.setter
    def limite(self, limite:float) -> None:
        if (limite < 0):
            print("Não foi possível alterar o limite! \U0001FAE4");
        else:
            self.__limite = limite;
    
    # Método para retornar o saldo total (saldo + limite)
    def saldoTotal(self) -> float:
        return self.saldo + self.__limite
    
    # Método para sacar um valor da conta corrente (usando limite se necessário)
    def sacar(self, valor:float) -> None:
        if valor > self.saldoTotal():
            print("Não foi possível sacar esse valor! \U0001FAE4")
            return
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            restante = valor - self.saldo
            self.saldo = 0
            self.__limite -= restante
    
    # Método para retornar os dados da conta corrente
    def retornaDados(self) -> str:
        return (super().retornaDados() + f" Limite: {self.limite};\n Saldo total (saldo+limite): {self.saldoTotal()}\n")
