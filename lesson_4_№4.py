import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')

features = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

combinations = [
    ('SepalWidthCm', 'SepalLengthCm', 'SepalLength от SepalWidth'),
    ('PetalLengthCm', 'SepalLengthCm', 'SepalLength от PetalLength'),
    ('PetalWidthCm',  'SepalLengthCm', 'SepalLength от PetalWidth'),
    ('PetalLengthCm', 'SepalWidthCm',  'SepalWidth от PetalLength'),
    ('PetalWidthCm',  'SepalWidthCm',  'SepalWidth от PetalWidth'),
    ('PetalWidthCm',  'PetalLengthCm', 'PetalLength от PetalWidth')
]

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
axes = axes.flatten() 

colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}

for i, (x_col, y_col, title) in enumerate(combinations):
    ax = axes[i]

    for species, group in df.groupby('Species'):
        ax.scatter(group[x_col], group[y_col], 
                   label=species, alpha=0.6, color=colors.get(species, 'gray'))
    
    k, b = np.polyfit(df[x_col], df[y_col], 1)

    x_line = np.linspace(df[x_col].min(), df[x_col].max(), 100)
    y_line = k * x_line + b
    
    ax.plot(x_line, y_line, color='black', linestyle='--', linewidth=2)
    
    ax.text(0.05, 0.95, f'y = {k:.2f}x + {b:.2f}', 
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(title)
    ax.grid(True, linestyle='--', alpha=0.5)

    if i == 0:
        ax.legend()

plt.tight_layout()
plt.show()