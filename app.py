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
col1, col2 = st.columns(2)
with col1:
    ph = st.number_input("pH", 0.0, 14.0, 7.0)
    tds = st.number_input("TDS (mg/L)", 0.0, 5000.0, 300.0)
    hardness = st.number_input("Hardness (mg/L)", 0.0, 1000.0, 150.0)
with col2:
    chloride = st.number_input("Chloride (mg/L)", 0.0, 2000.0, 100.0)
    turbidity = st.number_input("Turbidity (NTU)", 0.0, 1000.0, 2.0)
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