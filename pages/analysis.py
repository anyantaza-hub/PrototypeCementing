import streamlit as st
import pandas as pd

st.title("📊 Cementing Job Analysis")

uploaded = st.file_uploader("Upload data hasil job (CSV)", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df)
    st.line_chart(df)
