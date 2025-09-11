import streamlit as st 
import time

st.title("atividade ")


st.header("comtagen regresiva")

n=st.number_input("digite um numero:",step=1, min_value=0)

if st.button("inicar"):
   for i in range(n, 0, -1):
       st.info(i)
       time.sleep(1)
else:
    st.warning("!!!digite um numero")