class Ordenacao:
    """
    Contém métodos estáticos para algoritmos de ordenação.
    """

    @staticmethod
    def bolha(lista):
        """
        Ordena uma lista de alunos usando o algoritmo de ordenação bolha.

        """
        houve_troca = True
        while houve_troca:
            houve_troca = False
            for i in range(len(lista) - 1):
                if (lista[i].nome > lista[i + 1].nome) or (lista[i].nome == lista[i + 1].nome and lista[i].idade > lista[i + 1].idade):
                    houve_troca = True
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]

    @staticmethod
    def insercao(lista):
        """
        Ordena uma lista de alunos usando o algoritmo de ordenação por inserção.

        """
        for i in range(1, len(lista)):
            aux = lista[i]
            j = i - 1
            while j >= 0 and (aux.nome < lista[j].nome or (aux.nome == lista[j].nome and aux.idade < lista[j].idade)):
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = aux 

    @staticmethod
    def selecao(lista):
        """
        Ordena uma lista de alunos usando o algoritmo de ordenação por seleção.

        """
        for i in range(len(lista) - 1):
            pos_menor = i
            for j in range(i + 1, len(lista)):
                if lista[j].nome < lista[pos_menor].nome or (lista[j].nome == lista[pos_menor].nome and lista[j].idade < lista[pos_menor].idade):
                    pos_menor = j
            if i != pos_menor:
                lista[i], lista[pos_menor] = lista[pos_menor], lista[i]
