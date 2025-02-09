temp = int(input("Syötä päivän lämpötila: \n"))

if 0 <= temp <= 10:
    print("KYLMÄÄ")
elif 11 <= temp <= 15:
    print("KOLEAA")
elif 16 <= temp <= 20:
    print("NORMAALI LÄMPÖTILA")
elif 21 <= temp <= 25:
    print("LÄMMINTÄ")
elif 26 <= temp <= 30:
    print("HELLETTÄ")
