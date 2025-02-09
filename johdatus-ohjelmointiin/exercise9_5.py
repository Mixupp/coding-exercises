from functions import *

while True:

    selection = input("Valitse toimenpide (1-3), 0 lopettaa ohjelman:\n")

    if selection == "1":
        width = int(input("Anna laatikon leveys:\n"))
        height = int(input("Anna laatikon korkeus:\n"))
        depth = int(input("Anna laatikon syvyys:\n"))

        print(f"Laatikon tilavuus: {box_volume(width, height, depth)} m3\n")

    elif selection == "2":
        radius = int(input("Anna pallon säde:\n"))
        print(f"Pallon tilavuus: {ball_volume(radius)} m3\n")

    elif selection == "3":
        radius = int(input("Anna putken säde:\n"))
        length = int(input("Anna putken pituus:\n"))
        print(f"Laatikon tilavuus: {pipe_volume(radius, length)} m3\n")

    elif selection == "0":
        break

print("Kiitos ohjelman käytöstä!")
