from Util import Util
from Ordenacao import Ordenacao

import time
import threading

lista = []
lista_bolha = []

Util.gerar_numeros_lista(lista, 10000, 10000)
Util.gerar_numeros_lista(lista_bolha, 10000, 10000)

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



