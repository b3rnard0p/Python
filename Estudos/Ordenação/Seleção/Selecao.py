class Selecao:   
    @staticmethod
    def selecao(lista):       
        for i in range(0, len(lista) -1):
            posMenor = i
            for j in range(i+1, len(lista)):
                if (lista[j] < lista[posMenor]):
                    posMenor = j
                
            if (i != posMenor):
                tmp = lista[i]
                lista[i] = lista[posMenor]
                lista[posMenor] = tmp
