import datetime
from colorama import init, Fore

# Haetaan nykyinen vuosi
current_year = datetime.datetime.now().year

# Lista syntymävuosille
birth_years = []

# Kysytään käyttäjältä syntymävuodet ja tallennetaan ne listaan
for i in range(5):
    birth_year = input(f"Anna henkilön {i + 1} syntymävuosi: ")
    try:
        birth_year = int(birth_year)
        birth_years.append(birth_year)
    except ValueError:
        print(Fore.RED + "Virheellinen syöte! Anna vuosi numerona.")

# Käydään syntymävuodet läpi ja tarkistetaan iän oikeellisuus
for birth_year in birth_years:
    age = current_year - birth_year

    if 0 <= age <= 125:
        print(Fore.GREEN + f"{age} vuotta, Ikä OK!.")
    else:
        print(Fore.RED + "Ikä ei ole oikeassa muodossa.")

# Tulosta lopuksi valmis-viesti
print("Valmis!")
