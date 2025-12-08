import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Symulacja Ładowania Danych (Zamiast pliku CSV, tworzymy DataFrame)
# Zmienne związane z Twoimi zainteresowaniami (np. osiągi samochodów)
data = {
    'Model': ['RX-7', 'S2000', 'GT-R', 'Supra', 'Miata'],
    'HP': [276, 247, 565, 335, 181],
    'Weight_kg': [1260, 1260, 1750, 1540, 1050],
    'Country': ['Japan', 'Japan', 'Japan', 'Japan', 'Japan']
}
df = pd.DataFrame(data)

print("--- 1. Podstawowy Przegląd Danych ---")
print("Kształt danych (wiersze, kolumny):", df.shape)
print("\nPierwsze 5 wierszy:")
print(df.head())

# 2. Kluczowe Statystyki Opisowe (ROI na szybkości!)
print("\n--- 2. Statystyki Opisowe (HP i Waga) ---")
print(df[['HP', 'Weight_kg']].describe())

# 3. Prosta Wizualizacja (Obowiązkowa dla zrozumienia danych)
# Wykres słupkowy mocy (HP) dla różnych modeli.
plt.figure(figsize=(8, 5))
plt.plot(df['Model'], df['HP'], marker='o', linestyle='--', color='red')
plt.title('Moc (HP) Wybranych Japońskich Samochodów Sportowych', fontsize=14)
plt.xlabel('Model Samochodu')
plt.ylabel('Moc (HP)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.show()

# Opcjonalnie: Obliczanie stosunku mocy do wagi (Power-to-Weight Ratio)
df['Power_to_Weight'] = df['HP'] / df['Weight_kg']
print("\n--- 3. Wskaźnik Mocy do Wagi (Kluczowy dla Osiągów) ---")
print(df[['Model', 'Power_to_Weight']].sort_values(by='Power_to_Weight', ascending=False))
