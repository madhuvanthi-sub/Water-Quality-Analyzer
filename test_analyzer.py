from analyzer import (
    check_ph,
    check_tds,
    check_hardness,
    check_chloride,
    check_turbidity,
    classify_water
)
ph_result = check_ph(7.2)
tds_result = check_tds(350)
hardness_result = check_hardness(180)
chloride_result = check_chloride(120)
turbidity_result = check_turbidity(1.8)
results = [
    ph_result,
    tds_result,
    hardness_result,
    chloride_result,
    turbidity_result
]
overall = classify_water(results)
print("pH:", ph_result)
print("TDS:", tds_result)
print("Hardness:", hardness_result)
print("Chloride:", chloride_result)
print("Turbidity:", turbidity_result)
print("Overall:", overall)