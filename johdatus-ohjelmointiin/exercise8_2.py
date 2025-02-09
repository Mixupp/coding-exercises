import random
from colorama import init, Back

init(autoreset=True)

# Arvotaan numero väliltä 1-20
secret_number = random.randint(1, 20)

print("Tervetuloa arvauspeliin! Arvaa luku välillä 1-20.")

while True:
    try:
        # Kysytään käyttäjältä arvausta
        guess = int(input("Arvaa numero: "))

        if guess < secret_number:
            print(Back.BLUE + "Liian matala")
        elif guess > secret_number:
            print(Back.RED + "Liian korkea")
        else:
            print(Back.GREEN + "ONNEKSI OLKOON!")
            break  # Poistutaan silmukasta, kun oikea arvaus saatu
    except ValueError:
        print(Back.RED + "Syötä kelvollinen numero!")
