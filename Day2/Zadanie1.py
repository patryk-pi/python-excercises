import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6]])

print(mat.shape)  # zwraca rozmiar macierzy

print(np.sum(mat, axis = 0))  # sumuj w pionie czyli po kolumnach
print(np.sum(mat, axis = 1))  # sumuj w poziomie czyli po wierszach
