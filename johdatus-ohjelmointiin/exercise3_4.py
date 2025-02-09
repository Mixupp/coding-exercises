# Kysytään annettu rahamäärä
money = int(input("Anna rahaa:\n"))

#  Kysytään ostoksen hinta
price = int(input("Ostosten hinta:\n"))

# Tarkistetaan ehtolauseella, riittääkö annettu rahamäärä ostoksen maksamiseen
if money >= price:
    # Jos rahat riittävät, lasketaan takaisin annettava raha
    change = money - price
    print(f"Kiitos. Annetaan takaisin {change} €")
else:
    # Jos rahat eivät riitä, pyydetään inputilla lisää rahaa muuttujaan additional_money
    additional_money = int(input("Anna lisää rahaa:\n"))

    # Lasketaan uusi rahamäärä
    total_money = money + additional_money

    # Tarkistetaan riittävätkö rahat nyt
    if total_money >= price:
        # Jos rahat riittävät, lasketaan takaisin annettava raha
        change = total_money - price
        print(f"Kiitos. Annetaan takaisin {change} €")
    else:
        # Jos rahat eivät riitä vieläkään
        print("Sinulla ei ole tarpeeksi rahaa.")
