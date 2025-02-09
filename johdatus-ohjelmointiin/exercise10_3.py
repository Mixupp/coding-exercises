import random
from functions import *

# kutsutaan make_list -muuttujaa ja palautetaan lista
list = make_list("wisewords.txt")

# indeksin maksimiarvo on listan pituus - 1.
max_index = len(list) - 1
# index saa random arvon väliltä 0 ja max_index
index = random.randint(0, max_index)

# printataan päivän mietelause listasta indeksin perusteella
print(f"Päivän mietelause:\n{list[index]}")
