#Diferente das listas, são imutáveis 

#Tupla vazia
tupla_vazia = ()

#Tupla de numeros
numeros = (1,2,3,4,5)

#Tupla de Strings
string = ("Ana", "Bernardo")

#Tupla de tipos diferentes
mistura = (1, "Ana", 3.14, True)

#Tupla de tuplas
Tupla_de_tupla = ((1,2,3),(4,5,6),(7,8,9))

#Desempacotamento de tuplas
print(numeros)
a, b, c, d, e = numeros
print(a)
print(b)
print(c)
print(d)
print(e)

#Trocar valores de variaveis 
a = 1
b = 2
print(a, b)
a , b = b, a
print(a, b)

#Metodo count()
print(numeros.count(4))

#Metodo index()
print(numeros.index(4))