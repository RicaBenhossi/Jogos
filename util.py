def cabecalho_jogo(nome_jogo: str):
    print("*" * 33)
    print(f"Bem vindo ao jogo {nome_jogo.upper()}!")
    print("*" * 33)

def seleciona_qtd_tentativas() -> str:
    print("Qual o nível de dificuldade?")
    while True:
        print("(1) Fácil | (2) Médio | (3) Difícil | (0) Sair")

        try:
            nivel = int(input("Nível escolhido: ").strip()[0])
        except ValueError:
            print(f"O nível {nivel} digitado não é um nível válido. Digite um número entre 1 e 3.")
            continue

        if (not (nivel in range(0, 4))):
            print("Nível inválido. Seleciona um nível entre 1 e 3.")
        elif (nivel == 0):
            print("Até a próxima!")
            exit()
        else:
            break

    if (nivel == 1):
        return 10
    elif (nivel == 2):
        return 6
    else:
        return 3

