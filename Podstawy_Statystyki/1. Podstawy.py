import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# DANE Z ZADANIA
wyniki = np.array([65, 70, 75, 80, 80, 85, 85, 85, 90, 95, 100, 150])


def separator (text):
    print("=" * 50, text, "=" * 50, sep = "\n")


separator("STATYSTYKA OPISOWA - PODSTAWOWE MIARY")

# Miary tendencji centralnej
print("1. MIARY TENDENCJI CENTRALNEJ")
print("=" * 40)
print(f"Średnia arytmetyczna: {np.mean(wyniki): .2f} pkt")
print(f"Mediana:              {np.median(wyniki): .2f} pkt")
print(f"Moda:                  {stats.mode(wyniki, keepdims = True).mode[0]} pkt")

# Miary rozproszenia
print("\n1. MIARY ROZPROSZENIA")
print("=" * 40)
print(f"Minimum:              {np.min(wyniki): .2f} pkt")
print(f"Maksimum:             {np.max(wyniki): .2f} pkt")
print(f"Rozstęp:              {np.ptp(wyniki): .2f} pkt")
print(f"Wariancja:            {np.var(wyniki, ddof = 1): .2f} pkt^2")
print(f"Odchylenie std:       {np.var(wyniki, ddof = 1): .2f} pkt")
