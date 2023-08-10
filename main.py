# Importa a função "modificar_letra" do módulo "cores_uso"

from cores_uso import modificar_letra
# Define o símbolo "X" vermelho e o símbolo "O" azul, usando as funções do módulo "modificar_letra"

xis = modificar_letra.letra_VERMELHA + 'X' + modificar_letra.limpar_cores
bolinha = modificar_letra.letra_AZUL + 'O' + modificar_letra.limpar_cores

# Lista de posições iniciais do jogo

posicoes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Cria uma matriz "exemplo" com as primeiras posições
exemplo = [[posicoes[0], posicoes[1], posicoes[2]],
           [posicoes[3], posicoes[4], posicoes[5]],
           [posicoes[6], posicoes[7], posicoes[8]]]

# Atualiza as posições iniciais para "_" usando um loop
for num in posicoes:
    posicoes[num - 1] = "_"

# Lista de números representando as posições do tabuleiro
posicoes_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Solicita o nome dos jogadores
nom_jog1 = input("Nome jogador 1: ").title()
nom_jog2 = input("Nome jogador 2: ").title()

# Loop para solicitar o símbolo do jogador 1
while True:
    simbolo_jog1 = input(
        f"Escolha entre {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} ou {modificar_letra.letra_AZUL}O{modificar_letra.limpar_cores} {nom_jog1}: ").upper()
    if simbolo_jog1 not in ["X", 'O']:
        print('Apenas X ou O')
    else:
        break

# Define o símbolo do jogador 2 com base na escolha do jogador 1
simbolo_jog2 = ''
if simbolo_jog1 == 'X':
    simbolo_jog1 = xis
    simbolo_jog2 = bolinha
elif simbolo_jog1 == 'O':
    simbolo_jog1 = bolinha
    simbolo_jog2 = xis

# Cria dicionários para representar os jogadores
jogador1 = {nom_jog1: simbolo_jog1}
jogador2 = {nom_jog2: simbolo_jog2}

# Imprime os nomes e símbolos dos jogadores
for nome, simbo in jogador1.items():
    nom_jog1 = nome
    simbolo_jog1 = simbo
    print(f"{nome}: {simbo}")
for nome, simbol in jogador2.items():
    nom_jog2 = nome
    simbolo_jog2 = simbol
    print(f"{nome}: {simbol}")

# Define a variável "ativo" como True para controlar o fluxo do jogo
ativo = True

# Inicializa a variável "x" com 0
x = 0

