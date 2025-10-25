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
print(df['styl'])

# podstawowe informacje

print('\n' + "=" * 50)

print(f'Wymiary danych: {df.shape}')
print(f'Liczba wierszy: {df.shape[0]}')
print(f'Liczba kolumn: {df.shape[1]}')

# podglad danych
print(f'Pierwsze 5 piw: {df.head()}')
print(f'\n Ostatnie 5 piw: {df.tail()}')
print(f"\n Describe")
print(df.describe())

# typy danych
print(f"\n {df.info()}")

# statystyki numeryczne
kolumny_numeryczne = df.select_dtypes(include = 'number')
print(kolumny_numeryczne)

if len(kolumny_numeryczne) > 0:
    print('Statystyki dla cech numerycznych:')
    print(kolumny_numeryczne.describe())

# statystyki kategoryczne
print('\n' + "=" * 50)
print('Statystyki kategoryczne')
print('\n' + "=" * 50)

# kolumny_tekstowe = df.select_dtypes(exclude = 'number')
kolumny_tekstowe = df.select_dtypes(include = 'object')
print(kolumny_tekstowe)

if len(kolumny_tekstowe) > 0:
    for kolumna in kolumny_tekstowe:
        print(f"\n Kolumna: {kolumna}")
        print(f"Liczba unikalnych wartości: {len(df[kolumna].unique())}")
        print('3 najczestsze wartości')
        print(df[kolumna].value_counts().head(3))
else:
    print("Brak kolumnt kategorycznych w danych")

# brakujące wartości
print('\n' + "=" * 50)
print('Brakujace wartosci')
print('\n' + "=" * 50)

print(df.isnull().sum())

brakujace = df.isnull().sum().sum()

if brakujace > 0:
    print("Kolumny z brakującymi wartościami:")
    for kolumna in df.columns:
        if df[kolumna].isnull().sum() > 0:
            braki_liczbowo = df[kolumna].isnull().sum()
            braki_procentowo = (braki_liczbowo / len(df) * 100)
            print(f"      {kolumna}: {braki_procentowo}")
else:
    print("Wszystkie dane poprawne")

# wizualizacje

print('\n' + "=" * 50)
print('Tworzenie wykresów')
print('\n' + "=" * 50)

# wykres 1 zawartosci alkoholu
if 'alkohol' in df.columns:
    plt.figure(figsize = (10, 6))
    plt.subplot(1, 2, 1)

    plt.hist(df['alkohol'])
    plt.title('Histogram of alkohol')
    plt.xlabel('Alkohol w %')
    plt.ylabel('Liczba piw')
    plt.show()

if 'alkohol' in df.columns and False:
    plt.figure(figsize = (10, 6))
    plt.subplot(1, 2, 1)  # z lewej
    df['alkohol'].hist(bins = 10, color = 'lightblue', edgecolor = 'black')
    plt.title('Rozklad zawartosci alkoholu')
    plt.xlabel('Zawartosc alko w (%)')
    plt.ylabel('Liczba piw')
    plt.subplot(1, 2, 2)  # z prawej
    df.boxplot(column = 'alkohol', grid = False)
    plt.title('Boxplot: Zawartość alkoholu')
    plt.tight_layout()
    plt.show()

# wykres 2 rozklad ocen

plt.figure(figsize = (8, 5))
df['ocena'].hist(bins = 8, color = 'lightblue', alpha = 0.8)
plt.title('Rozkład ocen piw')
plt.xlabel('Ocena piw 1-5')
plt.ylabel('Liczba piw')
plt.grid(axis = 'y', alpha = 0.3)
plt.show()

# Wykres 3: Zależność między alkoholem a oceną
if 'alkohol' in df.columns and 'ocena' in df.columns:
    plt.figure(figsize = (8, 6))
    plt.scatter(df['alkohol'], df['ocena'], alpha = 0.6, s = 60, color = 'purple')
    plt.title('Zależność między zawartością alkoholu a oceną')
    plt.xlabel('Zawartość alkoholu (%)')
    plt.ylabel('Ocena')
    plt.grid(True, alpha = 0.3)

    # linia trendu
    z = np.polyfit(df['alkohol'], df['ocena'], 1)
    p = np.poly1d(z)
    plt.plot(df['alkohol'], p(df['alkohol']), "r--", alpha = 0.8)

    plt.show()

# Wykres 5: Macierz korelacji (jeśli są przynajmniej 2 kolumny numeryczne)
if len(kolumny_numeryczne) >= 2:
    plt.figure(figsize = (8, 6))
    macierz_korelacji = df[kolumny_numeryczne].corr()
    sns.heatmap(macierz_korelacji, annot = True, cmap = 'coolwarm', center = 0)
    plt.title('Korelacje między cechami numerycznymi')
    plt.tight_layout()
    plt.show()

# duplikaty

print('\n' + "=" * 50)
print('Analiza duplikatow')
print('\n' + "=" * 50)

# print(df.duplicated())
# print(df['styl'].duplicated())

duplikaty = df.duplicated()
if duplikaty.sum() > 0:
    print(f"Znaleziono {duplikaty.sum()} zduplikowanych wierszy")
else:
    print("Brak duplikatow")

### PODSUMOWANIE
