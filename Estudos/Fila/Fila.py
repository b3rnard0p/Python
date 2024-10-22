import random

class Fila:
    
    # Construtor
    def __init__(self, velocidades_caixas):
        self.clientes = []  
        self.velocidades_caixas = velocidades_caixas
        self.tempo_por_caixa = [0] * len(velocidades_caixas)
        self.registro_atendimento = []
        
    def mostra_fila(self):    
        print('Fila: ', self.clientes)
        
    def novo_cliente(self, id_cliente, duracao_cliente):
        self.clientes.append((id_cliente, duracao_cliente))
        print(f'Cliente adicionado: {id_cliente} com tempo {duracao_cliente}')
        
    def atende_clientes(self):
        for id_cliente, tempo_cliente in self.clientes:
            caixa_livre = self.tempo_por_caixa.index(min(self.tempo_por_caixa))
            duracao_atendimento = tempo_cliente / self.velocidades_caixas[caixa_livre]
            
            self.tempo_por_caixa[caixa_livre] += duracao_atendimento
            
            self.registro_atendimento.append((id_cliente, caixa_livre, duracao_atendimento))
        
        self.clientes.clear()  

    def mostra_registro(self):
        print('\nRegistro do Atendimento:')
        for id_cliente, caixa, tempo in self.registro_atendimento:
            print(f'  {id_cliente} atendido pelo Caixa {caixa} em {tempo:.2f} segundos.')

qtd_caixas = 2
velocidades_caixas = [random.randint(1, 5) for _ in range(qtd_caixas)]
mercado = Fila(velocidades_caixas)

qtd_clientes = random.randint(1, 10)
for i in range(qtd_clientes):
    duracao_cliente = random.randint(1, 20)
    mercado.novo_cliente(f'Cliente{i+1}', duracao_cliente)

mercado.mostra_fila()
mercado.atende_clientes()
mercado.mostra_registro()
