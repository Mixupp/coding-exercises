import random

rnd_number = random.randint(1,10)
side1 = random.randint(2,10)
side2 = random.randint(2,10)
area = side1 * side2

print(f"Arvottu luku: {rnd_number}")
print(f"Arvottu 1. sivu: {side1}")
print(f"Arvottu 2. sivu: {side2}")
print(f"Arvotuista sivuista laskettu pinta-ala: {area}")
