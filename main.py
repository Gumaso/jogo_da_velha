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
    simbolo_jog1 = input(
        f"Escolha entre {modificar_letra.letra_VERMELHA}X{modificar_letra.limpar_cores} ou {modificar_letra.letra_AZUL}O{modificar_letra.limpar_cores} {nom_jog1}: ").upper()
    if simbolo_jog1 not in ["X", 'O']:
        print('Apenas X ou O')
    else:
        break
simbolo_jog2 = ''
if simbolo_jog1 == 'X':
    simbolo_jog1 = xis
    simbolo_jog2 = bolinha
elif simbolo_jog1 == 'O':
    simbolo_jog1 = bolinha
    simbolo_jog2 = xis
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
ativo = True
x = 0
while x < 19:
    jogo_velha_formatado = f"""
        ---------
        | {posicoes_nums[0]} {posicoes_nums[1]} {posicoes_nums[2]} |
        | {posicoes_nums[3]} {posicoes_nums[4]} {posicoes_nums[5]} |
        | {posicoes_nums[6]} {posicoes_nums[7]} {posicoes_nums[8]} |
        ---------
        """
    print(jogo_velha_formatado)
    if x > 9:
        ativo = False
        break

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
                            if simbolo_jog2 == xis:
                                posicoes_nums[posicao - 1] = xis
                                break
                            else:
                                posicoes_nums[posicao - 1] = bolinha
                                break
                break

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
