
import streamlit as st
import pandas as pd

st.title("🎸 Eventi Musicali Gratuiti - Udine e dintorni")

zona = st.text_input("Cerca eventi per zona", "Udine")

df = pd.read_csv("eventi_udine.csv")

st.subheader(f"Eventi trovati per la zona: {zona}")
st.dataframe(df)
