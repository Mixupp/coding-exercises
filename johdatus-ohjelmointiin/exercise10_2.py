from functions import *

choice = input("Haluatko lukea vai kirjoittaa vieraskirjaan? (l/k)\n")

if choice == "k":
    message = input("Kirjoita uusi viesti:\n")
    file_append(message)
elif choice == "l":
    file_read("guestbook.txt")