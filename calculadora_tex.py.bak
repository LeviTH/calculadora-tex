import streamlit as st

def converter_oncas_para_gramas(oz):
    return oz * 28.3495

def converter_jardas_para_metros(yd):
    return yd * 0.9144

def calcular_tex(peso_gramas, comprimento_metros):
    if comprimento_metros == 0:
        return None
    return (peso_gramas / comprimento_metros) * 1000

st.title("🧶 Calculadora de TEX para Fios de Crochê e Tricô")

peso = st.number_input("Peso do fio:", min_value=0.0, step=0.1)
unidade_peso = st.selectbox("Unidade do peso:", ["Gramas (g)", "Onças (oz)"])

comprimento = st.number_input("Comprimento do fio:", min_value=0.0, step=0.1)
unidade_comp = st.selectbox("Unidade do comprimento:", ["Metros (m)", "Jardas (yd)"])

if st.button("Calcular TEX"):
    if unidade_peso == "Onças (oz)":
        peso = converter_oncas_para_gramas(peso)
    if unidade_comp == "Jardas (yd)":
        comprimento = converter_jardas_para_metros(comprimento)

    tex = calcular_tex(peso, comprimento)

    if tex is None:
        st.error("Comprimento não pode ser zero.")
    else:
        st.success(f"TEX: {round(tex, 2)}")
