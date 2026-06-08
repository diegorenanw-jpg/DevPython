import desenhos as d

palavra = input('Digite uma palavra secreta: ').lower().strip()

for x in range(50):
    print()

digitadas = []
acertos = []
erros = 0

while True:
    adivinha = d.imprimir_palavra_secreta(palavra, acertos)

    # * CONDIÇÃO DE VITORIA
    if adivinha == palavra:
        print('Você acertou!')
        break

    # * TENTATIVAS
    tentativa = input('\n Digite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Voce já usou essa letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')
    
    # Desenhando a forca
    d.imprimir_forca(erros)


    #CONDIÇÃO DE FIM DE JOGO
    if erros == 6:
        print('Enforcado!!')
        print(f'A palavra era {palavra}')
        break