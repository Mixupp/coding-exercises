try:
    # Pyydetään käyttäjältä kaksi numeroa
    first_number = float(input("Anna ensimmäinen numero: \n"))
    second_number = float(input("Anna toinen numero: \n"))

    # Suoritetaan jakolasku
    result = first_number / second_number
    print(f"Jakolaskun tulos: {result}")

except ValueError:
    print("Virheellinen muoto.")
except ZeroDivisionError:
    print("Nollalla ei saa jakaa.")
