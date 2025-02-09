# Kysytään käyttäjältä pistemäärä
score = int(input("Anna pistemäärä:\n"))

# Tarkistetaan, onko pistemäärä mahdollinen vertaamalla onko se alle 0 tai yli 100
if score < 0 or score > 100:
    print("Pistemäärä ei ole mahdollinen.")
else:
    # Määritellään arvosana pistemäärän mukaan
    if score <= 50:
        grade = 0
    elif score <= 60:
        grade = 1
    elif score <= 70:
        grade = 2
    elif score <= 80:
        grade = 3
    elif score <= 90:
        grade = 4
    else:  # score <= 100
        grade = 5

    # Tulostetaan arvosana muuttujasta grade
    print(f"Arvosana: {grade}")
