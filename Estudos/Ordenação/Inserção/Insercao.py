class Insercao:
    
    @staticmethod
    def insercao(lista=[]):   
        for i in range(1, len(lista)):
            aux = lista[i]
            for j in range(i-1, 0, -1):
                if (aux >= lista[j]):
                    break
                lista[j+1] = lista[j]
            
            lista[j+1] = aux 