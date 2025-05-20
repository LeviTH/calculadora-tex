import streamlit as st
import pandas as pd
import urllib.parse

# ======= Estilo CSS customizado =======
st.markdown("""
    <style>
        body {
            background-color: #f7f7f7;
        }
        .main {
            padding: 20px;
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.05);
        }
        .stButton button {
            background-color: #ff8c42;
            color: white;
            border-radius: 8px;
            height: 3em;
            font-weight: bold;
        }
        footer {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)

# ======= Cabeçalho / Logo =======
st.image("https://i.imgur.com/uZB3rU7.png", width=80)  # Substitua por seu próprio logo
st.markdown("<h2 style='text-align: center;'>🧶 Calculadora de TEX</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Descubra o TEX ideal do seu fio de crochê ou tricô em segundos!</p>", unsafe_allow_html=True)

# ======= Entradas =======
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    peso = st.number_input("🔢 Peso do fio", min_value=0.0, step=10.0, format="%.1f")
    unidade_peso = st.selectbox("Unidade do peso", ["Gramas (g)", "Onças (oz)"])

with col2:
    comprimento = st.number_input("📏 Comprimento do fio", min_value=0.0, step=10.0, format="%.1f")
    unidade_comp = st.selectbox("Unidade do comprimento", ["Metros (m)", "Jardas (yd)"])

# ======= Funções =======
def converter_oncas_para_gramas(oz):
    return oz * 28.3495

def converter_jardas_para_metros(yd):
    return yd * 0.9144

def calcular_tex(peso_gramas, comprimento_metros):
    if comprimento_metros == 0:
        return None
    return (peso_gramas / comprimento_metros) * 1000

# ======= Botão e Resultado =======
st.markdown("---")
if st.button("🔍 Calcular TEX"):
    peso_original = peso
    comprimento_original = comprimento

    if unidade_peso == "Onças (oz)":
        peso = converter_oncas_para_gramas(peso)
    if unidade_comp == "Jardas (yd)":
        comprimento = converter_jardas_para_metros(comprimento)

    tex = calcular_tex(peso, comprimento)

    if tex is None:
        st.error("❗ O comprimento não pode ser zero.")
    else:
        st.success(f"✅ O TEX do fio é: **{round(tex, 2)}**")

        # ======= Download do resultado =======
        resultado = pd.DataFrame({
            "Peso": [peso_original],
            "Unidade do Peso": [unidade_peso],
            "Comprimento": [comprimento_original],
            "Unidade do Comprimento": [unidade_comp],
            "TEX Calculado": [round(tex, 2)]
        })
        csv = resultado.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Baixar resultado (CSV)",
            data=csv,
            file_name="resultado_tex.csv",
            mime="text/csv"
        )

        # ======= Botão de Compartilhar no WhatsApp =======
        mensagem = f"Descobri o TEX do meu fio: {round(tex, 2)}! Calculado com a Calculadora TEX 🧶. Veja: https://calculadora-tex.streamlit.app"
        link_whatsapp = f"https://wa.me/?text={urllib.parse.quote(mensagem)}"
        st.markdown(f"[📲 Compartilhar no WhatsApp]({link_whatsapp})", unsafe_allow_html=True)

# ======= Rodapé personalizado =======
st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 0.85em;'>Desenvolvido por Levi | Projeto: Consciencius 🧘</p>",
    unsafe_allow_html=True
)
