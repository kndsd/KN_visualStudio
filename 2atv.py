import streamlit as st


st.title("soma de 5 numeros")

st.header("soma de 5 numeros")

n1 = st.number_input("digite numero", step=1)
n2 = st.number_input("digite numero", step=1)
n3 = st.number_input("digite numero", step=1)
n4 = st.number_input("digite numero", step=1)
n5 = st.number_input("digite numero", step=1)

soma = n1 + n2 + n3 + n4 + n5

if st.button("resutado"):
    st.success(f"soma:{soma}")
