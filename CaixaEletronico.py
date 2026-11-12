from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Carteira import Carteira
from func import limpar

# Método para cadastrar uma conta
def cadastrarConta(carteira: Carteira) -> None:
    num = input("Informe o número da conta: \n").strip()
    tit = input("\nInforme o nome do titular: \n").strip()

    try:
        sal = float(input("\nQual o valor do saldo inicial? \n"))
        tip = input("\nConta Corrente (C);\n Conta Poupança (P):\n")
        if tip.lower() == "c":
            conta = ContaCorrente(num, tit, sal)
        elif tip.lower() == "p":
            ren = float(input("\nQual o rendimento mensal (%)? \n"))
            conta = ContaPoupanca(num, tit, sal, ren)
        else:
            print("\nTipo de conta inválido!")
            return
        
        carteira.addConta(conta)
        print("\nConta cadastrada com sucesso!")
    
    except ValueError as erro:
        print(f"Não foi possível cadastrar a conta: {erro}")

# Método para cadastrar uma carteira
def cadastrarCarteira(cliente=None) -> Carteira:
    inv = input("Qual o tipo de investimento? \n")
    carteira = Carteira(inv)
    if cliente is not None:
        cliente.cadastrarCarteira(carteira)
    resposta = input("Deseja cadastrar uma conta? (s/n) \n")

    while resposta.lower() == "s":
        cadastrarConta(carteira)
        if len(carteira.listaContas) >= 3:
            print("Limite de contas atingido!")
            break
        resposta = input("Deseja cadastrar outra conta? (s/n) \n")
    return carteira

# main
def main() -> None:
    listaCarteiras = []
    listaClientes = []

    print("Bem-vindo ao POOdle Bank! 😊")

    while True:
        print("\n(01) Cadastrar um novo cliente")
        print("(02) Cadastrar uma nova carteira")
        print("(03) Listar as contas de uma carteira")
        print("(04) Pesquisar um cliente")
        print("(05) Sair do programa\n")

        try:
            opcao = int(input("Informe a opção desejada: \n"))

            match opcao:

                # Cadastro de cliente
                case 1:
                    nom = input("Digite o nome do cliente: \n")
                    end = input("Digite o endereço do cliente: \n")
                    tipo = input("Pessoa Física (PF);\nPessoa Jurídica (PJ):\n")

                    try:
                        if tipo.lower() == "pf":
                            dat = input("Digite a data de nascimento (dd/mm/aaaa): \n")
                            cpf = input("Digite o CPF: \n")
                            cliente = PessoaFisica(nom, dat, end, cpf)
                            limpar()
                        
                        elif tipo.lower() == "pj":
                            cnpj = input("Digite o CNPJ: \n")
                            sociedade = input("Digite o tipo de sociedade: \n")
                            cliente = PessoaJuridica(nom, end, cnpj, sociedade)
                            limpar()
                        
                        else:
                            limpar()
                            print("Tipo de cliente inválido!")
                            continue

                        listaClientes.append(cliente)
                        print("Cliente cadastrado com sucesso!")
                        resposta = input("Deseja cadastrar uma carteira para esse cliente? (s/n) \n")
                        if resposta.lower() == "s":
                            limpar()
                            carteira = cadastrarCarteira(cliente)
                            listaCarteiras.append(carteira)

                    except ValueError as erro:
                        print(f"Erro no cadastro: {erro}")

                # Cadastro de carteira
                case 2:
                    try:
                        carteira = cadastrarCarteira()
                        listaCarteiras.append(carteira)
                        limpar()
                        print("Carteira cadastrada com sucesso!")

                    except ValueError as erro:
                        print(f"Erro no cadastro: {erro}")

                # Listagem de contas
                case 3:
                    inv = input("Informe o tipo de investimento desejado: \n")

                    carteirasEncontradas = [carteira for carteira in listaCarteiras if carteira.investimento.lower() == inv.lower()]
                    if not carteirasEncontradas:
                        print("Não existe carteira desse tipo!")
                        continue

                    for carteira in carteirasEncontradas:
                        print(f"\nCarteira: {carteira.investimento}")
                        if not carteira.listaContas:
                            print("Essa carteira não possui contas!")
                            continue

                        for conta in carteira.listaContas:
                            print(conta.retornaDados())
                
                # Pesquisar um cliente (Consertar)
                case 4:
                    cli = input("Digite o número do documento do cliente: ")
                    for clientinho in listaClientes:
                        for carteirinha in clientinho.listaCarteiras:
                            for continha in carteirinha.listaContas:
                                if cli == continha.numero:
                                    print("Cliente encontrado!")
                                    print(f"Cliente: {clientinho.nome}\n")
                                    print(f"Carteiras: {clientinho.listaCarteiras}\n")
                    print("Cliente não foi encontrado!")
                    
                # Saída
                case 5:
                    limpar()
                    print("Volte sempre ao POOdle Bank! 😊")
                    break
                case _:
                    print("Opção inválida!")
        except ValueError:
            print("Informe uma opção numérica válida!")

if __name__ == "__main__":
    main()