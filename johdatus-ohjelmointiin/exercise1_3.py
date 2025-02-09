
# Kysytään käyttäjältä matkan pituus ja tallennetaan muuttujaan distance ja
# muunnetaan muotoon float
distance = float(input("Anna matkan pituus (km): "))

# Lasketaan muuttujaan consumption yhden kilometrin kulutus ja muutetaan muotoon float
consumption = float(6.5 / 100)

# Lasketaan kokonaiskulutus annetulle matkalle ja pyöristetään yhdeb desimaalin tarkkuuteen
total_consumption = round(distance * consumption,1)

# Tulostetaan kokonaiskulutus matkalle litroina
print(f"Kulutus: {total_consumption} l")