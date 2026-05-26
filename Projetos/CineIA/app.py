import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="CineIA", page_icon="🍿")

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error(
        "Configure a variável GEMINI_API_KEY no arquivo .env "
        "(copie de .env.example)."
    )
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3-flash-preview")
st.title("🍿 CineIA: Seu Próximo Filme")
st.markdown("Descubra filmes baseados no seu estado de espírito atual.")

with st.sidebar:
    st.header("Preferências")
    genero = st.multiselect(
        "Gêneros favoritos:",
        ["Ação", "Drama", "Sci-Fi", "Comédia", "Terror", "Documentário"],
    )
    tempo = st.slider("Duração máxima (minutos):", 60, 240, 120)
    mood = st.text_area(
        "Descreva como você está se sentindo ou o que busca no filme:",
        placeholder="Ex: Quero um filme de ficção científica com reviravoltas na história.",
    )
    botao_recomendar = st.button("Buscar Recomendações")

if botao_recomendar:
    if not mood:
        st.warning("Por favor, descreva o que você deseja assistir!")
    else:
        with st.spinner("Analisando catálogo cinematográfico..."):
            prompt = f"""
Você é um especialista em cinema.
Recomende 3 filmes para alguém que gosta de {', '.join(genero)} e que durem até {tempo}
minutos.
O usuário descreveu o clima do filme como: '{mood}'.
Para cada filme, forneça: Título, Ano e uma frase curta do porquê combina com o pedido.
"""
            try:
                response = model.generate_content(prompt)
                st.success("Aqui estão minhas sugestões:")
                st.markdown("---")
                st.write(response.text)

                st.markdown("### Deixe seu feedback:")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👍 Gostei"):
                        with open("feedback.csv", "a", encoding="utf-8") as f:
                            f.write(f"{mood},{genero},{tempo},Gostei\n")
                        st.success("Obrigado pelo seu feedback positivo!")
                with col2:
                    if st.button("👎 Não gostei"):
                        with open("feedback.csv", "a", encoding="utf-8") as f:
                            f.write(f"{mood},{genero},{tempo},Não gostei\n")
                        st.info("Feedback registrado. Vamos melhorar!")
            except Exception as e:
                st.error(f"Erro ao conectar com a IA: {e}")

st.caption(
    "Desenvolvido na disciplina de Desenvolvimento Full Stack – Sistema de Informação – "
    "Universidade Franciscana (UFN)"
)
