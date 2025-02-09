import math

def show_text():
    print("Tervetuloa ohjelman käyttäjäksi!")
    print("-------------------------------")
    print("Seuraa ohjeita!")
    print()


def show_personal_info():
    print("Miikka Ruotsalainen")
    print("Rovaniemi")
    print("Taivaanrannanmaalari")

# Funktio, joka laskee saaduista tunneista, minuuteista ja sekunneista
# sekuntien lukumäärän ja palauttaa sen
def count_seconds(hours, minutes, seconds):
    second_count = 0
    for x in range(hours):
        second_count += (60 * 60)
    for x in range(minutes):
        second_count += 60
    second_count += seconds
    return second_count


def magazine_serial_check(serial):
    result = True

    if serial[4] == "-":
        short_serial = serial.replace("-","")
        if len(short_serial) == 8 and short_serial.isdigit():
            return result
    else:
        result = False
        return result

# funktio, joka saa otsikon ja listan nimiä parametreina.
# funktio tulostaa otsikon ja sen jälkeen listan nimet numeroituna.
def show_numbered_list(title, data):
    print(title)
    for index, nimi in enumerate(data, start=1):
        print(f"{index}. {nimi}")
    print()

# Seuraavissa kolmessa funktiossa lasketaan
# laatikon, pallon ja putken tilavuudet ja palautetaan
# tilavuus. Hyödynnetään math-kirjastosta saatua piin likiarvoa.
def box_volume(width, height, depth):
    volume = width * height * depth
    return volume

def ball_volume(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return round(volume,2)


def pipe_volume(radius, length):
    volume = math.pi * radius ** 2 * length
    return round(volume,2)


def file_print(file):
    file_handle = open(f"{file}", "r", encoding="UTF-8")

    content = file_handle.read()

    lines = content.split("\n")

    for line in lines:
        print(f"-> {line}")

    file_handle.close()


def file_append(message):
    file_handle = open("guestbook.txt", "a", encoding="UTF-8")

    file_handle.write(f"{message}\n")

    file_handle.close()


def file_read(file):
    file_handle = open(f"{file}", "r", encoding="UTF-8")

    content = file_handle.read()

    lines = content.split("\n")

    for line in lines:
        print(line)

    file_handle.close()


def make_list(file):
    file_handle = open(f"{file}", "r", encoding="UTF-8")

    content = file_handle.read()

    lines = content.split("\n")

    file_handle.close()

    return lines