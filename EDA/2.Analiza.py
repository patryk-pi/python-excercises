import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pobieranie danych

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv"

try:
    df = pd.read_csv(url)
    print("dane pobrane")
except Exception as e:
    print(e)
    print("błąd danych")
    print("Używam dancyh zapasowych")
    data = {'nazwa': ['IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Ale', 'Bock'],
            'alkohol': [6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8], 'goryczka': [65, 25, 45, 30, 15, 40, 35, 25],
            'ocena': [4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],
            'styl': ['IPA', 'Lager', 'Ciemne', 'Lager', 'Pszeniczne', 'Ciemne', 'Jasne', 'Ciemne']}
    df = pd.DataFrame(data)

print(df)

# podstawowe informacje
