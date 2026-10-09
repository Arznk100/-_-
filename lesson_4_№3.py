import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')
species_counts = df["Species"].value_counts()

group_1 = df[df["PetalLengthCm"] <= 1.2].shape[0]
group_2 = df[(df["PetalLengthCm"] > 1.2) & (df["PetalLengthCm"] < 1.5)].shape[0]
group_3 = df[df["PetalLengthCm"] >= 1.5].shape[0]

sizes_petal = [group_1, group_2, group_3]
labels_petal = [
    "≤ 1.2 см",
    "1.2 < x < 1.5 см",
    "≥ 1.5 см",
]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7))

ax1.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=90)
ax1.set_title('Доли ирисов по видам')
ax1.axis('equal')  

ax2.pie(sizes_petal,labels=labels_petal,autopct="%1.1f%%",startangle=90,colors=["#ffcc99", "#abcdef", "#c2c2f0"],)
ax2.set_title("Доли ирисов по длине лепестка (PetalLengthCm)")
ax2.axis('equal')

plt.tight_layout()
plt.show()