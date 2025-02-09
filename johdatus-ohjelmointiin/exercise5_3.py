import math

while True:

    radius = float(input("Anna säde: \n"))

    area = math.pi * radius ** 2

    print(f"Ympyrän pinta-ala: {area:.2f}")

    choice = input("Haluatko jatkaa? (k/e): \n").strip().lower()

    if choice == "e":
        break