# Loop principal do jogo da velha
while x < 19:

    # Formata o tabuleiro de jogo com as posições atuais
    jogo_velha_formatado = f"""
        ---------
        | {posicoes_nums[0]} {posicoes_nums[1]} {posicoes_nums[2]} |
        | {posicoes_nums[3]} {posicoes_nums[4]} {posicoes_nums[5]} |
        | {posicoes_nums[6]} {posicoes_nums[7]} {posicoes_nums[8]} |
        ---------
        """
    # Imprime o tabuleiro formatado
    print(jogo_velha_formatado)
    # Verifica se o número de jogadas excedeu 9, encerrando o jogo
    if x > 9:
        ativo = False
        break
    # Loop para controlar as jogadas dos jogadores
    while ativo:
        if x % 2 == 0:
            while True:
                while True:
                    try:
                        posicao = int(input(f"Posicão para colocar o {simbolo_jog1} {nom_jog1}: "))
                    except ValueError:
                        print("\033[31mApenas números positivos entre 1 e 9\033[m")
                    else:
                        if posicao not in range(1, 10):
                            print("\033[31mPosição inexistente!\033[m")
                        elif posicoes_nums[posicao - 1] == "O":
                            print("\033[31mPosição já preenchida\033[m")
                        else:
                            # Preenche a posição no tabuleiro com o símbolo do jogador 1
                            if simbolo_jog1 == xis:
                                posicoes_nums[posicao - 1] = xis
                                break
                            else:
                                posicoes_nums[posicao - 1] = bolinha
                                break
                break
        elif x % 2 == 1:
            while True:
                while True:
                    try:
                        posicao = int(input(f"Posicão para colocar o {simbolo_jog2} {nom_jog2}: "))
                    except ValueError:
                        print("\033[31mApenas números\033[m")
                    else:
                        if posicao not in range(1, 10):
                            print("\033[31mPosição inexistente!\033[m")
                        elif posicoes_nums[posicao - 1] == 'X':
                            print("\033[31mPosição já preenchida\033[m")
                        else:
                            # Preenche a posição no tabuleiro com o símbolo do jogador 2
                            if simbolo_jog2 == xis:
                                posicoes_nums[posicao - 1] = xis
                                break
                            else:
                                posicoes_nums[posicao - 1] = bolinha
                                break
                break
        # Criação da matriz do jogo da velha com base nas posições atuais
        jogo_velha = [[posicoes_nums[0], posicoes_nums[1], posicoes_nums[2]],
                      [posicoes_nums[3], posicoes_nums[4], posicoes_nums[5]],
                      [posicoes_nums[6], posicoes_nums[7], posicoes_nums[8]]]

        # verticais
        if jogo_velha[0][0] == f"{xis}" and jogo_velha[1][0] == f"{xis}" and jogo_velha[2][0] == f"{xis}":
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")

                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")

                else:
                    continue
            x += 10

        elif jogo_velha[0][1] == f"{xis}" and jogo_velha[1][1] == f"{xis}" and jogo_velha[2][1] == f"{xis}":
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[0][2] == f"{xis}" and jogo_velha[1][2] == f"{xis}" and jogo_velha[2][2] == f"{xis}":
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[0][0] == f'{bolinha}' and jogo_velha[1][0] == f'{bolinha}' and jogo_velha[2][0] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")

                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue
            x += 10
        elif jogo_velha[0][1] == f'{bolinha}' and jogo_velha[1][1] == f'{bolinha}' and jogo_velha[2][1] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[0][2] == f'{bolinha}' and jogo_velha[1][2] == f'{bolinha}' and jogo_velha[2][2] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue
            x += 10

        # linhas horizontais
        elif jogo_velha[0][0] == f'{xis}' and jogo_velha[0][1] == f'{xis}' and jogo_velha[0][2] == f'{xis}':
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")

                    x += 10
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                else:
                    continue
            x += 10

        elif jogo_velha[1][0] == f'{xis}' and jogo_velha[1][1] == f'{xis}' and jogo_velha[1][2] == f'{xis}':
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[2][0] == f'{xis}' and jogo_velha[2][1] == f'{xis}' and jogo_velha[2][2] == f'{xis}':
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[0][0] == f'{bolinha}' and jogo_velha[0][1] == f'{bolinha}' and jogo_velha[0][2] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[1][0] == f'{bolinha}' and jogo_velha[1][1] == f'{bolinha}' and jogo_velha[1][2] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue
            x += 10
        elif jogo_velha[2][0] == f'{bolinha}' and jogo_velha[2][1] == f'{bolinha}' and jogo_velha[2][2] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        # linhas diagonais
        elif jogo_velha[0][0] == f'{xis}' and jogo_velha[1][1] == f'{xis}' and jogo_velha[2][2] == f'{xis}':
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[0][0] == f'{bolinha}' and jogo_velha[1][1] == f'{bolinha}' and jogo_velha[2][2] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                else:
                    continue

            x += 10
        elif jogo_velha[0][2] == f'{xis}' and jogo_velha[1][1] == f'{xis}' and jogo_velha[2][0] == f'{xis}':
            for nome, sim in jogador1.items():
                if sim == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome} ganhou!")
                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == xis:
                    print(f'Vitória do {xis}')
                    print(f"{nome2} ganhou!")
                    print(30)

                else:
                    continue

            x += 10
        elif jogo_velha[0][2] == f'{bolinha}' and jogo_velha[1][1] == f'{bolinha}' and jogo_velha[2][0] == f'{bolinha}':
            for nome, sim in jogador1.items():
                if sim == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome} ganhou!")
                    print(31)

                else:
                    continue
            for nome2, sim2 in jogador2.items():
                if sim2 == bolinha:
                    print(f'Vitória do {bolinha}')
                    print(f"{nome2} ganhou!")
                    print(32)

                else:
                    continue
        break
    x += 1
