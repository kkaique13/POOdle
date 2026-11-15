# Função para limpar a tela do terminal
def limpar():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')