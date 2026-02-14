import kagglehub
import pandas as pd
import os

# 1. Pobieranie danych
path = kagglehub.dataset_download("akashkr/phishing-website-dataset")
print("Folder z danymi:", path)

# 2. Musimy połączyć ścieżkę do folderu z nazwą pliku
# Najbezpieczniej zrobić to za pomocą os.path.join
file_path = os.path.join(path, "dataset.csv")

# UWAGA: Sprawdź w print(path), czy plik faktycznie nazywa się "dataset.csv"
# Czasami w tym folderze jest inny podfolder lub inna nazwa pliku.

# 3. Wczytanie danych z pełnej ścieżki
dataset = pd.read_csv(file_path)

print(dataset.head())