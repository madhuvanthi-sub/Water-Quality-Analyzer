from analyzer import (
    check_ph,
    check_tds,
    check_hardness,
    check_chloride,
    check_turbidity,
    classify_water
)
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
    ph_result = check_ph(ph)
    tds_result = check_tds(tds)
    hardness_result = check_hardness(hardness)
    chloride_result = check_chloride(chloride)
    turbidity_result = check_turbidity(turbidity)
    results = [
        ph_result,
        tds_result,
        hardness_result,
        chloride_result,
        turbidity_result
    ]
    overall = classify_water(results)
    st.subheader("Analysis Results")
    st.write("pH:", ph_result)
    st.write("TDS:", tds_result)
    st.write("Hardness:", hardness_result)
    st.write("Chloride:", chloride_result)
    st.write("Turbidity:", turbidity_result)
    st.subheader("Overall Water Quality")
    st.success(overall)