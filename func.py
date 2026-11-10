def limpar():
    """
    Limpa a tela do terminal.
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')