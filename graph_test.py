import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("data/water_samples.csv")
plt.bar(data["sample_id"], data["tds"])
plt.xlabel("Water Sample")
plt.ylabel("TDS (mg/L)")
plt.title("TDS Levels in Water Samples")
plt.show()