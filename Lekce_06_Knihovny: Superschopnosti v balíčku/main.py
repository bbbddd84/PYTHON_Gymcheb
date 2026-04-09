# Digitální věštírna
import random
import time

print("Vítej u Digitálního věštce!")
otazka = input("Zadej svou otázku (ano/ne): ")

print("Nahlížím do křišťálové koule...")
time.sleep(1.5)      # Dramatická pauza 1
print("...stahuji data z vesmíru...")
time.sleep(1.5)      # Dramatická pauza 2

stesti = random.randint(1, 100)

if stesti > 80:
    print("ODPOVĚĎ: Rozhodně ANO! Hvězdy ti přejí.")
elif stesti > 40:
    print("ODPOVĚĎ: Možná... zkus se zeptat později.")
else:
    print("ODPOVĚĎ: Bohužel, dnes to nevypadá dobře.")

print(f"\n(Tvé skóre štěstí pro tento pokus bylo: {stesti}/100)")


# ==========================================
# ÚKOL Č. 1: Kostka (Obtížnost: ⭐)
# Vytvoř program, který hodí kostkou (1-6).
# Pokud padne 6, vypiš: "VÍTĚZSTVÍ!". 
# Pokud padne cokoli jiného, vypiš: "Zkus to znovu."
# ==========================================

# SEM DOPLŇ SVŮJ KÓD:
import random

print("Házím kostkou...")
hod = random.randint(1, 6)

print(f"Padlo číslo: {hod}")

if hod == 6:
    print("VÍTĚZSTVÍ!")
else:
    print("Zkus to znovu.")


# ==========================================
# ÚKOL Č. 2: Cesta do školy (Obtížnost: ⭐⭐)
# Simuluj cestu do školy. Program si vylosuje náhodné číslo 1-3.
# 1 -> Šel jsi pěšky.
# 2 -> Jel jsi autobusem.
# 3 -> Jel jsi na drakovi.
# Pomocí if-elif-else vypiš příslušnou zprávu.
# ==========================================

# SEM DOPLŇ SVŮJ KÓD:
import random

print("Zjišťuji, jak ses dnes dostal do školy...")

cesta = random.randint(1, 3)

if cesta == 1:
    print("Šel jsi pěšky.")
elif cesta == 2:
    print("Jel jsi autobusem.")
else:
    print("Jel jsi na drakovi!")


# ==========================================
# ÚKOL Č. 3: Kreativní obrazec (Obtížnost: ⭐⭐⭐)
# Tvým úkolem je vytvořit "Digitální krystal".
# 1. Nech uživatele zadat jeho oblíbenou barvu.
# 2. Program náhodně vylosuje velikost krystalu (číslo 1-10).
# 3. Pokud je velikost větší než 5, vypiš krystal pomocí znaků (viz příklad níže).
# 4. Před výpisem přidej dramatickou pauzu 2 sekundy pomocí time.sleep().
#
# Příklad výstupu:
#      /\
#     /  \
#    /____\
# ==========================================

# SEM DOPLŇ SVŮJ KÓD:
import random
import time

print("Vítej v generátoru digitálního krystalu!")

barva = input("Zadej svou oblíbenou barvu: ")

velikost = random.randint(1, 10)

print("Krystal se formuje...")
time.sleep(2)

print(f"Tvoje energie barvy {barva} vytvořila krystal o velikosti {velikost}!")

if velikost > 5:
    print("\nTvůj krystal:")
    print("     /\\")
    print("    /  \\")
    print("   /    \\")
    print("  /______\\")
else:
    print("Krystal je příliš malý na zobrazení.")

# ==========================================
# ÚKOL Č. 4: Vytvoř "Digitální váhu", která náhodně vygeneruje hmotnost balíčku od 0.5 kg do 20.0 kg (pomocí uniform). Pokud váží víc než 15 kg, vypiš varování o těžkém nákladu.
# ==========================================

# SEM DOPLŇ SVŮJ KÓD:
import random

print("Digitální váha se spouští...")

hmotnost = random.uniform(0.5, 20.0)

print(f"Hmotnost balíčku: {hmotnost:.2f} kg")

if hmotnost > 15:
    print("POZOR: Těžký náklad!")
else:
    print("Balíček je v normě.")


# ==========================================
# ÚKOL Č. 5: Napište program, který bude simulovat jednoduchou hru o štěstí. Program si "vylosuje" náhodné celé číslo v rozmezí od 1 do 100 a uloží ho do proměnné stesti.

#Vaším úkolem je:

    # 1. Pomocí příkazu if zkontrolovat, zda je vylosované číslo větší než 50.

    # 2. Pokud je podmínka splněna, vypište na obrazovku zprávu: "Dnes máš štěstí!".

    # 3. Pokud podmínka splněna není (číslo je 50 nebo menší), použijte příkaz else a vypište: "Zkus to znovu.".
# ==========================================

# SEM DOPLŇ SVŮJ KÓD:
import random

print("Hra o štěstí začíná...")

stesti = random.randint(1, 100)

print(f"Tvoje číslo je: {stesti}")

if stesti > 50:
    print("Dnes máš štěstí!")
else:
    print("Zkus to znovu.")


# ==========================================
# Bonusová výzva:
# Zkuste program upravit tak, aby před vyhodnocením výsledku vypsal text "Házím kostkou..." a počkal 2 sekundy pomocí funkce time.sleep(), aby bylo napětí větší!
# ==========================================

# SEM DOPLŇ SVŮJ KÓD:
import random
import time

print("Hra o štěstí začíná...")

print("Házím kostkou...")
time.sleep(2)

stesti = random.randint(1, 100)

print(f"Tvoje číslo je: {stesti}")

if stesti > 50:
    print("Dnes máš štěstí!")
else:
    print("Zkus to znovu.")
