# Jogo da Velha
ex_tabuleiro = [['X O X'], ['O X O'], ['X O X']]
for x in range(len(ex_tabuleiro)):
    print(ex_tabuleiro[x])

print("Preencha os campos _________ com simbolos X, O ou _ para deixar em branco")
linha = input("Digite: ").upper()
if len(linha) < 9 or len(linha) > 9:
    print('Tamanho inválido')
else:
    print(f"""
    ---------
    | {linha[0]} {linha[1]} {linha[2]} |
    | {linha[3]} {linha[4]} {linha[5]} |
    | {linha[6]} {linha[7]} {linha[8]} |
    ---------
    """)


