from datetime import datetime

# Määritellään tiedot omiin muuttujiin
today = datetime.now()
date_string = today.strftime("%d.%m.%Y")
name = "Matti Meikäläinen"
birth_year = 1984
balance = 345

# Yhdistetään tiedot ja luodaan uusi muuttuja tulostamista varten
print_out = f"{name} ({birth_year}), saldo: {balance} €, päivitetty {date_string}."

# Tulostetaan lopputulos konsoliin
print(print_out)

