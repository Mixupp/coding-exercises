cents = int(input("Anna 1-100 senttiä: \n"))


# Tässä lasketaan kokonaislukujaolla paljonko 50snt kolikoita mahtuu annettuun
# senttimäärään. Sitten cents muuttujaan päivitetään jakojäännöksen sentit.
coins_50 = cents // 50
cents = cents % 50

# Seuraavaksi lasketaan montako 20snt kolikkoa mahtuu jäljelle
# jäävään senttimäärään

coins_20 = cents // 20
cents = cents % 20

# Ja 10snt kolikoita taas jäljelle jäävään jne.
coins_10 = cents // 10
cents = cents % 10

coins_5 = cents // 5
cents = cents % 5

coins_2 = cents // 2
cents = cents % 2

# Lopussa on vain yksittäisiä senttejä joten ei tarvita
# kuin muuttujaan sijoitus
coins_1 = cents

print(f"50snt kolikoita {coins_50} kpl")
print(f"20snt kolikoita {coins_20} kpl")
print(f"10snt kolikoita {coins_10} kpl")
print(f"5snt kolikoita {coins_5} kpl")
print(f"2snt kolikoita {coins_2} kpl")
print(f"1snt kolikoita {coins_1} kpl")
