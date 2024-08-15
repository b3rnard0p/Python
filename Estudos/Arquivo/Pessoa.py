class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"

class GerenciadorDePessoas:
    @staticmethod
    def salvar_pessoa_arquivo(nome_arquivo, pessoa):
        with open(nome_arquivo, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f"{pessoa.nome},{pessoa.idade},{pessoa.email}\n")
        print(f"As informações de {pessoa.nome} foram salvas em {nome_arquivo}.")

    @staticmethod
    def carregar_pessoas_arquivo(nome_arquivo):
        pessoas = []
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                nome, idade, email = linha.strip().split(',')
                pessoas.append(Pessoa(nome, int(idade), email))
        return pessoas

    @staticmethod
    def exibir_pessoas(pessoas):
        for pessoa in pessoas:
            print(pessoa)

# Criando algumas pessoas
pessoa1 = Pessoa("João Silva", 30, "joao@example.com")
pessoa2 = Pessoa("Maria Oliveira", 25, "maria@example.com")

# Salvando as pessoas em um arquivo
GerenciadorDePessoas.salvar_pessoa_arquivo("pessoas.txt", pessoa1)
GerenciadorDePessoas.salvar_pessoa_arquivo("pessoas.txt", pessoa2)

# Carregando e exibindo as pessoas do arquivo
pessoas = GerenciadorDePessoas.carregar_pessoas_arquivo("pessoas.txt")
GerenciadorDePessoas.exibir_pessoas(pessoas)
