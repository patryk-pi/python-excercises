import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

import warnings

from pandas.core.reshape import encoding

warnings.filterwarnings('ignore')
# 1. pobieranie danych

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv"

try:
    df = pd.read_csv(url)
    print('dane pobrane')
except Exception as e:
    print(f'Bląd {e}')
    print('Uzywam danych zapasowych')
    data = {
        'nazwa': ['IPA', 'IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Ale', 'Bock'],
        'alkohol': [6.5, 6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8],
        'goryczka': [65, 65, np.nan, 45, 30, 15, 40, 35, 25],
        'ocena': [4.2, 4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],
        'styl': ['IPA', 'IPA', 'Lager', 'Ciemne', 'Lager', np.nan, 'Ciemne', 'Jasne', 'Ciemne']
    }
    df = pd.DataFrame(data)

print(df)

# 2. Podstawowe info
print('\n' + '=' * 50)
print(f'Wymiary danych: {df.shape}')
print(f'Liczba wierszy: {df.shape[0]}')
print(f'Liczba kolumn: {df.shape[1]}')

# 3. Podgląd danych
print("Pierwsze 5 piw:")
print(df.head())
print("\nOstatnie 5 piw:")
print(df.tail())
# print('\nDescribe')
# print(df.describe())

# 4. Typy danych
print(f'\n{df.info()}')

# 5. Statystyki numeryczne
kolumny_numeryczne = df.select_dtypes(include = 'number').columns

if len(kolumny_numeryczne) > 0:
    print('Stasystyki dla chech numerycznych:')
    print(df[kolumny_numeryczne].describe())
else:
    print('Brak kolumn numerycznych w danych')

# 6. Statystyki kategoryczne
print("\n" + "=" * 50)
print("STATYSTYKI KATEGORYCZNE")
print("=" * 50)

kolumny_tekstowe = df.select_dtypes(include = 'object').columns
if len(kolumny_tekstowe) > 0:
    for kolumna in kolumny_tekstowe:
        print(f'\nKolumna: {kolumna}')
        print(f'Liczba unikalnych wartości: {df[kolumna].unique()}')
        print('5 najczęstrzych wartości')
        print(df[kolumna].value_counts().head(3))
else:
    print('Brak kolumn kategorycznych w danych')

# 7. Brakujące wartości
print("\n" + "=" * 50)
print("BRAKUJĄCE WARTOŚCI")
print("=" * 50)

brakujace = df.isnull().sum()
if brakujace.sum() > 0:
    print('Kolumny z brakującymi wartościami:')
    for kolumna in df.columns:
        if df[kolumna].isnull().sum() > 0:
            braki_liczbowo = df[kolumna].isnull().sum()
            braki_procentowo = (braki_liczbowo / len(df)) * 100
            print(f'    {kolumna}: {braki_liczbowo} ({braki_procentowo:.1f})%')

# 8. Wizualizacje
print("\n" + "=" * 50)
print("TWORZENIE WYKRESÓW")
print("=" * 50)

# wykres 1, rozklad zawartosci alkoholu
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

# wykres 2, rozklad ocen
if 'ocena' in df.columns and False:
    plt.figure(figsize = (8, 5))
    df['ocena'].hist(bins = 8, color = 'lightgreen', edgecolor = 'black', alpha = 0.7)
    plt.title('Rozkład ocen piw')
    plt.xlabel('Ocena (w skali 1-5)')
    plt.ylabel('Liczba piw')
    plt.grid(axis = 'y', alpha = 0.3)
    plt.show()

# Wykres 3: Zależność między alkoholem a oceną
if 'alkohol' in df.columns and 'ocena' in df.columns and False:
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

# Wykres 4: Popularność stylów piw

if 'styl' in df.columns and False:
    plt.figure(figsize = (10, 6))
    df['styl'].value_counts().plot(kind = 'bar', color = 'orange', edgecolor = 'black')
    plt.title('Popularność stylów piw')
    plt.xlabel('Styl piwa')
    plt.ylabel('Liczba piw')
    plt.xticks(rotation = 45)
    plt.grid(axis = 'y', alpha = 0.3)
    plt.tight_layout()
    plt.show()

# Wykres 5: Macierz korelacji (jeśli są przynajmniej 2 kolumny numeryczne)
if len(kolumny_numeryczne) >= 2 and False:
    plt.figure(figsize = (8, 6))
    macierz_korelacji = df[kolumny_numeryczne].corr()
    sns.heatmap(macierz_korelacji, annot = True, cmap = 'coolwarm', center = 0)
    plt.title('Korelacje między cechami numerycznymi')
    plt.tight_layout()
    plt.show()

# 9. Analiza duplikatów
print("\n" + "=" * 50)
print("ANALIZA DUPLIKATÓW")
print("=" * 50)

