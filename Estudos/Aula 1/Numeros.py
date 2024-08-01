import random

Class Numeros:
    
    """_summary_
        Classe que possui serviços de manipulação de números
    """
    
    @staticmethod
    def popular_aleatorio(lista, quantidade, limite):
        
        """_summary_
            Método de classe que popula com numeros inteiros uma lista
        Args:
            lista (int): para números
            quantidade (int): contém a quantidade de números a serem gerados na lista
            limite (int): range do número
        """
        
        for i in range(0, quantidade):
            lista.append(random.randint(0, limite))
    