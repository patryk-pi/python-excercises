# dana jest lista liczb
# program wypisuje parzyste oraz średnią z parzystych

# dana jest lista imion
# program wypisuje imiona żeńskie zaczynające się na "A", ale krótsze niż 6 liter


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# even_numbers = [number for number in numbers if number % 2 == 0]

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
#
# print(mean(even_numbers))

imiona = ['Ala', 'agnieszka', 'Beata', 'Iza', 'Andrzej', 'ala']
wybrane_imiona = []

# for imie in imiona:
#     imie = imie.lower()
#     if len(imie) > 6:
#         if imie[0] == 'a':
#             if imie[-1] == 'a':
#                 wybrane_imiona.append(imie)

imiona = ['Ala', 'agnieszka', 'Beata', 'Iza', 'Andrzej', 'ala']
wybrane_imiona = []

for imie in imiona:
    imie = imie.lower()
    if len(imie) > 6 and imie[0] == 'a' and imie[-1] == 'a':
        wybrane_imiona.append(imie)

print(wybrane_imiona)

print(wybrane_imiona)
