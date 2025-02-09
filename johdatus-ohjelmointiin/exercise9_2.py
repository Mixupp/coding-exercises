from functions import *

hours = int(input("Anna tunnit: \n"))
minutes = int(input("Anna minuutit: \n"))
seconds = int(input("Anna sekunnit: \n"))

# Funktiota kutsutaan suoraan printin sisällä ja sen palauttama sekuntiarvo näytetään
# printattavassa tekstissä.
print(f"Yhteensä {count_seconds(hours, minutes, seconds)} sekuntia.")
