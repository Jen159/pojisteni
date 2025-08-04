# import potřebných knihoven
import os

# vlastní výjimka pro záporný věk
class NegativeAgeError(Exception):
    pass


# třída reprezentující jednoho pojištěného
class Pojisteni:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}, věk: {self.vek}, tel: {self.telefon}"


# třída pro správu seznamu všech pojištěných
class SeznamPojistenych:
    def __init__(self):
        self.seznam = []  # seznam objektů třídy Pojisteni

    def pridej_pojisteneho(self, pojisteny):
        # přidá nového pojištěného do seznamu
        self.seznam.append(pojisteny)

    def vypis_seznam(self):
        # vypíše všechny pojištěné v seznamu
        if not self.seznam:
            print("❌ Seznam pojištěných je prázdný.")
        else:
            print("\n📋 Seznam pojištěných:")
            for pojisteny in self.seznam:
                print(pojisteny)
            print()

    def vyhledat_pojisteneho(self, jmeno, prijmeni):
        # hledá pojištěného podle jména a příjmení (ignoruje velikost písmen)
        for pojisteny in self.seznam:
            if pojisteny.jmeno.lower() == jmeno.lower() and pojisteny.prijmeni.lower() == prijmeni.lower():
                return pojisteny
        return None

    def odeber_pojisteneho(self, jmeno, prijmeni):
        # smaže pojištěného ze seznamu, pokud existuje
        pojisteny = self.vyhledat_pojisteneho(jmeno, prijmeni)
        if pojisteny:
            self.seznam.remove(pojisteny)
            return True
        return False


# funkce pro bezpečné zadání věku s validací a vlastní výjimkou
def zadat_vek():
    while True:
        try:
            vek = int(input("Zadejte věk: "))
            if vek < 0:
                raise NegativeAgeError("⚠️ Věk nesmí být záporný.")
            return vek
        except ValueError:
            print("⚠️ Neplatný věk. Zadejte prosím číslo.")
        except NegativeAgeError as e:
            print(e)


# funkce pro zadání telefonního čísla pouze jako číslic
def zadat_telefon():
    telefon = input("Zadejte telefonní číslo: ").strip()
    while not telefon.isdigit():
        print("⚠️ Telefonní číslo musí obsahovat pouze číslice.")
        telefon = input("Zadejte telefonní číslo: ").strip()
    return telefon


# hlavní menu aplikace
def main():
    seznam = SeznamPojistenych()  # vytvoří nový prázdný seznam pojištěných

    while True:
        print("\n🛡️  Evidence pojištěných")
        print("--------------------------")
        print("1 - Přidat pojištěného")
        print("2 - Zobrazit seznam pojištěných")
        print("3 - Vyhledat pojištěného")
        print("4 - Upravit pojištěného")     
        print("5 - Smazat pojištěného")
        print("6 - Ukončit program")

        try:
            volba = int(input("Zadejte číslo volby (1–6): "))
        except ValueError:
            print("⚠️ Neplatný vstup. Zadejte číslo od 1 do 6.")
            continue

        if volba == 1:
            # přidání nového pojištěného
            jmeno = input("Zadejte jméno: ").strip()
            prijmeni = input("Zadejte příjmení: ").strip()
            vek = zadat_vek()
            telefon = zadat_telefon()

            pojisteny = Pojisteni(jmeno, prijmeni, vek, telefon)
            seznam.pridej_pojisteneho(pojisteny)
            print("✅ Pojištěný byl úspěšně přidán.")

        elif volba == 2:
            # výpis všech pojištěných
            seznam.vypis_seznam()

        elif volba == 3:
            # vyhledání konkrétního pojištěného
            jmeno = input("Zadejte jméno: ").strip()
            prijmeni = input("Zadejte příjmení: ").strip()
            nalezeny = seznam.vyhledat_pojisteneho(jmeno, prijmeni)

            if nalezeny:
                print("🔍 Nalezený pojištěný:")
                print(nalezeny)
            else:
                print("❌ Pojištěný nebyl nalezen.")

        elif volba == 4:
            # úprava pojištěného (věk a telefon)
            jmeno = input("Zadejte jméno pojištěného k úpravě: ").strip()
            prijmeni = input("Zadejte příjmení: ").strip()
            pojisteny = seznam.vyhledat_pojisteneho(jmeno, prijmeni)

            if pojisteny:
                print(f"🔧 Úprava údajů pro: {pojisteny}")
                novy_vek = zadat_vek()
                novy_telefon = zadat_telefon()
                pojisteny.vek = novy_vek
                pojisteny.telefon = novy_telefon
                print("✅ Údaje byly úspěšně upraveny.")
            else:
                print("❌ Pojištěný nebyl nalezen.")

        elif volba == 5:
            # smazání pojištěného
            jmeno = input("Zadejte jméno pojištěného ke smazání: ").strip()
            prijmeni = input("Zadejte příjmení: ").strip()
            uspesne = seznam.odeber_pojisteneho(jmeno, prijmeni)

            if uspesne:
                print("🗑️ Pojištěný byl úspěšně smazán.")
            else:
                print("❌ Pojištěný nebyl nalezen.")

        elif volba == 6:
            # ukončení programu
            print("👋 Ukončuji program. Měj se pěkně!")
            break

        else:
            print("⚠️ Neplatná volba. Zadejte číslo od 1 do 6.")
            
        
# spuštění aplikace
if __name__ == '__main__':
    main()
