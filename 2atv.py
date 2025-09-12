import streamlit as st


st.title("soma de 5 numeros")

st.header("soma de 5 numeros")
for i in range(4):
    nota= st.number_input(f"digite a {i+1}ªnota :")


if st.button("resutado"):
    st.success("soma:")
