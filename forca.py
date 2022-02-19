import random as rnd
import util as utl
import json


def jogar():
    utl.cabecalho_jogo("forca")
    palavra_secreta = define_palavra_secreta()
    acertou = False
    enforcou = False
    resposta = inicializa_letras_acertadas(palavra_secreta)

    erros = 0
    while (not acertou and not enforcou):
        print_resposta(resposta)
        chute = get_chute_valido(resposta)
        if (chute in palavra_secreta):
            preenche_lacunas(palavra_secreta, chute, resposta)
            acertou = not ("_" in resposta)
        else:
            erros += 1
            desenha_forca(erros)
            enforcou = (erros == 7)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("-" * 120)
    print("FIM DO JOGO.")


def define_palavra_secreta() -> str:
    palavras_forca = carrega_palavras_do_arquivo()
    temas_disponiveis = list(tema for tema in palavras_forca.keys())
    temas_disponiveis.insert(0, "Todas os temas")
    print("Selecione um tema para sortear a palavra secreta.")
    for indice, tema in enumerate(temas_disponiveis):
        print(f"[{indice}] - {tema.strip().upper()}")
    while True:
        try:
            tema_escolhido = int((input("Tema escolhido: ")).strip())
        except ValueError:
            print("Caracter digitádo é inválido. Digite um número inteiro.")
            continue
        else:
            if (not (tema_escolhido in range(len(temas_disponiveis)))):
                print("Digite uma opção válido.")
                continue
            else:
                break

    if (tema_escolhido > 0):
        sorteio_temas = list(tema.strip().upper() for tema in palavras_forca[temas_disponiveis[tema_escolhido]])
    else:
        sorteio_temas = list()
        for palavras in palavras_forca.values():
            for palavra in palavras:
                sorteio_temas.append(palavra)
    return sorteio_temas[rnd.randrange(len(sorteio_temas) - 1)]


def carrega_palavras_do_arquivo() -> dict:
    with open("forca_palavras.json", mode="r", encoding="utf8") as arquivo:
        load_json = dict(json.load(arquivo))

    return {key: [key_dict.upper() for key_dict in load_json[key]] for key in load_json}


def print_resposta(resposta: str):
    print("Palpites:\n")
    for letra in resposta:
        print(letra, end=" ")
    print("\n")


def preenche_lacunas(palavra: str, chute: str, resposta: list) -> list():
    index = 0
    for letra in palavra:
        if (letra == chute):
            resposta[index] = letra
        index += 1
    return resposta


def get_chute_valido(resposta: list) -> str:
    while True:
        print("Caso seja digitada mais de uma letra, será considerada apenas a primeira letra da palavra.")
        chute_lido = input("Qual a letra você escolhe? \n")
        if (not chute_lido):
            print("Chute inválido. Digite ao menos uma letra.")
            continue
        chute = chute_lido.upper().strip()[0]
        if (chute in (resposta)):
            print(f"Você já chutou a letra {chute}. Escolha outra letra.")
        elif (not chute.isalpha()):
            print("Chute inválido. O caracter escolhido não é uma letra.")
        else:
            return chute


def inicializa_letras_acertadas(palavra: str) -> list:
    return [("-" if letra == " " else "_") for letra in palavra]


def imprime_mensagem_perdedor(palavra_secreta):
    print("Você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________      ")
    print("   /               \     ")
    print("  /                 \    ")
    print("//                   \/\ ")
    print("\|   XXXX     XXXX   | / ")
    print(" |   XXXX     XXXX   |/  ")
    print(" |   XXX       XXX   |   ")
    print(" |                   |   ")
    print(" \__      XXX      __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | I I I I I I I |     ")
    print("   |  I I I I I I  |     ")
    print("   \_             _/     ")
    print("     \_         _/       ")
    print("       \_______/         ")


def imprime_mensagem_vencedor():
    print("Parabéns, você venceu!!!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == "__main__"):
    jogar()
