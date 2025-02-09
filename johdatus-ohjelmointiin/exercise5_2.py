total_rainfall = 0

for month in range(1, 13):
    rainfall = float(input("Anna kuukauden sademäärä: \n"))
    total_rainfall += rainfall

average_rainfall = total_rainfall / 12

print(f"Vuoden keskiarvo on n. {average_rainfall:.1f} mm")
