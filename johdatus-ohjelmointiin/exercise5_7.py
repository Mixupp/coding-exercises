products = [
    "PHILIPS_Vedenkeitin_HD4646_2020_09_21_C_1",
    "KENWOOD_Yleiskone_KVL8300S_2015_09_22_C_3",
    "BOSCH_Tehosekoitin_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Mikroaaltouuni_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Pakastin_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Jääkaappi_ERF4114AOW_2017_11_07_C_2"
]


categories = ["Muut", "Pienlaitteet", "Kylmälaitteet", "Sekoittimet"]

for product in products:

    parts = product.split("_")

    manufacturer = parts[0]
    name = parts[1]
    model = parts[2]
    year = parts[3]
    month = parts[4]
    day = parts[5]
    category_num = int(parts[7])
    category = categories[category_num]

    print(f"Valmistaja: {manufacturer}")
    print(f"Nimi ja malli: {name} ({model})")
    print(f"Kategoria: {category}")
    print(f"Lisäyspäivämäärä: {day}.{month}.{year}")
    print("")
