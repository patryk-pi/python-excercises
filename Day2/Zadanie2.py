import numpy as np

oceny = np.array([
    [4, 3, 5],
    [2, 3, 1],
    [5, 5, 6],
    [2, 4, 5]
])

print("Macierz ocen: \n", oceny)

srednie_uczniow = np.mean(oceny, axis = 1)
print("Średnia ocen każdego ucznia: \n", srednie_uczniow)

srednie_przedmiotow = np.mean(oceny, axis = 0)
print("Średnia ocen z przedmiotów: \n", srednie_przedmiotow)

max_ocena = np.max(oceny)
print("Najwyższa ocena w klasie: ", max_ocena)

oceny_nowe = oceny + 1
print("Oceny po podwyżce: ", oceny_nowe)
