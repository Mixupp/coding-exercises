# Pyydetään käyttäjältä viikon työtunnit ja muunnetaan ne liukuluvuksi (float), jotta voidaan käsitellä desimaaleja
weekly_hours = float(input("Syötä viikon työtunnit: \n"))

# Pyydetään käyttäjältä tuntipalkka ja muunnetaan se myös liukuluvuksi
hourly_rate = float(input("Syötä tuntipalkkasi: \n"))

# Tarkistetaan, onko työtunteja enemmän kuin 40.0. Jos kyllä, lasketaan ylityökorvaus.
if weekly_hours > 40.0:

    # Lasketaan ylitunnit vähentämällä 40.0 viikon työtunneista. Jos työtunnit ovat alle 40, ylitunnit ovat negatiivinen arvo.
    # Huomio: Tämä ei vielä vaikuta ohjelman toimintaan ennen kuin tarkistetaan, onko tunnit yli 40.
    overtime_hours = weekly_hours - 40.0

    # Perustyöajan palkka lasketaan 40 tunnin mukaan
    fulltime_pay = 40.0 * hourly_rate

    # Ylityökorvaus lasketaan 1.5-kertaisena peruspalkkaan nähden ja kerrotaan ylitunneilla
    overtime_pay = hourly_rate * 1.5 * overtime_hours

    # Kokonaispalkka on perustyöajan palkka + ylityökorvaus
    total_salary = fulltime_pay + overtime_pay
else:
    # Jos työtunteja on 40 tai vähemmän, kokonaispalkka lasketaan suoraan peruspalkan mukaan
    total_salary = weekly_hours * hourly_rate

# Tulostetaan viikon palkka, pyöristettynä kahden desimaalin tarkkuuteen
print(f"Viikon ansiosi ovat: {round(total_salary, 2)}€")


