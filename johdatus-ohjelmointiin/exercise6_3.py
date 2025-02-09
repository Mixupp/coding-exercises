import statistics

num_students = int(input("Syötä oppilaiden lukumäärä: "))

grades = []

for i in range(num_students):
    grade = float(input("Anna opiskelijan arvosana: \n"))
    grades.append(grade)

average = sum(grades) / len(grades)

if 0 <= average < 1:
    evaluation = "Huono tulos"
elif 1 <= average < 2:
    evaluation = "Heikko tulos"
elif 2 <= average < 3:
    evaluation = "Tyydyttävä tulos"
elif 3 <= average < 4:
    evaluation = "Hyvä tulos"
else:
    evaluation = "Kiitettävä tulos"

median = statistics.median(grades)

mode = statistics.mode(grades)

print(f"\nKeskiarvo: {average:.1f}")
print(f"Sanallinen arvio: {evaluation}")

print(f"Mediaani: {median}")
print(f"Moodi: {mode}")
