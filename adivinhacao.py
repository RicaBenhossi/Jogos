import random as rnd
import util


def jogar():
    util.cabecalho_jogo("adivinhação")
    maximo_de_tentativas = util.seleciona_qtd_tentativas()

    numero_secreto = rnd.randrange(1, 101)
    pontos = 1000

    print(f"Você tem {maximo_de_tentativas} chances. Boa sorte!")
    for rodada_atual in range(1, maximo_de_tentativas + 1):
        print(f"Rodada {rodada_atual} de {maximo_de_tentativas}.")
        chute = get_chute_valido()

        print(f"Seu chute foi {chute}.")

        acertou = (chute == numero_secreto)
        chute_maior = (chute > numero_secreto)

        if(acertou):
            print("Você acertou :)")
            print(f"Seu score foi de: {pontos}")
            break
        else:
            print('-' * 120)
            print("Você errou :(")
            print(f"Seu chute foi {('maior' if chute_maior else 'menor')} que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

        if (rodada_atual > 3):
            print("Você perdeu!!!")

    print("FIM DO JOGO.")


def get_chute_valido() -> int:
    while True:
        chute_lido = input("\ndigite o seu palpite (número entre 1 e 100): ")
        if (not chute_lido):
            print("Você deve digitar um números entre 1 e 100.")
            continue
        try:
            chute = int(chute_lido.strip()[0])
        except Exception:
            print("Palpite inválido. Você deve digitar um números entre 1 e 100.")
            continue

        if (not (1 <= chute <= 100)):
            print("Palpite inválido. Você deve digitar um números entre 1 e 100.")
            continue
        else:
            return chute


if (__name__ == "__main__"):
    jogar()
