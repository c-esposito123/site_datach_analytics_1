import streamlit as st

NOME_EMPRESA = "DataCH Analytics"

PAGINAS = [
    "🏠 Home",
    "📈 Gráficos",
    "📋 Tabelas",
    "⬇️ Download Relatório",
    "📧 Enviar Email",
]


def montar_sidebar():
    """Monta o cabeçalho/configurações da barra lateral (nome do usuário, etc.)."""
    st.sidebar.title("⚙️ Configurações")

    if "nome_usuario" not in st.session_state:
        st.session_state["nome_usuario"] = ""

    nome = st.sidebar.text_input(
        "Seu nome",
        value=st.session_state["nome_usuario"],
        placeholder="Digite seu nome...",
        key="input_nome_sidebar",
    )
    st.session_state["nome_usuario"] = nome

    st.sidebar.markdown("---")


def menu() -> str:
    """Renderiza o menu de navegação e devolve a página escolhida."""
    st.sidebar.title("📊 Menu")

    escolha = st.sidebar.radio("Navegação", PAGINAS, key="menu_navegacao")

    montar_sidebar()

    st.sidebar.caption(f"📊 {NOME_EMPRESA}")
    st.sidebar.caption("Plataforma de Análise de Churn")

    return escolha


def saudacao():
    nome = st.session_state.get("nome_usuario", "").strip()
    if nome:
        st.markdown(f"#### 👋 Olá, **{nome}**! Seja bem-vindo(a) de volta.")
    else:
        st.markdown("#### 👋 Olá! Que bom ter você aqui.")
        st.caption("Dica: preencha seu nome na barra lateral para uma experiência personalizada.")
    st.markdown("")
