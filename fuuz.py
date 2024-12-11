cislo= int(input("Zadej číslo :" ))
out = ""
if not cislo % 3:
    out = "Fizz"

if not cislo % 5:
    out +="buzz"
if out:
    print(out)
else:
    print(cislo)