print("Cesta autom")
distance = float(input("Vzdialenosť: "))
consuption = float(input("Spotreba: ")) 
travelers = float(input("Počet cestujúcich: "))
cost = float(input("Cena nafty/benzínu:"))

while distance > 0:
    consuption_per_1 = consuption / 100
    print(f"Cesta výjde {((consuption_per_1*distance)*cost)/travelers:.1f}€ na jedného.")
    distance = float(input("Vzdialenosť: "))
    onsuption = float(input("Spotreba: ")) 
    travelers = float(input("Počet cestujúcich: "))
    cost = float(input("Cena nafty/benzínu:"))