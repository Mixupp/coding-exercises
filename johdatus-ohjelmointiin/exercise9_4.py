from functions import *

string = input("Syötä tapahtuman osallistujat pilkulla eroteltuna:\n")

people = string.split(",")

people = [p.strip() for p in people]

show_numbered_list("Ilmoittautumisjärjestys:", people)

people.sort()

show_numbered_list("Aakkosjärjestys etunimen perusteella:", people)


people = [" ".join(reversed(p.split(" "))) for p in people]
people.sort()

show_numbered_list("Aakkosjärjestys sukunimen perusteella:", people)





