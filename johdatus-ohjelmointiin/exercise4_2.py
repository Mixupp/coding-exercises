
def check_palindrome(input_str):
    reversed_str = input_str[::-1]
    return input_str == reversed_str

def main():
    user_input = input("Anna jokin teksti: ")

    # Tarkistetaan, onko syöte tyhjä ennen kuin jatketaan
    if user_input == "":
        print("Antamasi teksti on tyhjä.")
        return

    # Tulos tallennetaan muuttujaan palindrome_result
    palindrome_result = check_palindrome(user_input)

    print(f"{user_input[::-1]}")

    # Tarkistetaan if-elsellä onko tulos tosi vai epätosi ja tulostetaan.
    if palindrome_result:
        print("Palindromi: KYLLÄ")
    else:
        print("Palindromi: EI")

if __name__ == "__main__":
    main()
