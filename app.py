import streamlit as st
st.title("Water Quality Analyzer")
st.write("Enter the water sample measurements.")
ph = st.number_input(
    "pH",
    min_value=0.0,
    max_value=14.0,
    value=7.0
)
tds = st.number_input(
    "TDS (mg/L)",
    min_value=0.0,
    value=300.0
)
hardness = st.number_input(
    "Hardness (mg/L)",
    min_value=0.0,
    value=150.0
)
chloride = st.number_input(
    "Chloride (mg/L)",
    min_value=0.0,
    value=100.0
)
turbidity = st.number_input(
    "Turbidity (NTU)",
    min_value=0.0,
    value=2.0
)
if st.button("Analyze Water"):
    st.write("Analysis started...")