class Ordenacao:

    def bolha(lista = []):
        houve_troca = True
        while(houve_troca):
            houve_troca = False
            for i in range(0, len(lista)-1):
                if lista[i] > lista[i+1]:
                    houve_troca = True
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux

