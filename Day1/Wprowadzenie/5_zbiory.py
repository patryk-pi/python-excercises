liczby = {
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
}

losowanie1 = {
    1,
    3,
    5,
    4,
}

losowanie2 = {
    1,
    7,
    8,
    10,
    4
}

unikalne_losowane_liczby = losowanie1 ^ losowanie2
print(unikalne_losowane_liczby)

losowane_wspolne_liczby = losowanie1 & losowanie2
print(losowane_wspolne_liczby)

niewylosowane_liczby = liczby - losowanie1 - losowanie2
print(niewylosowane_liczby)

polaczone_losowania = losowanie1 | losowanie2
print(polaczone_losowania)
