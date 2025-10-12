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

age = int(input("Ile masz lat? "))

if age <= 0:
    print("Zły wiek")
elif age < 18:
    print(f"Masz {age} lat")
    print(f"Będziesz dorosły za {18 - age} lat")
else:
    print(f"Masz {age} lat")
    print("Jesteś pełnoletni")

print("Koniec programu")
