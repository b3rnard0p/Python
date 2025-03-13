#Chave-Valor

#Dicionario vazio
dicionario_vazio = {}

#Dicionario de numeros
numeros = {1: "Um", 2: "Dois"}

#Dicionario de string
nomes = {"Ana": 1, "Bia": 2}

#Exemplo usual
user = {"nome": "Ana", "idade": 25, "email": "be@gmail.com"}

#Adicionar item
user["city"]= "São Paulo"

#Modificar um item
user["idade"] = 26

#Remover um item
print(user.pop("idade"))
print(user.pop("idade", "Chave não existe"))

#popitem() -->Remove o último item
print(user.popitem())
print(user)

