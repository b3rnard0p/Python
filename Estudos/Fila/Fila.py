import random

fila_clientes = []

def distribuir_clientes(fila_clientes, velocidades_caixas):
    total_tempo = 0
    tempo_por_caixa = [0] * len(velocidades_caixas)
    registro_atendimento = []  

    for id_cliente, tempo_cliente in fila_clientes:
        caixa_livre = tempo_por_caixa.index(min(tempo_por_caixa))
        duracao_atendimento = tempo_cliente / velocidades_caixas[caixa_livre]
        
        tempo_por_caixa[caixa_livre] += duracao_atendimento
        
        registro_atendimento.append((id_cliente, caixa_livre, duracao_atendimento))

    return registro_atendimento

qtd_clientes = random.randint(1, 10)
for i in range(qtd_clientes):
    duracao_cliente = random.randint(1, 20)
    fila_clientes.append((f'Cliente{i+1}', duracao_cliente))

print('Clientes:', fila_clientes)

velocidades_caixas = [random.randint(1, 5) for _ in range(2)]
print('Velocidades dos Caixas:', velocidades_caixas)

registro_atendimento = distribuir_clientes(fila_clientes, velocidades_caixas)

print('\nRegistro do Atendimento:')
for id_cliente, caixa, tempo in registro_atendimento:
    print(f'  {id_cliente} atendido pelo Caixa {caixa} em {tempo:.2f} segundos.')