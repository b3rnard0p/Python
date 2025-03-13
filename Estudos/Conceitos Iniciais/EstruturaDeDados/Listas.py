#Lista vazia
lista_vazia = []
print(lista_vazia)

#Lista de Números
numeros = [1, 2, 3, 4, 5]

print(numeros)
print(numeros[3])

#Lista de Strings
nomes = ["Ana", "Bernardo", "Luana", "Fernanda"]
print(nomes)
print(nomes[0])

#Lista Variavel
mistura = [1, "Ana", 3.14, True]
print(mistura)
print(mistura[1])

#Lista de listas
lista_de_lista = [[1,2,3], [4,5,6], [7,8,9]]
print(lista_de_lista)
print(lista_de_lista[0])
print(lista_de_lista [0][0])

#Remover item: pop() --> remove o ultimo da lista ou pelo indice
print(nomes.pop())
print(nomes.pop(0))

#Remover item: remove() --> remove pelo nome
nomes.remove("Bernardo")

#Remover item: del --> remove pelo indice
del nomes[0]

#Adcionar pessoas a lista com append
nomes.append("jessica")
nomes.append("Albani")

#Limpar a lista: clear()
nomes.clear()

#Ordenar uma lista: sort() --> Não pode ser usada em uma lista com tipos misturados
numeros = [5,4,3,2,1]
numeros.sort()
numeros.sort(reverse=True)






