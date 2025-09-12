import streamlit as st
import time


st.title("media")

st.header("lasos de repetisao")

soma = 0 



for i in range(4):
    nota= st.number_input(f"digite a {i+1}ªnota :")

    soma = soma + nota 



media = soma / 4

if st.button("aperte"):
   st.info(f"media:{media}")