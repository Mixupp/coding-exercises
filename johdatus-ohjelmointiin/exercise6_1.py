max_number = 0

for x in range(5):
    while True:
        try:
            number = int(input("Anna numero: "))
            if number > 0:
                break
            else:
                print("Luku ei ole positiivinen. Yritä uudelleen.")
        except ValueError:
            print("Virheellinen syöte. Syötä positiivinen kokonaisluku.")

    if number > max_number:
        max_number = number

print(f"Suurin käyttäjän luku: {max_number}")
