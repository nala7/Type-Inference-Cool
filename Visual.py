from Main import run_pipeline
import streamlit as st 
from Grammar import *

st.sidebar.header("About")
st.sidebar.subheader("Segundo Proyecto de Compilacion: Cool Type Inferer")
st.sidebar.text("Nadia González Fernández")
st.sidebar.text("Jose Alejandro Labourdette-Lartigue Soto")
st.sidebar.text("Grupo: C-312")

data = st.text_area("Enter code", "", 500)
run = st.button("Run")
if run:
    text = run_pipeline(G, data)
    st.text(text)