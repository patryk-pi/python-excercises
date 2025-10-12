import random

wylosowana_liczba = random.randint(1, 100)

print("Zgadnij jaką liczbę mam na myśli (1-100")

print(wylosowana_liczba)

while True:
    liczba = int(input("Podaj liczbęb 1-100: "))

    if liczba > wylosowana_liczba:
        print("Twoja liczba jest większa")
    elif liczba < wylosowana_liczba:
        print("Twoja liczba jest mniejsza")
    else:
        print("Gratulacje, zgadłeś!", wylosowana_liczba)
