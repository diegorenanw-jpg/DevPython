import desenhos as d
from random import choice
from os import path
import bd

def iniciar_jogo():
    caminho = path.join(path.dirname(__file__), 'palavras.txt')

    lista_palavras = list()
    arquivo = open(caminho, 'r')
    for linha in arquivo:
        linha = linha.strip()
        linha = linha.lower()
        lista_palavras.append(linha)

    arquivo.close()

    palavra_sorteada = choice(lista_palavras)


    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem esta jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)

        # * CONDIÇÃO DE VITORIA
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break

        # * TENTATIVAS
        tentativa = input('\n Digite uma letra: ').lower().strip()
        if tentativa in digitadas:
            print('Voce já usou essa letra!')
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')
        
        # Desenhando a forca
        score = d.imprimir_forca(erros)


        #CONDIÇÃO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!!')
            print(f'A palavra era {palavra_sorteada}')
            break

    bd.inserir_dado(nome, score)