temperature = float(input("Anna tämänhetkinen ulkolämpötila (°C): "))
humidity = float(input("Anna tämänhetkinen kosteusprosentti (%): "))

freezing = False
heatwave = False
raining = False
hailstorm = False

if temperature < 0:
    freezing = True

if humidity > 80:
    if temperature <= -20:
        hailstorm = True
    else:
        raining = True

if temperature > 20:
    heatwave = True

print(f"Lämpötila: {temperature}°C")

if freezing:
    print("Pakkasta.")
if hailstorm:
    print("Sataa rakeita!")
if raining:
    print("Sataa.")
if heatwave:
    print("Helleaalto!")
if raining and heatwave:
    print("Kosteaa ja tukalaa.")
