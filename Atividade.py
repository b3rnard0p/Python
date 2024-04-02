import csv

class Personagem:
    def __init__(self, nome, energia, categoria):
        self.nome = nome
        self.energia = energia
        self.categoria = categoria

def carregar_do_csv():
    personagens = []
    try:
        with open('personagens.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                nome, energia, categoria = row
                personagem = Personagem(nome, int(energia), categoria)
                personagens.append(personagem)
    except FileNotFoundError:
        pass  # Arquivo não encontrado, retorna lista vazia
    return personagens

def salvar_no_csv(personagens):
    with open('personagens.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for personagem in personagens:
            writer.writerow([personagem.nome, personagem.energia, personagem.categoria])

def main():
    personagens = carregar_do_csv()

    while True:
        print("\nMenu:")
        print("1. Cadastrar Personagem")
        print("2. Listar Personagens")
        print("3. Remover Personagem")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do personagem: ")
            energia = int(input("Digite a energia do personagem: "))
            categoria = input("Digite a categoria do personagem: ")
            novo_personagem = Personagem(nome, energia, categoria)
            personagens.append(novo_personagem)
            salvar_no_csv(personagens)
            print("Personagem cadastrado com sucesso!")
        elif opcao == '2':
            if not personagens:
                print("Não há personagens cadastrados.")
            else:
                print("Lista de Personagens:")
                for personagem in personagens:
                    print(f"Nome: {personagem.nome}, Energia: {personagem.energia}, Categoria: {personagem.categoria}")
        elif opcao == '3':
            if not personagens:
                print("Não há personagens cadastrados para remover.")
            else:
                nome_remover = input("Digite o nome do personagem que deseja remover: ")
                removido = False
                for personagem in personagens:
                    if personagem.nome.lower() == nome_remover.lower():
                        personagens.remove(personagem)
                        salvar_no_csv(personagens)
                        removido = True
                        print("Personagem removido com sucesso!")
                        break
                if not removido:
                    print("Personagem não encontrado.")
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
