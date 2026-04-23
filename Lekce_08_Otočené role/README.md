# Projekt: Otočené role – Staň se tvůrcem!

Vítejte u Vašeho prvního samostatného projektu! Tentokrát neplníš úkoly, které jsem připravil já, ale Vy sami vytváříte program, který mi nasdílíte k vyzkoušení. Ukážeme si, jak dokážete zkombinovat vše, co jsme se zatím naučili.

## Co musíte dodržet:

**Originální nápad:**

Vytvořte program, který kombinuje knihovny random (náhoda) a time.sleep (pauzy).

K tomu přidejte buď vizuální část pomocí Turtle (kreslení), nebo ASCII art (obrázky z písmenek).

Příklad: Digitální věštkyně, která po chvilce napětí (pauza) vybere náhodnou odpověď a vykreslí ji želvou, nebo generátor náhodných ASCII příšerek.

Vysvětlivky v kódu (Dokumentace):

Používejte komentáře #.

Musím z Vašeho kódu pochopit, proč jste použili právě tuto podmínku, tento cyklus nebo proč jste zvolili danou funkci. Kód by měl být srozumitelný i pro někoho, kdo ho vidí poprvé.

## README je Vaše vizitka:

Přímo sem do tohoto souboru (pod toto zadání) napište krátké shrnutí:

Co program dělá?

Proč jste si vybrali právě toto téma?




import random
import time

# Tento program vytváří náhodnou ASCII příšerku.
# Používám knihovnu random pro náhodný výběr vlastností
# a time.sleep pro krátké pauzy, aby program působil napínavěji.


def vypis_pomaly(text, pauza=0.8):
    # Funkce vypíše text a potom na chvíli počká.
    # Díky tomu program nepůsobí "usekaně" a má lepší atmosféru.
    print(text)
    time.sleep(pauza)


def vytvor_jmeno():
    # Jméno skládám ze dvou náhodných částí.
    # Rozdělení na začátek a konec jména mi umožní vytvořit více kombinací.
    zacatky = ["Gru", "Zlo", "Mra", "Fuf", "Kru", "Bla", "Šmo", "Drco"]
    konce = ["lík", "bor", "drak", "ťas", "ňous", "zoun", "prcek", "mon"]
    return random.choice(zacatky) + random.choice(konce)


def vytvor_oblicej():
    # Tady náhodně vybírám oči, pusu a doplněk.
    # Každá část se vybírá zvlášť, takže vzniká hodně různých obličejů.
    oci = random.choice(["o o", "O O", "- -", "^ ^", "@ @", "* *"])
    pusa = random.choice(["___", "~~~", "\\_/", "oOo", "---", "www"])
    doplnek = random.choice(["rohy", "čepice", "uši", "antény", "nic"])

    # Podmínka if rozhoduje, jak bude vypadat horní část příšerky.
    # Použil jsem ji proto, že některé doplňky mají vlastní speciální vzhled.
    if doplnek == "rohy":
        hlava = "  /\\   /\\\\"
    elif doplnek == "čepice":
        hlava = "  _____"
    elif doplnek == "uši":
        hlava = " (\\   /)"
    elif doplnek == "antény":
        hlava = "  | | | |"
    else:
        hlava = "         "

    # Vrátím všechny části obličeje najednou.
    return hlava, oci, pusa, doplnek


def vytvor_telo():
    # Náhodně vybírám styl těla a rukou.
    # Díky tomu nevypadá každá příšerka stejně.
    telo = random.choice([
        " |  ###  | ",
        " |  $$$  | ",
        " |  @@@  | ",
        " |  %%%  | ",
        " |  &&&  | "
    ])

    ruce = random.choice([
        "--|     |--",
        "\\\\|     |//",
        "~~|     |~~",
        "__|     |__"
    ])

    nohy = random.choice([
        "   /   \\\\",
        "   || ||",
        "   /| |\\\\",
        "   ^^ ^^"
    ])

    return ruce, telo, nohy


def nahodna_schopnost():
    # Seznam schopností slouží k tomu, aby měla každá příšerka i "charakter".
    schopnosti = [
        "umí chrlit duhu",
        "zpívá strašidelné písničky",
        "umí zmizet ve tmě",
        "miluje ponožky",
        "umí skákat až ke stropu",
        "vydává legrační zvuky",
        "sbírá sušenky",
        "umí hypnotizovat pohledem"
    ]
    return random.choice(schopnosti)


def vykresli_priserku(jmeno, hlava, oci, pusa, ruce, telo, nohy):
    # Tato funkce pouze vypíše výsledný ASCII obrázek.
    # Oddělená funkce je přehlednější než mít všechno v hlavní části programu.
    print()
    print(f"Tvá příšerka se jmenuje: {jmeno}")
    print(hlava)
    print("   .-\"\"\"-.")
    print(f"  / {oci} \\")
    print(f" |   {pusa}   |")
    print(f" {ruce}")
    print(f" {telo}")
    print(f" {nohy}")
    print()


def hlavni_menu():
    # Hlavní cyklus programu.
    # Používám while, protože chci uživateli umožnit vytvořit více příšerek,
    # dokud se sám nerozhodne skončit.
    while True:
        vypis_pomaly("Vítej v generátoru náhodných ASCII příšerek!", 1)
        vypis_pomaly("Probíhá míchání slizu, lektvarů a chaosu...", 1)
        vypis_pomaly("Vytvářím příšerku...", 1.5)

        # Tady se opravdu vytváří všechny části příšerky.
        jmeno = vytvor_jmeno()
        hlava, oci, pusa, doplnek = vytvor_oblicej()
        ruce, telo, nohy = vytvor_telo()
        schopnost = nahodna_schopnost()

        vykresli_priserku(jmeno, hlava, oci, pusa, ruce, telo, nohy)

        vypis_pomaly(f"Doplňek: {doplnek}", 0.7)
        vypis_pomaly(f"Speciální schopnost: {schopnost}", 1)

        # Uživatel rozhodne, jestli chce pokračovat.
        # lower() používám proto, aby fungovala odpověď s velkým i malým písmenem.
        dalsi = input("Chceš vytvořit další příšerku? (ano/ne): ").lower()

        if dalsi == "ano":
            # Pokud uživatel zadá ano, cyklus pokračuje a vznikne nová příšerka.
            print()
            vypis_pomaly("Dobře, chystám další příšerku...", 1)
            print()
        elif dalsi == "ne":
            # Pokud uživatel zadá ne, program se ukončí.
            vypis_pomaly("Program končí. Měj se příšerkově krásně!", 1)
            break
       else:
            # Tato větev řeší nečekaný vstup.
            # Program se díky tomu nesesype a uživatel dostane jasnou informaci.
            vypis_pomaly("Neznámá odpověď, ale beru to jako konec programu.", 1)
            break


# Tato podmínka zajistí, že se program spustí jen tehdy,
# když otevřeme právě tento soubor.
if __name__ == "__main__":
    hlavni_menu()

Jak se program spouští?

## Jak odevzdat práci:

Napište kód: Vše tvořte v souboru s koncovkou .py (např. muj_projekt.py).

Aktualizujte README: Nezapomeňte dopsat své info o projektu sem do tohoto souboru.

Uložte na GitHub, dle README Práce s GitHubem: Jakmile budete hotovi, nezapomeňte na Commit (s popisem, co jste udělali) a Push.
