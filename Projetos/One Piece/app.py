import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="LogPose IA", page_icon="🏴‍☠️", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Inter:wght@300;400;500;600;700&family=Pirata+One&family=Outfit:wght@300;400;500;600;700&display=swap');

    /* Global Styles */
    .stApp {
        background: radial-gradient(circle at 50% 0%, #0c152b 0%, #070b19 70%, #03040a 100%) !important;
        color: #e2e8f0 !important;
        font-family: 'Outfit', sans-serif !important;
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    ::-webkit-scrollbar-track {
        background: #040814;
    }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #aa7c11, #d4af37);
        border-radius: 5px;
        border: 2px solid #040814;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: #ffd700;
    }

    /* Titles and Headers */
    .header-container {
        text-align: center;
        padding: 2rem 1.5rem;
        margin-top: 1rem;
        margin-bottom: 2.5rem;
        background: rgba(10, 17, 40, 0.45);
        border: 1px solid rgba(212, 175, 55, 0.25);
        border-radius: 20px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), inset 0 1px 1px rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(8px);
    }
    .main-title {
        font-family: 'Pirata One', cursive;
        font-size: 4.5rem;
        font-weight: 400;
        letter-spacing: 4px;
        margin: 0;
        padding: 0;
        line-height: 1.1;
        background: linear-gradient(90deg, #ffd700 0%, #00f5d4 50%, #ffd700 100%);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: titleShimmer 6s linear infinite;
        filter: drop-shadow(0 4px 12px rgba(0, 245, 212, 0.15));
    }
    @keyframes titleShimmer {
        0% { background-position: 0% 50%; }
        100% { background-position: 200% 50%; }
    }
    .main-subtitle {
        font-family: 'Cinzel', serif;
        font-size: 1.25rem;
        color: #ffd700;
        font-weight: 700;
        letter-spacing: 3px;
        margin-top: 10px;
        margin-bottom: 12px;
        text-transform: uppercase;
        text-shadow: 0 2px 5px rgba(0,0,0,0.5);
    }
    .tagline {
        font-family: 'Outfit', sans-serif;
        font-size: 1.05rem;
        color: #94a3b8;
        max-width: 650px;
        margin: 0 auto;
        line-height: 1.5;
    }

    /* Glassmorphic Cards */
    .glass-card {
        background: rgba(10, 18, 42, 0.55) !important;
        border: 1px solid rgba(212, 175, 55, 0.2) !important;
        border-radius: 18px !important;
        padding: 28px !important;
        margin-bottom: 28px !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(15px) !important;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
    }
    .glass-card:hover {
        border-color: rgba(0, 245, 212, 0.35) !important;
        box-shadow: 0 20px 45px rgba(0, 245, 212, 0.08), 0 10px 20px rgba(0, 0, 0, 0.3) !important;
        transform: translateY(-2px);
    }

    /* Sidebar Custom Styling */
    [data-testid="stSidebar"] {
        background-color: rgba(5, 8, 22, 0.96) !important;
        border-right: 1px solid rgba(212, 175, 55, 0.15) !important;
    }
    .sidebar-header {
        padding: 18px 12px;
        border-bottom: 1px dashed rgba(212, 175, 55, 0.25);
        margin-bottom: 25px;
        text-align: center;
    }
    .sidebar-header h3 {
        font-family: 'Cinzel', serif;
        color: #ffd700;
        margin: 0;
        font-size: 1.3rem;
        font-weight: 700;
        letter-spacing: 1.5px;
    }
    .sidebar-header p {
        font-size: 0.85rem;
        color: #64748b;
        margin: 5px 0 0 0;
    }

    /* Streamlit Widget Styling */
    .stTextArea label, .stSelectbox label, .stToggle label, .stMultiSelect label, [data-testid="stSidebar"] label {
        font-family: 'Cinzel', serif !important;
        font-size: 0.95rem !important;
        font-weight: 700 !important;
        color: #ffd700 !important;
        letter-spacing: 1px !important;
        margin-bottom: 8px !important;
    }

    /* Text Inputs, Selectboxes & Textarea Styling */
    div[data-baseweb="textarea"] {
        background-color: rgba(5, 8, 20, 0.75) !important;
        border: 1px solid rgba(212, 175, 55, 0.25) !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
    }
    div[data-baseweb="textarea"]:focus-within {
        border-color: rgba(0, 245, 212, 0.6) !important;
        box-shadow: 0 0 15px rgba(0, 245, 212, 0.25) !important;
    }

    div[data-baseweb="select"] {
        background-color: rgba(5, 8, 20, 0.75) !important;
        border: 1px solid rgba(212, 175, 55, 0.25) !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"]:focus-within {
        border-color: rgba(0, 245, 212, 0.6) !important;
    }

    /* Button Custom Styling */
    .stButton > button {
        background: linear-gradient(135deg, #d4af37 0%, #b8860b 50%, #8b6508 100%) !important;
        color: #050814 !important;
        font-family: 'Outfit', sans-serif !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        box-shadow: 0 5px 15px rgba(184, 134, 11, 0.2) !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 245, 212, 0.35) !important;
        background: linear-gradient(135deg, #00f5d4 0%, #00e5ff 100%) !important;
        color: #050814 !important;
        border-color: rgba(255, 255, 255, 0.3) !important;
    }
    .stButton > button:active {
        transform: translateY(1px) !important;
    }

    /* AI Response Styling via Chat Message */
    [data-testid="stChatMessage"] {
        background-color: rgba(10, 18, 42, 0.65) !important;
        border: 1px solid rgba(212, 175, 55, 0.3) !important;
        border-left: 6px solid #d4af37 !important;
        border-radius: 16px !important;
        padding: 25px 30px !important;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.45) !important;
        backdrop-filter: blur(10px) !important;
        margin-top: 15px !important;
        margin-bottom: 25px !important;
    }
    [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li {
        font-family: 'Outfit', sans-serif !important;
        font-size: 1.08rem !important;
        line-height: 1.7 !important;
        color: #f1f5f9 !important;
    }
    [data-testid="stChatMessage"] h1, [data-testid="stChatMessage"] h2, [data-testid="stChatMessage"] h3 {
        font-family: 'Cinzel', serif !important;
        color: #ffd700 !important;
        margin-top: 20px !important;
        margin-bottom: 10px !important;
        letter-spacing: 1px !important;
    }
    [data-testid="stChatMessage"] h1 { font-size: 1.8rem !important; }
    [data-testid="stChatMessage"] h2 { font-size: 1.5rem !important; }
    [data-testid="stChatMessage"] h3 { font-size: 1.25rem !important; }
    [data-testid="stChatMessage"] li {
        margin-bottom: 8px !important;
    }
    [data-testid="stChatMessage"] strong {
        color: #00f5d4 !important;
        font-weight: 600 !important;
        text-shadow: 0 0 5px rgba(0, 245, 212, 0.15);
    }

    /* Feedback Header */
    .feedback-header {
        font-family: 'Cinzel', serif;
        color: #ffd700;
        font-size: 1.3rem;
        font-weight: 700;
        margin-top: 40px;
        margin-bottom: 20px;
        letter-spacing: 1.5px;
        border-bottom: 1px dashed rgba(212, 175, 55, 0.3);
        padding-bottom: 8px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.5);
    }

    /* Custom Footer */
    .maritime-footer {
        text-align: center;
        margin-top: 60px;
        padding-top: 25px;
        padding-bottom: 25px;
    }
    .maritime-footer .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(212, 175, 55, 0.25), transparent);
        width: 70%;
        margin: 0 auto 20px auto;
    }
    .maritime-footer p {
        font-size: 0.88rem;
        color: #64748b;
        font-family: 'Outfit', sans-serif;
        letter-spacing: 0.5px;
    }
    .maritime-footer .ship-icon {
        font-size: 1.8rem;
        display: inline-block;
        animation: boatFloat 4s ease-in-out infinite;
        margin-top: 8px;
        cursor: default;
    }
    @keyframes boatFloat {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-6px) rotate(4deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Top Banner
st.image("logpose_banner.png", use_container_width=True)

# Main Title Container
st.markdown(
    """
    <div class="header-container">
        <h1 class="main-title">LOGPOSE IA</h1>
        <h2 class="main-subtitle">O Oráculo Absoluto da Grand Line</h2>
        <p class="tagline">Trace rotas seguras pelos mistérios, personagens, arcos, poderes e teorias do lendário mundo de One Piece.</p>
    </div>
    """,
    unsafe_allow_html=True
)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("A variável GEMINI_API_KEY não foi encontrada no ambiente.")
    st.info("Crie/edite seu arquivo .env com GEMINI_API_KEY=... e rode novamente.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3-flash-preview")

system_prompt = """
Você é o "LogPose", um modelo de inteligência artificial especialista absoluto no universo de One Piece, criado por Eiichiro Oda.
Seu objetivo é ajudar o usuário com informações precisas, detalhadas e contextualizadas sobre o mangá e o anime.

Diretrizes de Comportamento:
1. Persona: Você é entusiasmado por aventuras, respeitoso com a história e usa termos nativos do universo (como Akuma no Mi, Haki, Yonkou, Shichibukai, Mugiwaras) naturalmente, sem precisar explicá-los a menos que seja solicitado.
2. Precisão Histórica: Baseie suas respostas estritamente no cânone da obra (Mangá principalmente, SBS e Databooks oficiais). Se algo aconteceu apenas em Filler de anime ou Filmes, especifique isso claramente.
3. Tratamento de Teorias: O universo de One Piece é cheio de mistérios. Quando o usuário perguntar sobre algo não revelado (ex: o que é o One Piece, a mãe do Luffy, o século perdido), você deve expor o que a obra já mostrou de fato e, se relevante, mencionar as teorias mais aceitas pela comunidade, deixando explícito que são APENAS teorias.
4. Organização das Respostas: Sempre que explicar sobre personagens, arcos ou poderes, use tópicos (bullet points) e negritos para facilitar a leitura. Evite blocos massivos de texto.
5. Alerta de Spoiler: Seja direto, mas se a resposta envolver acontecimentos muito recentes do mangá (arco atual), coloque um breve aviso de spoiler no início da resposta.

Se você não souber de uma informação ou se ela nunca foi dita na obra, responda honestamente:
"Essa informação ainda está oculta nas névoas da Grand Line" ou "Nem mesmo os Gorosei sabem disso ainda",
e explique o que se sabe de mais próximo.
"""

with st.sidebar:
    st.markdown(
        """
        <div class="sidebar-header">
            <h3>⚓ DECK DE COMANDO</h3>
            <p>Ajuste os parâmetros da jornada</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    foco = st.selectbox(
        "Foco da resposta:",
        ["Geral", "Personagens", "Arcos", "Poderes", "Teorias", "Cronologia"],
    )
    nivel = st.selectbox("Nível de detalhe:", ["Rápido", "Médio", "Profundo"])
    incluir_spoilers = st.toggle("Permitir spoilers recentes", value=False)

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
pergunta = st.text_area(
    "🗺️ Qual é sua dúvida no universo de One Piece?",
    placeholder="Ex: Qual a importância de Joy Boy para a história atual?",
    height=170,
)
enviar = st.button("Consultar o LogPose")
st.markdown("</div>", unsafe_allow_html=True)

if "ultima_resposta" not in st.session_state:
    st.session_state.ultima_resposta = ""

if enviar:
    if not pergunta.strip():
        st.warning("Digite uma pergunta antes de consultar o LogPose.")
    else:
        with st.spinner("Traçando rota pelas correntes da Grand Line..."):
            user_prompt = f"""
Contexto de formato da resposta:
- Foco solicitado: {foco}
- Nível de detalhe: {nivel}
- Permissão de spoilers recentes: {"SIM" if incluir_spoilers else "NÃO"}

Pergunta do usuário:
{pergunta}
"""
            try:
                full_prompt = f"{system_prompt}\n\n{user_prompt}"
                response = model.generate_content(full_prompt)
                st.session_state.ultima_resposta = response.text
            except Exception as exc:
                st.error(f"Falha ao consultar a IA: {exc}")

if st.session_state.ultima_resposta:
    st.markdown("### 🧭 Rota Traçada pelo LogPose")
    with st.chat_message("assistant", avatar="🧭"):
        st.markdown(st.session_state.ultima_resposta)

    st.markdown('<div class="feedback-header">📜 Livro de Bordo (Feedback da Tripulação)</div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("👍 Excelente resposta"):
            with open("feedback.csv", "a", encoding="utf-8") as file:
                file.write(f'"{pergunta}","{foco}","{nivel}",Gostei\n')
            st.success("Valeu, nakama! Feedback positivo registrado.")
    with col2:
        if st.button("👎 Pode melhorar"):
            with open("feedback.csv", "a", encoding="utf-8") as file:
                file.write(f'"{pergunta}","{foco}","{nivel}",Nao gostei\n')
            st.info("Feedback registrado. O LogPose vai calibrar a rota.")

st.markdown(
    """
    <div class="maritime-footer">
        <div class="divider"></div>
        <p>LogPose IA • Projeto temático de One Piece com Streamlit + Gemini</p>
        <div class="ship-icon">⛵</div>
    </div>
    """,
    unsafe_allow_html=True
)

