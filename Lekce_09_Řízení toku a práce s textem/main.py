import time

# ==========================================
# ÚKOL 1: Odpočet s pauzou
# Vypište čísla od 5 do 1. Mezi každým číslem program počká 1 sekundu.
# Nakonec vypište "START!".
# ==========================================
print("--- Úkol 1: Odpočet ---")

# ZDE DOPRACOVAT KÓD
import time

print("--- Úkol 1: Odpočet ---")

# Cyklus počítá od 5 do 1 (krok -1 znamená odčítání)
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)  # Pauza 1 sekunda mezi čísly

print("START!")

# ==========================================
# ÚKOL 2: Break
# Procházejte seznam ovoce. Vypisujte názvy, ale pokud narazíte na "banan",
# vypište "Banán nalezen, končím!" a okamžitě ukončete cyklus.
# ==========================================
print("\n--- Úkol 2: Stop na banánu ---")
ovoce = ["jablko", "hruska", "banan", "pomeranc", "jahoda"]

# ZDE DOPRACOVAT KÓD
print("\n--- Úkol 2: Stop na banánu ---")
ovoce = ["jablko", "hruska", "banan", "pomeranc", "jahoda"]

for item in ovoce:
    if item == "banan":
        print("Banán nalezen, končím!")
        break  # Okamžitě ukončí celý cyklus
    print(item)

# ==========================================
# ÚKOL 3: Continue
# Vypište všechna lichá čísla v rozsahu 1 až 10.
# Použijte příkaz 'continue' pro přeskočení sudých čísel.
# ==========================================
print("\n--- Úkol 3: Přeskoč sudá ---")

# ZDE DOPRACOVAT KÓD
print("\n--- Úkol 3: Přeskoč sudá ---")

for i in range(1, 11):
    if i % 2 == 0:
        continue  # Přeskočí sudá čísla
    print(i)

# ==========================================
# ÚKOL 4: Metoda .join()
# Máte seznam slov níže. Spojte je do jedné věty oddělené " - ".
# Výsledek vypište.
# ==========================================
print("\n--- Úkol 4: Spojování slov ---")
slova = ["Python", "je", "super", "jazyk"]

# ZDE DOPRACOVAT KÓD
print("\n--- Úkol 4: Spojování slov ---")
slova = ["Python", "je", "super", "jazyk"]

vysledek = " - ".join(slova)
print(vysledek)

# ==========================================
# ÚKOL 5: For - Else (Hledání čísla)
# Hledejte číslo 10 v seznamu 'cisla'. Pokud ho najdete, vypište "Nalezeno" 
# a ukončete cyklus. Pokud tam nebude, vypište "Číslo 10 v seznamu není"
# pomocí konstrukce 'else' za cyklem.
# ==========================================
print("\n--- Úkol 5: Hledání s Else ---")
cisla = [1, 3, 7, 11, 15] 

# ZDE DOPRACOVAT KÓD
print("\n--- Úkol 5: Hledání s Else ---")
cisla = [1, 3, 7, 11, 15]

for cislo in cisla:
    if cislo == 10:
        print("Nalezeno")
        break  # Pokud najdeme, ukončíme cyklus
else:
    # Tento blok se provede jen pokud nedošlo k break
    print("Číslo 10 v seznamu není")
