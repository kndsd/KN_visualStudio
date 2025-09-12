import streamlit as st
import time


st.title("media")

st.header("notas")

soma = 0 



for i in range(7):
    nota= st.number_input(f"digite a {i+1}ªnota :")

    soma = soma + nota 



media = soma / 7

if st.button("aperte"):
   st.info(f"media:{media}")
   if media >= 7:
     st.success("aprovado")
     
   else:
     st.error("!!reprovado!!")      

      