import jogo as jogo_forca
import bd

def mostrar_menu():
    print("="*30)
    print(" " * 7 + "JOGO DA FORCA")
    print("="*30)
    print("\n 1 - Jogar")
    print(" 2 - Score")
    print(" 3 - Sair \n")
    print("="*30)

while True:
    conn = bd.conectar()
    bd.criar_tabela(conn)

    mostrar_menu()
    opcao = int(input("Escolha uma opção (1-3): "))
    if opcao == 1:
        print("Iniciando o jogo...")
        jogo_forca.iniciar_jogo()
        input("Pressione Enter para voltar ao menu...")

    elif opcao == 2:
        print("SCORE:")
        dados = bd.listar_dados()
        if not dados:
            print('Score Vazio.')
        else:
            i = 1
            for jogador in dados:
                print(f'{i} - > {jogador[1]}, Pontuacao: {jogador[2]}')
                i += 1
        input('Digite qualquer tecla para continuar.')

    elif opcao == 3:
        print("Saindo do jogo...")
        break
    else:
        print("Opção inválida. Tente novamente.")


bd.desconectar(conn)