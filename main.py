# Jogo da Velha
ex_tabuleiro = [['X O X'], ['O X O'], ['X O X']]
for x in range(len(ex_tabuleiro)):
    print(ex_tabuleiro[x])

print("Preencha os campos _________ com simbolos X, O ou _ para deixar em branco")
linha = input("Digite: ").upper()
if len(linha) < 9 or len(linha) > 9:
    print('Tamanho inválido')
else:
    print("Preencha os campos _________ com simbolos X, O ou _ para deixar em branco")
    linha = input("Digite: ").upper()
    if len(linha) < 9 or len(linha) > 9:
        print('Tamanho inválido')
    tabuleiro = [[linha[0], linha[1], linha[2]], [linha[3], linha[4], linha[5]], [linha[6], linha[7], linha[8]]]
    for lista in tabuleiro:
        print(lista)
    # linhas verticais
    if tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X":
        print('vitoria do X')
    elif tabuleiro[0][0] == 'O' and tabuleiro[1][0] == 'O' and tabuleiro[2][0] == 'O':
        print('vitoria do O')
    elif tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X":
        print('vitoria do X')
    elif tabuleiro[0][1] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][1] == 'O':
        print('vitoria do O')
    elif tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X":
        print('vitoria do X')
    elif tabuleiro[0][2] == 'O' and tabuleiro[1][2] == 'O' and tabuleiro[2][2] == 'O':
        print('vitoria do O')