duplikaty = df.duplicated()
# print(duplikaty)
if duplikaty.sum() > 0:
    print(f'Znaleziono {duplikaty.sum()} zduplikowanych wierszy')
    print('zduplikowane wiersze: ')
    print(df[duplikaty])
else:
    print('Brak duplikatów')

# Podsumowanie
print("\n" + "=" * 50)

print("PODSUMOWANIE ANALIZY")
print("=" * 50)

print("Analiza EDA zakończona pomyślnie!")
print(f"Przeanalizowano {len(df)} piw")
print(f"Liczba cech: {len(df.columns)}")

if len(kolumny_numeryczne) > 0:
    print("Znalezione cechy numeryczne:", list(kolumny_numeryczne))

if len(kolumny_tekstowe) > 0:
    print("Znalezione cechy kategoryczne:", list(kolumny_tekstowe))

# najlepiej ocenione
if 'ocena' in df.columns and 'nazwa' in df.columns:
    print("\n3 najwyżej oceniane piwa")
    najlepsze = df.nlargest(3, 'ocena')[['nazwa', 'ocena']]
    print(najlepsze)

# najzwyższa zawartosć alko
if 'alkohol' in df.columns and 'nazwa' in df.columns:
    print("\n3 piwa z najwyższą zawartością alkoholu:")
    mocne = df.nlargest(3, 'alkohol')[['nazwa', 'alkohol']]
    print(mocne)

print("\n" + "=" * 50)

POKAZ_WYKRESY = False

ZAPISZ_WYKRESY = False

print("\n" + "=" * 50)
print('ANALIZA OUTLIERÓW')
print("\n" + "=" * 50)

if len(kolumny_numeryczne) > 0:
    for kolumna in kolumny_numeryczne:
        Q1 = df[kolumna].quantile(0.25)
        Q3 = df[kolumna].quantile(0.75)
        # Rozstęp międzykwartylowy
        IQR = Q3 - Q1
        dolna_granica = Q1 - 1.5 * IQR
        gorna_granica = Q3 - 1.5 * IQR

        outliers = df[(df[kolumna] < dolna_granica) | (df[kolumna] > gorna_granica)]

        print(f'Outliery w {kolumna}: {len(outliers)}')

if "styl" in df.columns and 'ocena' in df.columns:
    print("\nŚrednie oceny wg stylów")

    styl_stats = df.groupby('styl').agg({
        'ocena': ['mean', 'count'],
        'alkohol': 'mean'
    }).round(2)

    print(styl_stats)

if 'styl' in df.columns and 'ocena' in df.columns and 'alkohol' in df.columns and POKAZ_WYKRESY:
    plt.figure(figsize = (12, 6))

    styl_grouped = df.groupby('styl').agg({
        'ocena': 'mean',
        'alkohol': 'mean',
        'nazwa': 'count'
    }).rename(columns = {'nazwa': 'count'})

    plt.scatter(styl_grouped['alkohol'],
                styl_grouped['ocena'],
                s = styl_grouped['count'] * 50,
                alpha = 0.6
                )

    for style, row in styl_grouped.iterrows():
        plt.annotate(style,
                     (row['alkohol'], row['ocena']),
                     xytext = (5, 5),
                     textcoords = 'offset points',
                     )

    plt.xlabel('Średnia zawartość alkohou %')
    plt.ylabel('Średnia ocena')
    plt.title('Porównanie stylów piw')
    plt.grid(True, alpha = 0.3)

    if ZAPISZ_WYKRESY:
        plt.savefig('styl_piw_porownanie.png',
                    dpi = 300,
                    bbox_inches = 'tight',  # przyciecie marginesow
                    )

    plt.show()

if len(kolumny_numeryczne) >= 2 and POKAZ_WYKRESY:
    sns.pairplot(df[kolumny_numeryczne])

    plt.suptitle('Pairplot zmiennych numerycznych', y = 1.02)

    if ZAPISZ_WYKRESY:
        plt.savefig('styl_piw_pairplot_wykresy.png',
                    dpi = 300,
                    bbox_inches = 'tight'
                    )

# CZYSZCZENIE DANYCH

print("\n" + "=" * 50)
print('Propozycje czyszczenia dancyh')
print("\n" + "=" * 50)

if 'goryczka' in df.columns and df['goryczka'].isnull().sum() > 0:
    median_goryczka = df.groupby('styl')['goryczka'].transform('median')
    df['goryczka_uzupełniona'] = df['goryczka'].fillna(median_goryczka)

    print(f'Uzupełniono {df['goryczka'].isnull().sum()} brakujących wartosci goryczki')

# USUWANIE DUPLIKATOW

if duplikaty.sum() > 0:
    df_cleaned = df.drop_duplicates()

    print(f'Usunieto {duplikaty.sum()} duplikatów')

else:
    df.cleaned = df.copy()

