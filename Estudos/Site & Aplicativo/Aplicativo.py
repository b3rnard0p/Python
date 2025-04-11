# O q eu quero no meu sistema?
    # Titulo Hashzap
    # botao de iniciar chat
        # popup para entrar no chat
        # quando entrar no chat: (aparece para todo mundo)
            # a mensagem que você entrou no chat
            # o campo e o botão de enviar mensagem
        # a cada mensagem que você envia (aparece para todo mundo)
            # Nome: Texto da Mensagem

# Framework --> Flask

import flet as ft # --> importar o framework

# Função principal que configura toda a interface do chat
# Recebe a página como parâmetro e configura todos os elementos visuais
def main(pagina): 
    
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    nome_usuario = ft.TextField(label="Escreva seu nome")

    # Função que gerencia o recebimento de mensagens
    # Recebe mensagens do pubsub e as exibe no chat
    # Trata dois tipos de mensagens:
    # 1. Mensagens normais do chat
    # 2. Mensagens de entrada de novos usuários
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        elif tipo == "entrada":
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE))
        elif tipo == "saida":
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} saiu do chat", 
                                         size=12, italic=True, color=ft.colors.RED))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    # Função que envia mensagens para todos os usuários conectados
    # É chamada quando o usuário clica no botão enviar ou pressiona enter
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    # Função que gerencia a entrada de um novo usuário no chat
    # Mostra o popup de boas-vindas e configura a interface do chat
    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
        pagina.add(chat)
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        pagina.add(ft.Row(
            [campo_mensagem, botao_enviar_mensagem]
        ))
        pagina.add(botao_sair)
        pagina.update()

    def sair_chat(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "saida"})
        # Limpa a página
        pagina.clean()
        # Adiciona os elementos iniciais
        pagina.add(popup)
        pagina.add(texto)
        pagina.add(botao_iniciar)
        pagina.update()

    botao_sair = ft.ElevatedButton("Sair", on_click=sair_chat)

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    # Função que abre o popup de entrada no chat
    # É chamada quando o usuário clica no botão "Iniciar chat"
    def entrar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(popup)
    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, port=8000) # --> Rodar o projeto

