# Ohjelman alkuosa, annetaan special_price:lle alkuarvo,
# voi aloittaa myös arvosta True, jos haluat toimia käänteisellä logiikalla:
special_price = False

is_student = input("Oletko opiskelija? (k/e): \n")
travel_month = int(input("Mille kuukaudelle matka varataan? (1-12) "))

if is_student == "k" and (1 < travel_month < 6 or 8 < travel_month < 12):
    special_price = True

if special_price:
 print("Alennus myönnetty!")
else:
 print("Normaali hinta.")
