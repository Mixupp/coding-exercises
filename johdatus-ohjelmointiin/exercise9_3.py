from functions import *

input_issn = input("Anna ISSN-sarjanumero: \n")

result = magazine_serial_check(input_issn)

if result:
    print(f"Oikea ISSN.")
else:
    print("Väärä ISSN.")