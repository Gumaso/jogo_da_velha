class FundoCores():
    def __init__(self, fundo_PRETO, fundo_VERMELHO, fundo_VERDE, fundo_AMARELO, fundo_AZUL, fundo_ROXO, fundo_CIANO,
                 fundo_CINZA):
        self.fundo_PRETO = fundo_PRETO
        self.fundo_VERMELHO = fundo_VERMELHO
        self.fundo_VERDE = fundo_VERDE
        self.fundo_AMARELO = fundo_AMARELO
        self.fundo_AZUL = fundo_AZUL
        self.fundo_ROXO = fundo_ROXO
        self.fundo_CIANO = fundo_CIANO
        self.fundo_CINZA = fundo_CINZA

    def fundo_preto(self):
        return self.fundo_PRETO


class LetrasCores():
    def __init__(self, letra_PRETA, letra_VERMELHA, letra_VERDE, letra_AMARELA, letra_AZUL, letra_ROXA, letra_CIANO,
                 letra_CINZA, LIMPAR):
        self.letra_PRETA = letra_PRETA
        self.letra_VERMELHA = letra_VERMELHA
        self.letra_VERDE = letra_VERDE
        self.letra_AMARELA = letra_AMARELA
        self.letra_AZUL = letra_AZUL
        self.letra_ROXA = letra_ROXA
        self.letra_CIANO = letra_CIANO
        self.letra_CINZA = letra_CINZA
        self.limpar_cores = LIMPAR

class Exemplos(FundoCores, LetrasCores):
    def __init__(self, fundo_PRETO, fundo_VERMELHO, fundo_VERDE, fundo_AMARELO, fundo_AZUL, fundo_ROXO, fundo_CIANO,
                 fundo_CINZA):
        super().__init__(fundo_PRETO, fundo_VERMELHO, fundo_VERDE, fundo_AMARELO, fundo_AZUL, fundo_ROXO, fundo_CIANO,
                         fundo_CINZA)


    def colorindo_letras(self):
        print("Use a classe LetrasCores com o metódo  modificar_letra")
        print("Exemplo: modificar_letra.letra_VERDE + 'texto' ")
        print("Nesse caso todo texto restante será verde")
        print("Exemplo 2: modificar_letra.letra_PRETA + 'texto' + modificar.limpar_cores")
        print("No exemplo 2 o texto será preto até o modificar.limpar_cores")
        print("OUTRA FORMA DE UTILIZAÇÃO")
        print("{modificar_letra.letra_VERDE}Uma frase em Python{modificar_letra.limpar_cores}Outra frase em Python")
        print(f"A frase 'Uma frase em Python' ficará em verde e 'Outra frase em Python' ficará normal")
        print('OBS: coloque o f antes das aspas')
    def colorindo_letras_e_fundos(self):
        print("Use as classes LetrasCores e FundoCores  com o metódo  modificar_letra e modificar_fundo")


modificar_fundo = FundoCores('\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m',
                             '\033[47m')

modificar_letra = LetrasCores('\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m',
                              '\033[37m', '\033[m')