import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv")  # df = data frame - ramka danych

# print("Pierwsze 5 wierszy danych: \n", df.head(), "\n")  # head pokazuje pierwsze wiersze
# print("Informacje o kolumnach: \n", df.info())  # typy danych i informacje nie puste

print("Podstawowe statystyki opisowe")
# print(df.describe())  # podstawowe statystyki - średnia
#
# statystyki = df.describe()
# print(statystyki.mean())

# mean_per_class = df.groupby("class")["sepallength"].mean()
# print("Średnia długość sepal_lenght dla każdego gatunku: \n", mean_per_class)
#
# filtered = df[df["petalwidth"] > 1.5]
# print("Rekordy, gdzie petal_width jest > 1.5: \n", filtered)

plt.figure()  # Bez tego nie otworzą sie 2 wykresy na raz - tylko pojedynczo
plt.hist(df[df["class"] == "Iris-setosa"]["sepallength"], bins = 25)

plt.figure()
plt.scatter(df.sepallength, df.sepalwidth, color = "red")
plt.show()
