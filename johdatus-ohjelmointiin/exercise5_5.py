months = ("Tammikuu", "Helmikuu", "Maaliskuu", "Huhtikuu", "Toukokuu", "Kesäkuu",
          "Heinäkuu", "Elokuu", "Syyskuu", "Lokakuu", "Marraskuu", "Joulukuu")

month_number = int(input("Anna kuukauden numero: \n"))

if 1 <= month_number <= 12:
    print(f"{months[month_number - 1]}")

