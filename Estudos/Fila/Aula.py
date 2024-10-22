class fila:
    
    #Construtor
    def __init__(self, velocidadedeAtendimento):
        self.clientes = []  
        self.servidor = velocidadedeAtendimento
        self.total = 0
        
    def mostraFila(self):    
        print('Fila: ', self.clientes, 'Tempo total: ', self.total)
        
    def mudaVelServidor(self, novaVelocidade):
        print('Mudando a velocidade do servidor')
        print('Antes: ', self.servidor, 'Depois: ', novaVelocidade)
        self.servidor = novaVelocidade
        
    def novoCliente(self, valor):
        self.clientes.append(valor) 
        print('Cliente adicionado na fila')
        print(self.clientes) 
        
    def atendeCliente(self):
        cli = ''
        tatend = 0
        if len(self.clientes) > 0:
            cli = self.clientes.pop(0)
            tatend = cli/self.servidor
            self.total = self.total+tatend
        print('Cliente atendido: ', cli, '\n No tempo: ', tatend)
        self.mostraFila()
        
mercado = fila(2)
mercado.novoCliente(10)
mercado.novoCliente(20)
mercado.novoCliente(30)
mercado.novoCliente(40)
mercado.atendeCliente()
mercado.atendeCliente()
mercado.mudaVelServidor(5)
mercado.atendeCliente()
mercado.atendeCliente()
mercado.atendeCliente()