import json

file_handle = open("countries.json", "r", encoding="UTF-8")

content = file_handle.read()
file_handle.close()

countries = json.loads(content)

print("Kaikki maat ja pääkaupungit:")
for country in countries:
    print(f"{country['country']}: {country['capital']}")

initial = input("Minkä alukirjaimen maat ja pääkaupungit tulostetaan?\n")

# Käydään läpi countries lista niin monta kertaa kuin löytyy country
for country in countries:
    # jos countryn ensimmäinen merkki == initial, printataan countryn arvo
    # ja capital arvo
    if country['country'][0] == initial:
        print(f"{country['country']}: {country['capital']}")
