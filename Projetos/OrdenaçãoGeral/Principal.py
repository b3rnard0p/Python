import threading
import os
from Aluno import Aluno
from Ordenacao import Ordenacao

def main():
    """
    Função principal que executa a ordenação das listas usando diferentes algoritmos em threads separadas.
    """
    os.system("cls") 

    tamanho = 60000

    lista_bolha = Aluno.gerar_alunos(tamanho)
    lista_insercao = Aluno.copiar_lista_alunos(lista_bolha)
    lista_selecao = Aluno.copiar_lista_alunos(lista_bolha)
    lista_sort = Aluno.copiar_lista_alunos(lista_bolha)

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
            lista_sort.sort(key=lambda aluno: (aluno.nome, aluno.idade)),
            print("feito... sort python")
        )
    ).start()

    threading.Thread(
        target=lambda: (
            print("Ordenando a lista para inserção..."),
            Ordenacao.insercao(lista_insercao),
            print("feito... com inserção")
        )
    ).start()

    threading.Thread(
        target=lambda: (
            print("Ordenando a lista para seleção..."),
            Ordenacao.selecao(lista_selecao),
            print("feito... com seleção")
        )
    ).start()

if __name__ == "__main__":
    main()
