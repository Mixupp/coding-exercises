basket = ["omena", "banaani", "kirsikka", "porkkana", "peruna", "tomaatti", "kaali"]

user_input = input("Syötä sana tai numero: ")

# Jos syötetään numero
if user_input.isnumeric():
    index = int(user_input) - 1
    if 0 <= index < len(basket):
        for i in range(len(basket)):
            if i == index:
                continue
            print(basket[i])
    else:
        print("Numero on virheellinen!")
# Jos syötetään sana
else:
    user_word = user_input.lower()
    if user_word in basket:
        for item in basket:
            if item == user_word:
                continue
            print(item)
    else:
        print("Sanaa ei löytynyt.")
