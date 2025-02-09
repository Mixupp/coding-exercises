text = "The quick brown fox jumps over the lazy dog. That \
sentence contains every letter in the English alphabet. Neat!"

print(text,"\n")

text = text.replace("fox", "duck")

print(text,"\n")

input_str = input("Anna poistettava sana: \n")

if f"{input_str}" not in text:
 print("Sanaa ei löytynyt.\n")
else:
 text = text.replace(f"{input_str}", "")

print(text,"\n")

print(f"Merkkejä: {len(text)}\n")
text_list = text.split()
print(len(text_list),"\n")

text = text.replace(" ", "\n")
print(text,"\n")

user_text = input("Anna jokin lause: \n")

if len(user_text) > 20:
 print(f"{user_text[:20]} ...")

else:
 print(user_text)