import math

side1 = float(input("Anna kolmion ensimmäinen kateetti: \n"))
side2 = float(input("Anna kolmion toinen kateetti: \n"))

side3 = round(math.sqrt((side1 ** 2) + (side2 ** 2)),2)

print(f"Hypotenuusan pituus: {side3} m")

