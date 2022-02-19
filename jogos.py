import forca
import adivinhacao

def main():
    print("*"*33)
    print("Escolha o seu jogo")
    print("*"*33)

    print("Qual Jogo deseja Jogar?")
    while True:
        print("(1) Adivinhação | (2) Forca | (0) Sair")

        jogo = int(input("Jogo escolhido: "))
        if (not (jogo in range(0, 3))):
            print("Seleciona um jogo válido.")
        elif (jogo == 0):
            print("Até a próxima!")
            exit()
        else:
            break
    if (jogo == 1):
        print("Jogando ADIVINHAÇÃO")
        adivinhacao.jogar()
    elif(jogo == 2):
        print("Jogando FORCA")
        forca.jogar()
    print("JOGO ENCERRADO.")

main()