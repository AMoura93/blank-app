import streamlit as st
from datetime import datetime, timedelta

def calcular_preco(check_in, check_out, e_epoca_alta, e_late_checkout, 
                   preco_epoca_baixa, preco_epoca_alta, taxa_late_checkout):
    num_noites = (check_out - check_in).days
    preco_base = preco_epoca_alta if e_epoca_alta else preco_epoca_baixa
    preco_total = num_noites * preco_base
    if e_late_checkout:
        preco_total += taxa_late_checkout
    return preco_total

# Configurar título da página
st.set_page_config(page_title="Calculadora de Preço de Estadia")

st.title("Calculadora de Preço de Estadia")

# Barra lateral para configurações de preço
st.sidebar.header("Configurações de Preço")
preco_epoca_baixa = st.sidebar.number_input("Preço por Noite (Época Baixa)", value=18.0, step=0.5, format="%.2f")
preco_epoca_alta = st.sidebar.number_input("Preço por Noite (Época Alta)", value=20.0, step=0.5, format="%.2f")
taxa_late_checkout = st.sidebar.number_input("Taxa de Late Check-out", value=13.0, step=1.0, format="%.2f")

# Formulário principal
check_in = st.date_input("Data de Check-in", min_value=datetime.today())
check_out = st.date_input("Data de Check-out", min_value=check_in + timedelta(days=1))

col1, col2 = st.columns(2)
with col1:
    e_epoca_alta = st.checkbox("Época Alta")
with col2:
    e_late_checkout = st.checkbox("Late Check-out")

if st.button("Calcular Preço"):
    if check_out <= check_in:
        st.error("A data de check-out deve ser posterior à data de check-in.")
    else:
        preco_total = calcular_preco(
            check_in, check_out, e_epoca_alta, e_late_checkout,
            preco_epoca_baixa, preco_epoca_alta, taxa_late_checkout
        )
        st.success(f"Preço Total: {preco_total:.2f}€")

# Exibir configurações atuais
st.subheader("Configurações Atuais")
st.write(f"Preço Época Baixa: {preco_epoca_baixa:.2f}€ por noite")
st.write(f"Preço Época Alta: {preco_epoca_alta:.2f}€ por noite")
st.write(f"Taxa de Late Check-out: {taxa_late_checkout:.2f}€")