df_cleaned['kategoria_alkohol'] = pd.cut(df_cleaned['alkohol'],
                                         # granice przedzialow
                                         bins = [0, 5, 6.5, 10],
                                         # nazwy kategorii
                                         labels = ['lekkie', 'średnie', 'mocne'])

print("\n Kategorie alkoholowe:")
print(df_cleaned['kategoria_alkohol'].value_counts())

df_cleaned.to_csv('piwa_przetworzone', index = False)
print("\n" + "=" * 50)
print("\n" + "=" * 50)
print("\n" + "=" * 50)

with open('raport_analizy.txt', 'w', encoding = 'utf-8') as f:
    f.write("Raport analizy piw \n")
    f.write(f'{"=" * 50} \n')
    f.write(f'Liczba przeanalizowanych piw: {len(df)} \n')
    f.write(f'Liczba cech: {len(df.columns)} \n')

    if 'ocena' in df.columns:
        f.write(f'Średnia ocena: {df['ocena'].mean(): 2f} \n')
        f.write(f'Mediana oceny: {df['ocena'].median(): 2f} \n')

    if 'alkohol' in df.columns:
        f.write(f'Średnia zawartość alkoholu: {df['alkohol'].mean(): 2f} \n')
        f.write(f'Mediana zawartości alkoholu: {df['alkohol'].median(): 2f} \n')


def znajdz_piwa (df, min_ocena = None, max_alcohol = None, styl = None):
    filter = pd.Series([True] * len(df))  # wszystkie piwa spełniają warunki
    if min_ocena is not None:
        filter &= df['ocena'] >= min_ocena
    if max_alcohol is not None:
        filter &= df['alkohol'] <= max_alcohol
    if styl is not None:
        filter &= df['styl'] == styl
    return df[filter]


if all(col in df.columns for col in ['ocena', 'alkohol', 'styl']):
    print('\n Piwa z oceną > 4.0 i alkoholem < 6%')

    print(znajdz_piwa(df, min_ocena = 4, max_alcohol = 6))

# ANALIZA KORELACJI I ZALEŻNOŚCI

print("\n" + "=" * 50)
print("Szczegółowa analiza korelacji i zależności")
print("\n" + "=" * 50)

if len(kolumny_numeryczne) >= 2:
    print("Macierz korelacji")

    macierz_korelacji = df[kolumny_numeryczne].corr()
    print(macierz_korelacji.round(3))

    # nagłowek do interpretacji korelacji
    print('\n ===== INTERPRETACJA KORELACJI =====')
    for i in range(len(macierz_korelacji.columns)):
        for j in range(i + 1, len(macierz_korelacji.columns)):
            kol1 = macierz_korelacji.columns[i]
            kol2 = macierz_korelacji.columns[j]
            korelacja = macierz_korelacji.iloc[i, j]

            # interpretacja siły korelacji

            if abs(korelacja) > 0.7:
                silna = "BARDZO SILNA"
            elif abs(korelacja) >= 0.5:
                silna = "SILNA"
            elif abs(korelacja) >= 0.3:
                silna = 'UMIARKOWANA'
            else:
                silna = "SŁĄBY ZWIĄZEK LUB JEGO BRAK"

            # interpretacja kierunku

            if korelacja > 0:
                # dodatnia korelacja, gdzie rosna 2 zmienne
                kierunek = "dodatnia"
            elif korelacja < 0:
                # ujemna korelacja, gdzie 1 zmienna rośnie, a druga maleje
                kierunek = "ujemna"
            else:
                kierunek = "brak korelacji"

            print(f'{kol1} vs {kol2}: {korelacja: .3f} ({silna} korelacja) {kierunek}')

# analiza jak styl piwa wpływa na cechy numeryczne

if 'styl' in df.columns and len(kolumny_numeryczne) > 0:
    print('\n ===== WPŁYW STYLU NA CECHY NUMERYCZNE =====')

    for kolumna_num in kolumny_numeryczne:
        statystyki_styl = df.groupby('styl')[kolumna_num].agg(['mean', 'std', 'min', 'max']).round(2)
        print(f'\n analiza {kolumna_num.upper()} według stylów')
        print(statystyki_styl)

# Szczegółowa analiza rozkładu danych

print('\n' + '=' * 50)
print('Szczegółowa analiza rozkładu danych')
print('\n' + '=' * 50)

for kolumna in kolumny_numeryczne:
    print(f'\n ===== ANALIZA ROZKŁADU: {kolumna.upper()} ======')
    dane = df[kolumna].dropna()
    print(f'Liczba wartości: {len(dane)}')
    print(f'Średnia: {dane.mean(): 3f}')
    print(f'Mediana: {dane.median(): 3f}')
    print(f'Wariancja: {dane.var: 3f}')
    print(f'Minimum: {dane.min(): 3f}')
    print(f'Maximum: {dane.max(): 3f}')
    print(f'Zakres: {dane.max() - dane.min(): 3f}')
