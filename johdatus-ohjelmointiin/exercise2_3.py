import math

salary = float(input("Anna kuukausipalkkasi: "))
tax_percentage =  float(input("Anna veroprosenttisi: "))

tax = round((tax_percentage / 100) * salary,2)
salary_left = round(salary - tax,2)

print(f"Käteenjäävä osuus: {salary_left} €")
print(f"Verot: {tax} €")



