# Kysytään käyttäjältä minuutit
minutes = int(input("Anna minuutit: "))

# Lasketaan tunnit ja jäljelle jäävät minuutit
hours = minutes // 60
minutes_leftover = minutes % 60

# Tulostetaan tulos
print(f"{hours}h {minutes_leftover}min")
