from Util import Util
from Insercao import Insercao

import time
import threading

os.system("cls")
lista_insercao = []


tamanho = 60000

Util.gerar_numeros_lista(lista_insercao, tamanho, 20)

threading.Thread(
    target=lambda: (
        Ordenacao.insercao(lista_insercao),
        print("feito... com insercao")
    )
).start()




