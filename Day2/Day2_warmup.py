# @formatter:on

# print("Ala ma kota. \nKot ma Alę.")

slowo = "Mama"
napis = "PieS piesek PIEs"
lista_napis = napis.split()

print(slowo.capitalize())
print(slowo.replace("m", "M", 1))
print(napis.lower())
print(len(lista_napis))

### PETLE

# age = int(input("Ile masz lat? "))
#
# if age <= 0:
#     print("Zły wiek")
# elif age < 18:
#     print(f"Masz {age} lat")
#     print(f"Będziesz dorosły za {18 - age} lat")
# else:
#     print(f"Masz {age} lat")
#     print("Jesteś pełnoletni")
#
# print("Koniec programu")

# Walidator karty do bankomatu

poprawny_pin = 1234

# for i in range(3):
#     wprowadzony_pin = int(input("Podaj PIN: "))
#     if wprowadzony_pin == poprawny_pin:
#         print(poprawny_pin, "Zapraszam do wypłaty gotówki")
#         break
#     else:
#         print(f"Pin niepoprawny, zostało {2 - i} prób")
#         if i == 2:
#             print("Karta zablokowana")

liczba_prob = 3

while True:
    wprowadzony_pin = (input("Podaj PIN: "))
    if wprowadzony_pin == poprawny_pin:
        print(poprawny_pin, "Zapraszam do wypłaty gotówki")
        break
    else:
        liczba_prob -= 1
        print(f"Pin niepoprawny, zostało {liczba_prob}")
        if liczba_prob == 0:
            print("Karta zablokowana")
            break
