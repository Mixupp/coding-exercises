import json
import urllib.request

# Ladataan säätiedot API:sta
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

# alustetaan muuttujat tuulen nopeuksien seurantaa varten
max_wind = 0
# alustetaan äärettömäksi, jotta saadaan min wind päivitettyä ensimmäisellä kierroksella
min_wind = float('inf')
max_location = ""
min_location = ""

# Käydään säätiedot läpi
for data in weather:
    wind_speed = data["wind"]
    location = data["location"]

    # Etsitään suurin ja pienin tuulen nopeus
    if wind_speed > max_wind:
        max_wind = wind_speed
        max_location = location
    if wind_speed < min_wind:
        min_wind = wind_speed
        min_location = location

# Tulostetaan suurin ja pienin tuulen nopeus
print(f"Tänään eniten tuulee sijainnissa: {max_location}, {max_wind} m/s")
print(f"Tänään vähiten tuulee sijainnissa: {min_location}, {min_wind} m/s")
