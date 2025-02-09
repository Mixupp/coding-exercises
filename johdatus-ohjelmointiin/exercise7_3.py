shopcart = [
    {"name": "Lokki-valaisin", "price": 349.9},
    {"name": "Stockholm-matto", "price": 129.9},
    {"name": "Malm-lipasto", "price": 49.9},
    {"name": "Vienna-divaanisohva", "price": 799.9},
    {"name": "Ritz-nojatuoli", "price": 369.9}
]

total = 0

print("Kuitti ostoksista: ")
for item in shopcart:
    print(f"- {item['name']} : {item['price']} €")
    total += item['price']

without_vat = total / 1.24
vat = total - without_vat

print(f"\nYhteensä: {total} €")
print(f"ALV (24%): {vat:.2f} €")
print("Tervetuloa uudelleen!")
