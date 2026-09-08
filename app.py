from analyzer import (
    check_ph,
    check_tds,
    check_hardness,
    check_chloride,
    check_turbidity,
    classify_water
)
import streamlit as st
import matplotlib.pyplot as plt
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
    if ph_result == "Normal":
        st.success("pH: Normal")
    else:
        st.warning("pH: " + ph_result)
    if tds_result == "Normal":
        st.success("TDS: Normal")
    else:
        st.warning("TDS: " + tds_result)
    if hardness_result == "Normal":
        st.success("Hardness: Normal")
    else:
        st.warning("Hardness: " + hardness_result)
    if chloride_result == "Normal":
        st.success("Chloride: Normal")
    else:
        st.warning("Chloride: " + chloride_result)
    if turbidity_result == "Normal":
        st.success("Turbidity: Normal")
    else:
        st.warning("Turbidity: " + turbidity_result)
    st.subheader("Overall Water Quality")
    st.success(overall)
    st.header("📊 Measured Values vs Reference Limits")
    PH_LOWER_LIMIT = 6.5
    PH_UPPER_LIMIT = 8.5
    TDS_LIMIT = 500
    HARDNESS_LIMIT = 200
    CHLORIDE_LIMIT = 250
    TURBIDITY_LIMIT = 5
    st.subheader("pH")
    fig_ph, ax_ph = plt.subplots()
    ax_ph.bar(
        ["Measured pH", "Lower Limit", "Upper Limit"],
        [ph, PH_LOWER_LIMIT, PH_UPPER_LIMIT]
    )
    ax_ph.set_ylabel("pH")
    ax_ph.set_title("Measured pH vs Reference Range")
    st.pyplot(fig_ph)
    plt.close(fig_ph)
    st.subheader("TDS")
    fig_tds, ax_tds = plt.subplots()
    ax_tds.bar(
        ["Measured TDS", "Reference Limit"],
        [tds, TDS_LIMIT]
    )
    ax_tds.set_ylabel("TDS (mg/L)")
    ax_tds.set_title("Measured TDS vs Reference Limit")
    st.pyplot(fig_tds)
    plt.close(fig_tds)
    st.subheader("Hardness")
    fig_hardness, ax_hardness = plt.subplots()
    ax_hardness.bar(
        ["Measured Hardness", "Reference Limit"],
        [hardness, HARDNESS_LIMIT]
    )
    ax_hardness.set_ylabel("Hardness (mg/L)")
    ax_hardness.set_title("Measured Hardness vs Reference Limit")
    st.pyplot(fig_hardness)
    plt.close(fig_hardness)
    st.subheader("Chloride")
    fig_chloride, ax_chloride = plt.subplots()
    ax_chloride.bar(
        ["Measured Chloride", "Reference Limit"],
        [chloride, CHLORIDE_LIMIT]
    )
    ax_chloride.set_ylabel("Chloride (mg/L)")
    ax_chloride.set_title("Measured Chloride vs Reference Limit")
    st.pyplot(fig_chloride)
    plt.close(fig_chloride)
    st.subheader("Turbidity")
    fig_turbidity, ax_turbidity = plt.subplots()
    ax_turbidity.bar(
        ["Measured Turbidity", "Reference Limit"],
        [turbidity, TURBIDITY_LIMIT]
    )
    ax_turbidity.set_ylabel("Turbidity (NTU)")
    ax_turbidity.set_title("Measured Turbidity vs Reference Limit")
    st.pyplot(fig_turbidity)
    plt.close(fig_turbidity)