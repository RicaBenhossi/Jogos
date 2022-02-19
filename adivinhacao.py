import random as rnd

def jogar():
    numero_secreto = rnd.randrange(1, 101)
    pontos = 1000

    print("*"*33)
    print("Bem vindo ao jogo de adivinhação!")
    print("*"*33)

    print("Qual o nível de dificuldade?")
    while True:
        print("(1) Fácil | (2) Médio | (3) Difícil | (0) Sair")

        nivel = int(input("Nível escolhido: "))
        if (not (nivel in range(0, 4))):
            print("Seleciona um nível válido.")
        elif (nivel == 0):
            print("Até a próxima!")
            exit()
        else:
            break

    if (nivel == 1):
        maximo_de_tentativas = 10
    elif (nivel == 2):
        maximo_de_tentativas = 6
    else:
        maximo_de_tentativas = 3

    print(f"Você tem {maximo_de_tentativas} chances. Boa sorte!")

    for rodada_atual in range(1, maximo_de_tentativas + 1):
        print(f"Rodada {rodada_atual} de {maximo_de_tentativas}.")
        chute = int(input("\ndigite o seu palpite (número entre 1 e 100)."))
        if (chute < 1 or chute > 100):
            print('Palpite inválido. Você deve digitar um números entre 1 e 100')
            continue

        print(f"Seu chute foi {chute}.")

        acertou = (chute == numero_secreto)
        chute_maior = (chute > numero_secreto)

        if(acertou):
            print("Você acertou :)")
            print(f"Pontuação: {pontos}")
            break
        else:
            print("Você errou :(")
            print(f"Seu chute foi {('maior' if chute_maior else 'menor')} que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

        if (rodada_atual > 3):
            print("Você perdeu!!!")

    print("FIM DO JOGO.")

if (__name__ == "__main__"):
    jogar()