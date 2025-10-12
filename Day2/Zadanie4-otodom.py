# @formatter:on

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("otodom (1).csv")
# print(df.head(10))  # Wyswielta defaultowo pierwsze 5 wierszy, mozna podac jako argument ilosc wierszy do wyswietlenia
# print(df.tail(10))  # Wyswielta defaultowo ostatnie 5 wierszy, mozna podac jako argument ilosc wierszy do wyswietlenia
# print(df.describe().T)  # T robie transpozycje kolumn z wierszami

print(df.isnull().sum())
# df = df.dropna() # usuwa wiersze z zerami

df['price_per_m2'] = df['price'] / df["space"]
df['is_new'] = df["year"] > 2015
df['floors_left'] = df["no_of_floors"] - df["floor"]  # ile pięter jest nad nami

# print(df[df["no_of_rooms"] > 3])
# print(df[(df["price"] > 500000) & (df["space"] > 60)])

# print(df.groupby('no_of_rooms')['price_per_m2'].mean())  # cena za m2 zależna od liczby pokoi
print(df.groupby('no_of_floors')['space'].mean())

# Aggregacja

print(df.groupby('no_of_rooms').agg({
    'price': 'mean',
    'space': 'mean',
    'price_per_m2': 'mean',
}))

print(df.sort_values('price', ascending = False).head())
df.to_csv("otodom_clean.csv", index = False)
