class cliente:
    
    def __init__(self, itens, prioridade):
        self.itens = itens
        self.prioridade = prioridade
    
    def getItens(self):
        return self.itens

    def getPrioridade(self):
        return self.prioridade

class fila:
    
    # Construtor
    def __init__(self, velocidadedeAtendimento):
        self.clientes = []  
        self.servidor = velocidadedeAtendimento
        self.total = 0
        
    def mostraFila(self):    
        for cliente in self.clientes:
            print(cliente.itens, cliente.prioridade)
        
    def mudaVelServidor(self, novaVelocidade):
        print('Mudando a velocidade do servidor')
        print('Antes:', self.servidor, 'Depois:', novaVelocidade)
        self.servidor = novaVelocidade
        
    def novoCliente(self, valor, prioridade):
        cli = cliente(valor, prioridade)
        print('Clinete: ', cli.itens, cli.prioridade)
        self.clientes.append(cli) 
        print('Cliente adicionado na fila')
        self.mostraFila()
        
    def atendeCliente(self):
        if len(self.clientes) > 0:
            self.clientes.sort(key=lambda x: x.getPrioridade(), reverse=True)
            
            cli = self.clientes.pop(0)  
            tatend = cli.getItens() / self.servidor 
            self.total += tatend
            
            print(f'Cliente atendido: {cli.itens, cli.prioridade}\nTempo de atendimento: {tatend:.2f} unidades de tempo.')
            self.mostraFila()
        else:
            print("Não há clientes na fila.")
        

mercado = fila(2)
mercado.novoCliente(10, 3)
mercado.novoCliente(20, 2)
mercado.novoCliente(30, 1)
mercado.novoCliente(40, 3)

mercado.atendeCliente()
mercado.atendeCliente()

mercado.mudaVelServidor(5)

mercado.atendeCliente()
mercado.atendeCliente()

