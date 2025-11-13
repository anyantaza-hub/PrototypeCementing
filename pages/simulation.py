import streamlit as st
import numpy as np
import pandas as pd

st.title("🧪 Cementing Simulation")

st.write("Simulasi dasar untuk menghitung tekanan, densitas, dan displacement.")

md = st.number_input("Masukkan Mud Density (ppg)", 8.0, 20.0, 12.5)
flow = st.number_input("Flow rate (bpm)", 1.0, 20.0, 5.0)

pressure = md * flow * 12.3
st.metric("Estimated Pressure (psi)", f"{pressure:,.2f}")
