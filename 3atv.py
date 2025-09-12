import streamlit as st
import time 


st.title("verivificasao")

pares = 0
inpares = 0

for i in range(1,6):
    nu=st.number_input(f"digite 0 {i} º numero:", step=1)
    if nu % 2==0:
        pares = pares + 1
    else:
        inpares = inpares + 1
if st.button("verificar"):
    st.info (f"pares:{pares}")
    st.info(f"inpares:{inpares}")            