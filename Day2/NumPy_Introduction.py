# @formatter:on

### Petla FOR
ceny = [15, 20, 18, 30]
nowe_ceny = []

for cena in ceny:
    nowe_ceny.append(cena + 2)

print(nowe_ceny)

### NumPy

import numpy as np

np_ceny = np.array([15, 20, 18, 30])
# np_nowe_ceny = np_ceny + 2

np_nowe_ceny = np_ceny - 2

print(np_nowe_ceny * 2)
print(np.mean(np_nowe_ceny))  # SREDNIA
print(np.max(np_nowe_ceny))
