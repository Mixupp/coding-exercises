while True:

    number = int(input("Syötä luku (1-10), jonka kertotaulun haluat nähdä (0 lopettaa): "))

    if number == 0:
        break

    if number < 1 or number > 10:
        print("Vääränlainen luku.")
        continue

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

    print()