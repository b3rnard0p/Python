class Celula:
    def __init__(self, linha, coluna, valor):
        self.linha = linha
        self.coluna = coluna
        self.valor = valor    

    def __hash__(self):
        return hash((self.linha, self.coluna, self.valor))

    def __repr__(self):
        return f'Celula({self.linha}, {self.coluna}, {self.valor})'

    @staticmethod
    def transforma_matriz_em_hash(matriz, tabela_hash):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] != 0:
                    tabela_hash.add(Celula(i, j, matriz[i][j]))
        
        Celula.qtd_linhas = len(matriz)
        Celula.qtd_colunas = len(matriz[0])

    @staticmethod
    def transforma_hash_em_matriz(tabela_hash, matriz):
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz[i][j] = 0
        
        for ponto in tabela_hash:
            matriz[ponto.linha][ponto.coluna] = ponto.valor        

    @staticmethod
    def exibe_matriz_em_hash(tabela_hash):
            print("Matriz[",Celula.qtd_linhas,"][",Celula.qtd_colunas,"]")

            for ponto in tabela_hash:
                print(ponto)

def exibir(matriz):
    for linha in matriz:
        print(linha)

tam_linha = 5
tam_coluna = 5
matriz_especial = [[0 for _ in range(tam_linha)] for _ in range(tam_coluna)]

matriz_especial[0][0] = 5
matriz_especial[2][3] = 5
matriz_especial[4][2] = 5

exibir(matriz_especial)

tabela_hash = set()
Celula.transforma_matriz_em_hash(matriz_especial, tabela_hash)
Celula.exibe_matriz_em_hash(tabela_hash)

print("Gerando matriz especial a partir da tabela hash")
outra_matriz = [[0 for _ in range(Celula.qtd_linhas)] for _ in range(Celula.qtd_colunas)]
Celula.transforma_hash_em_matriz(tabela_hash, outra_matriz)
exibir(outra_matriz)
