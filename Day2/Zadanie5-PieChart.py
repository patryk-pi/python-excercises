# @formatter:on

import matplotlib.pyplot as plt

lista_wydatkow = ["mieszkanie", "media", "jedzenie", "rozrywka", "nauka", "inwestycje"]
wydatki = [3000, 300, 1000, 500, 200, 1500]

explode = [0 for i in lista_wydatkow]
explode[3] = 0.3
explode[lista_wydatkow.index("inwestycje")] = 0.2

plt.pie(
    wydatki,  # <-- dane, a nie 'values'
    labels = lista_wydatkow,  # <-- etykiety
    explode = explode,
    autopct = "%.2f%%",  # dodaj %% żeby pokazać znak procenta
    shadow = True,
)

plt.title("Struktura wydatków")
plt.show()
