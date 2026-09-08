def check_ph(ph):
    if ph < 6.5:
        return "Low"
    elif ph > 8.5:
        return "High"
    else:
        return "Normal"
def check_tds(tds):
    if tds <= 500:
        return "Normal"
    else:
        return "High"
def check_hardness(hardness):
    if hardness <= 200:
        return "Normal"
    else:
        return "High"
def check_chloride(chloride):
    if chloride <= 250:
        return "Normal"
    else:
        return "High"
def check_turbidity(turbidity):
    if turbidity <= 5:
        return "Normal"
    else:
        return "High"
def classify_water(results):
    abnormal = 0
    for result in results:
        if result != "Normal":
            abnormal += 1
    if abnormal == 0:
        return "Good"
    elif abnormal <= 2:
        return "Moderate"
    else:
        return "Poor"