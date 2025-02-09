original_price = float(input("Anna hinta ilman alv (€): "))
increase = 1.25

new_price = (original_price * increase)
new_price = round(new_price,2)

print(f"Hinta alv:n kanssa: {new_price} €")