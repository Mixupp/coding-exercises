country_distance = float(input("Matka-ajon kilometrit: "))
city_distance = float(input("Kaupunkiajon kilometrit: "))

consumption_city = float(7.5 / 100)
consumption_country = float(5.1 / 100)

consumption_total = ((country_distance * consumption_country) +
                     (city_distance * consumption_city))

print(f"Kulutus: {consumption_total:.2f} l")
