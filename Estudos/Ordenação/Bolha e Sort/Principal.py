from Util import Util
from Ordenacao import Ordenacao

import time
import threading

os.system("cls")
lista_bolha = []
lista_insercao = []
lista = []
lista_selecao = []

tamanho = 60000

Util.gerar_numeros_lista(lista_bolha, tamanho, 20)
Util.gerar_numeros_lista(lista_insercao, tamanho, 20)
Util.gerar_numeros_lista(lista, tamanho, 20)
Util.gerar_numeros_lista(lista_selecao, tamanho, 20)

threading.Thread(
    target=lambda: (
        print("Ordenando a lista para o bolha..."),
        Ordenacao.bolha(lista_bolha),
        print("feito... com bolha")
    )
).start()

threading.Thread(
    target=lambda: (
        print("Ordenando a lista para o sort..."),
        lista.sort(),
        print("feito... sort python")
    )
).start()

threading.Thread(
    target=lambda: (
        Ordenacao.insercao(lista_insercao),
        print("feito... com insercao")
    )
).start()

threading.Thread(
    target=lambda: (
        Ordenacao.selecao(lista_selecao),
        print("feito... com seleção")
    )
).start()

# # inicio = time.time()

# print("Ordenando a lista para o bolha...")
# Ordenacao.bolha(lista_bolha)

# fim = time.time()

# tempo_decorrido = fim - inicio

# print(f"Tempo decorrido:{tempo_decorrido: .6f} segundos")

# ###############################################################################

# inicio = time.time()

# print("Ordenando a lista para o sort...")
# lista.sort()

# fim = time.time()

# tempo_decorrido = fim - inicio

# print(f"Tempo decorrido:{tempo_decorrido: .6f} segundos")



