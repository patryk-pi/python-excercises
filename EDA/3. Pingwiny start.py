import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')
print(type(penguins))
print(penguins.head().to_string())

# sns.pairplot(penguins, hue = 'species')
# plt.show()

penguins_filtered = penguins.drop(columns = ['island', 'sex']).dropna()
penguins_features = penguins_filtered.drop(columns = ['species'])
penguins_target = pd.get_dummies(penguins_filtered['species'])
