class Carteira:
    # Método construtor da classe Carteira
    def __init__(self, investimento:str) -> None:
        self.__investimento = investimento;
        self.__listaContas = [];
    
    # Propriedade para acessar o tipo de investimento
    @property
    def investimento(self) -> str:
        return self.__investimento
    @investimento.setter
    def investimento(self, investimento:str) -> None:
        self.__investimento = investimento;
    
    # Propriedade para acessar a lista de contas da carteira
    @property
    def listaContas(self) -> list:
        return self.__listaContas
    
    # Método para adicionar uma conta à carteira (limite de 3 contas)
    def addConta(self, objConta:object) -> None:
        if (len(self.__listaContas) == 3):
            print("Não é possível ter mais que 3 contas! \U0001F621")
        else:
            self.__listaContas.append(objConta);
    
    # Método para retornar as contas com saldo negativo
    def contasNegativas(self) -> list:
        listaNegativas = []
        for continha in self.listaContas:
            if continha.saldo < 0:
                listaNegativas.append(continha);
        if len(listaNegativas) == 0:
            print("Nenhuma conta está negativa nessa carteira! \U0001F929")
        return listaNegativas