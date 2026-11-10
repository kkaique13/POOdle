from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
from Carteira import Carteira
from func import limpar

if __name__ == "__main__":
    listaCarteiras = []
    print("Bem vindo ao POOdle Bank! \U0001F60A");
    
    while True:
        print("(01) Cadastrar uma nova carteira \U0001F601");
        print("(02) Listar as contas de uma carteira existente \U0001F643");
        print("(03) Sair do programa \U0001F614 \n");
        try:
            opcao = int(input("Informe a opção desejada \U0001F917: \n"))
            match opcao:
                case 1:
                    inv = input("Qual o tipo de investimento? \U0001F9D0 \n")
                    car = Carteira(inv)
                    resposta = input("Deseja cadastrar uma conta?(s/n) \U0001F9D0 \n")
                    
                    while resposta.lower() == "s":
                        num = input("Informe o número da conta \U0001F917: \n")
                        
                        tit = input("Informe o nome do titular \U0001F917: \n")
                        
                        try:
                            sal = float(input("Qual o valor do saldo inicial? \U0001F917 \n"))
                        except ValueError:
                            limpar()
                            print("Saldo inicial inválido! \U0001F621 \n")
                            continue
                        
                        tip = input("\nConta Corrente (C);\nConta Poupança(P);\U0001F917\n")
                        if tip.lower() == "c":
                            car.addConta(ContaCorrente(num, tit, sal))
                            
                        elif tip.lower() == "p":
                            try:
                                ren = float(input("Qual o rendimento mensal? \U0001F917\n"))
                            except ValueError:
                                limpar()
                                print("Rendimento mensal inválido! \U0001F621 \n")
                                continue
                            car.addConta(ContaPoupanca(num, tit, sal, ren))
                        else:
                            limpar()
                            print("Tipo de conta inválido! \U0001F621 \n")
                            continue
                        resposta = input("Deseja cadastrar uma conta?(s/n) \U0001F9D0 \n")
                        
                        if resposta.lower() == "n":
                            break
                    
                    listaCarteiras.append(car)
                    limpar()
                    print(f"Cadastro da carteira {inv} realizado com sucesso! \U0001F601 \n")
                    
                case 2:
                    inv = input("Informe o investimento desejado \U0001F9D0: \n")
                    achou = False
                    for carteirinha in listaCarteiras:
                        if carteirinha.investimento.lower() == inv.lower():
                            achou = True
                            limpar()
                            if carteirinha.listaContas == []:
                                print(f"Essa carteira {inv} não possui contas cadastradas! \U0001FAE4 \n")
                            else:
                                for continha in carteirinha.listaContas:
                                    print(continha.retornaDados());
                    if not achou:
                        limpar()
                        print("Não existe carteira do tipo informado! \U0001F641 \n")
                        
                case 3:
                    limpar()
                    break
                
                case _:
                    limpar()
                    print("Opção inválida! \U0001F621")
                    
        except ValueError:
            limpar()
            print("Opção inválida! \U0001F621")   
                
    print("Volte sempre ao POOdle Bank! \U0001F601")