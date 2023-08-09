'''mostrar o jogo da velha com números nas posicões

criar um loop de que enquanto no jogo for diferente de X ou O
pegar  o nome do jogador1
jogador 2
depois o simbolo do jogador 1
simbolo do jogador 2

criar um loop para perguntar a posicao que o jogador um quer colocar seu simbolo
se nessa posicao tiver um X ou O dizer que está preenchido e mostrar as opções disponiveis
se ele dizer uma posicao valida, fazer o mesmo com o jogador dois

'''
from cores_uso import modificar_letra
xis = modificar_letra.letra_VERMELHA + 'X' + modificar_letra.limpar_cores
bolinha = modificar_letra.letra_AZUL + 'O' + modificar_letra.limpar_cores
posicoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exemplo = [[posicoes[0], posicoes[1], posicoes[2]], [posicoes[3], posicoes[4], posicoes[5]],
           [posicoes[6], posicoes[7], posicoes[8]]]
for num in posicoes:
    posicoes[num - 1] = "_"
posicoes_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nom_jog1 = input("Nome jogador 1: ").title()
nom_jog2 = input("Nome jogador 2: ").title()
while True:
    simbolo_jog1 = input(f"Escolha entre {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} ou {modificar_letra.letra_AZUL}O{modificar_letra.limpar_cores} {nom_jog1}: ").upper()
    if simbolo_jog1 not in ["X", 'O']:
        print('Apenas X ou O')
    else:
        break
if simbolo_jog1 == 'X':
    simbolo_jog1 = modificar_letra.letra_VERMELHA + simbolo_jog1 + modificar_letra.limpar_cores
elif simbolo_jog1 == 'O':
    simbolo_jog1 = modificar_letra.letra_AZUL + simbolo_jog1 + modificar_letra.limpar_cores
simbolo_jog2 = ''

if simbolo_jog1 == 'X':
    simbolo_jog2 = 'O'
elif simbolo_jog1 == 'O':
    simbolo_jog2 = 'X'
jogador1 = {nom_jog1: simbolo_jog1}
jogador2 = {nom_jog2: simbolo_jog2}
for nome, simbo in jogador1.items():
    nom_jog1 = nome
    simbolo_jog1 = simbo
    print(f"{nome}: {simbo}")
for nome, simbol in jogador2.items():
    nom_jog2 = nome
    simbolo_jog2 = simbol
    print(f"{nome}: {simbol}")
for x in range(10):
    jogo_velha_formatado = f"""
        ---------
        | {posicoes_nums[0]} {posicoes_nums[1]} {posicoes_nums[2]} |
        | {posicoes_nums[3]} {posicoes_nums[4]} {posicoes_nums[5]} |
        | {posicoes_nums[6]} {posicoes_nums[7]} {posicoes_nums[8]} |
        ---------
        """
    print(jogo_velha_formatado)
    while True:
        if x % 2 == 0:
            while True:
                while True:
                    try:
                        simbolo = int(input(f"Posicão para colocar o {modificar_letra.letra_VERMELHA}{simbolo_jog1}{modificar_letra.limpar_cores} {nom_jog1}: "))

                    except ValueError:
                        print("\033[31mApenas números positivos entre 1 e 9\033[m")
                    else:
                        if simbolo not in range(1, 10):
                            print("\033[31mPosição inexistente!\033[m")
                        elif posicoes_nums[simbolo - 1] == "O":
                            print("\033[31mPosição já preenchida\033[m")
                        else:
                            posicoes_nums[simbolo - 1] = modificar_letra.letra_VERMELHA + 'X' + modificar_letra.limpar_cores
                            break
                break
        elif x % 2 == 1:
            while True:
                while True:
                    try:
                        simbolo = int(input(f"Posicão para colocar o {modificar_letra.letra_AZUL}{simbolo_jog2}{modificar_letra.limpar_cores} {nom_jog2}: "))
                    except ValueError:
                        print("\033[31mApenas números\033[m")
                    else:
                        if simbolo not in range(1, 10):
                            print("\033[31mPosição inexistente!\033[m")
                        elif posicoes_nums[simbolo - 1] == 'X':
                            print("\033[31mPosição já preenchida\033[m")
                        else:
                            posicoes_nums[simbolo - 1] = modificar_letra.letra_AZUL + 'O' + modificar_letra.limpar_cores
                            break
                break
        jogo_velha = [[posicoes_nums[0], posicoes_nums[1], posicoes_nums[2]],
                      [posicoes_nums[3], posicoes_nums[4], posicoes_nums[5]],
                      [posicoes_nums[6], posicoes_nums[7], posicoes_nums[8]]]
        if jogo_velha[0][0] == "X" and jogo_velha[1][0] == "X" and jogo_velha[2][0] == "X":
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 1')
            break
        elif jogo_velha[0][1] == "X" and jogo_velha[1][1] == "X" and jogo_velha[2][1] == "X":
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 3 ')
            break
        elif jogo_velha[0][2] == "X" and jogo_velha[1][2] == "X" and jogo_velha[2][2] == "X":
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 5 ')
            break
        elif jogo_velha[0][0] == 'O' and jogo_velha[1][0] == 'O' and jogo_velha[2][0] == 'O':
            print('vitoria do {O} 2 ')
            break
        elif jogo_velha[0][1] == 'O' and jogo_velha[1][1] == 'O' and jogo_velha[2][1] == 'O':
            print('vitoria do {O} 4 ')
            break
        elif jogo_velha[0][2] == 'O' and jogo_velha[1][2] == 'O' and jogo_velha[2][2] == 'O':
            print('vitoria do {O}')
            break

        # linhas horizontais
        elif jogo_velha[0][0] == 'X' and jogo_velha[0][1] == 'X' and jogo_velha[0][2] == 'X':
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 6 ')
            break
        elif jogo_velha[1][0] == 'X' and jogo_velha[1][1] == 'X' and jogo_velha[1][2] == 'X':
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 7')
            break
        elif jogo_velha[2][0] == 'X' and jogo_velha[2][1] == 'X' and jogo_velha[2][2] == 'X':
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 8')
            break

        elif jogo_velha[0][0] == 'O' and jogo_velha[0][1] == 'O' and jogo_velha[0][2] == 'O':
            print('vitoria do {O} 9')
            break
        elif jogo_velha[1][0] == 'O' and jogo_velha[1][1] == 'O' and jogo_velha[1][2] == 'O':
            print('vitoria do {O} 10')
            break
        elif jogo_velha[2][0] == 'O' and jogo_velha[2][1] == 'O' and jogo_velha[2][2] == 'O':
            print('vitoria do {O} 11')
            break
        # linhas diagonais
        elif jogo_velha[0][0] == 'X' and jogo_velha[1][1] == 'X' and jogo_velha[2][2] == 'X':
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 12')
            break
        elif jogo_velha[0][0] == 'O' and jogo_velha[1][1] == 'O' and jogo_velha[2][2] == 'O':
            print('vitoria do {O} 13')
            break
        elif jogo_velha[0][2] == 'X' and jogo_velha[1][1] == 'X' and jogo_velha[2][0] == 'X':
            print(f'vitoria do {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} 14')
            break
        elif jogo_velha[0][2] == 'O' and jogo_velha[1][1] == 'O' and jogo_velha[2][0] == 'O':
            print('vitoria do {O} 15')
            break
        break

else:
    print("EMPATE")

