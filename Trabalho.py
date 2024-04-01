import random

# Função para criar uma lista aleatória com M elementos
def criar_lista(M):
    return sorted([random.randint(1, 100) for _ in range(M)])

# Criar N listas aleatórias de tamanho M
N = 10
M = 5
listas = [criar_lista(M) for _ in range(N)]

# Exibir as 10 listas
print("Listas:")
for i, lista in enumerate(listas, start=1):
    print(f"Lista {i}: {lista}")

# Função para encontrar números comuns e únicos entre as listas
def encontrar_comuns_unicos(listas):
    ocorrencias = {}
    comuns = []
    unicos = set()

    # Contar a ocorrência de cada número em todas as listas
    for lista in listas:
        for num in lista:
            ocorrencias[num] = ocorrencias.get(num, 0) + 1

    # Encontrar números comuns e únicos
    for num, count in ocorrencias.items():
        if count == N:  # Presente em todas as listas
            comuns.append(num)
        elif count == 1:  # Presente em apenas uma lista
            unicos.add(num)

    return comuns, list(unicos)

# Ordenar todas as listas de menor para maior
listas = [sorted(lista) for lista in listas]

# Encontrar números comuns e únicos
numeros_comuns, numeros_unicos = encontrar_comuns_unicos(listas)

# Exibir resultados
print("\nNúmeros comuns em todas as listas:", numeros_comuns)
print("Números únicos em apenas uma das listas:", numeros_unicos)
