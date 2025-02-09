import math

side1 = float(input("Anna särmiön ensimmäisen sivun pituus: \n"))
side2 = float(input("Anna särmiön toisen sivun pituus: \n"))
side3 = float(input("Anna särmiön kolmannen sivun pituus: \n"))

volume_box = round(side1 * side2 * side3,2)

print(f"Särmiön tilavuus: {volume_box} m3")

radius_ball = float(input("Anna pallon säde: \n"))

volume_ball = round(((4/3) * math.pi * (radius_ball ** 3)),2)

print(f"Pallon tilavuus: {volume_ball} m3")

