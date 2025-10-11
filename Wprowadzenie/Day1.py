# @formatter:on
# print("Witaj")
# # imie = input("Podaj imię")
#
# # print("Witaj", imie)
#
# a = 5
# a = int(a)
# b = 7
#
# print(a + b)
# print("suma a i b wynosi:", a + b)
#
# slownik = ["kot", "pies", "tata", "5"]
#
# print("Zmienna a jest typu", type(a), "zmienna słownik jest typu", type(slownik))


# wiek = int(input("Podaj wiek: "))
#
# if wiek < 18:
#     print(f"Masz {wiek} lat")
#     print(f"Będziesz pełnoletni za {18 - wiek} lat")
# else:
#     print("Jesteś pełnoletni, rób co chcesz")
#
#
#
# print("Koniec programu")

# correct_password = 1234
# password = int(input("Enter your password: "))
# if password != correct_password:
#     print("Hasło niepoprawne")
# else:
#     print("Hasło poprawne")
#
#
# zarobki_brutto = int(input("Podaj zarobki brutto: "))
# liczba_dzieci = int(input("Podaj liczbę dzieci: "))


# Rozwiazanie A
# dodatek_na_dziecko = 500
# podatek1 = 0.2
# podatek2 = 0.1
# zarobki = (zarobki_brutto - (zarobki_brutto * podatek1) ) + liczba_dzieci * dodatek_na_dziecko
# print(zarobki, zarobki_brutto - (zarobki_brutto * podatek1) )

# Rozwiązanie B

# if zarobki_brutto < 3000:
#     podatek = 0
# elif zarobki_brutto >= 3000 and zarobki_brutto < 5000:
#     podatek = 0.1
# else:
#     podatek = 0.2
#
# # Dodatek na dzieci (tylko na 2 i 3 dziecko)
# if liczba_dzieci < 2:
#     dodatek_na_dziecko = 0
# else:
#     dodatek_na_dziecko = 500 * min(liczba_dzieci - 1, 2)
#
# # Zarobki netto
# zarobki_netto = zarobki_brutto - zarobki_brutto * podatek + dodatek_na_dziecko
#
# print(f"Zarobki netto: {zarobki_netto} zł")

# Zadanie 2

# typ = input("Podaj typ mieszkania (cegła/płyta): ").lower()
#
# if typ !="cegła" and typ != "płyta":
#     print("Nieznany typ mieszkania")
#     exit()
#
# powierzchnia = float(input("Powierzchnia: "))
#
# if typ == "cegła":
#     koszt_dzień = powierzchnia * 0.3
# elif typ == "płyta":
#     koszt_dzień = powierzchnia * 0.5
#
# koszt_miesiac = koszt_dzień * 30
#
# print(koszt_miesiac)

#### LISTY

# lista = [4, 5, 7, 8]
# print(max(lista))
# print(min(lista))
# print(sum(lista))
# print(sorted(lista))

people = ["Mateusz", "Olaf", "Bartek", "Andrzej"]
# print(sorted(people))
# people.remove("Andrzej")

lista_zakupów = ["jajka", "mleko", "chleb", ["John", "Paul"]]

print(lista_zakupów[-1][1])
print(lista_zakupów[len(lista_zakupów) - 1][0])
