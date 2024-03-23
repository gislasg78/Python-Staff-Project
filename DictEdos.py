# Dictionaries in Python with federal entities of Mexico.

federal_entities_MX =  {1 : "Aguascalientes", 2 : "Baja California", 3 : "Baja California Sur", 4 : "Campeche",
                        5 : "Chiapas", 6 : "Chihuahua", 7 : "Ciudad de México", 8 : "Coahuila", 9 : "Colima",
                        10 : "Durango", 11 : "Estado de México", 12 : "Guanajuato", 13 : "Guerrero", 14 : "Hidalgo",
                        15 : "Jalisco", 16 : "Michoacán", 17 : "Morelos", 18 : "Nayarit", 19 : "Nuevo León",
                        20 : "Oaxaca", 21 : "Puebla", 22 : "Querétaro", 23 : "Quintana Roo", 24 : "San Luis Potosí",
                        25 : "Sinaloa", 26 : "Sonora", 27 : "Tabasco", 28 : "Tamaulipas", 29 : "Tlaxcala",
                        30 : "Veracruz", 31 : "Yucatán", 32 : "Zacatecas"}

print("Dictionary of federal entities.")
print(federal_entities_MX)

print()
print("Keys to the federal entities.")
print(f"{federal_entities_MX.keys()}.")

print()
print("Values of the federal entities.")
print(f"{federal_entities_MX.values()}.")

print()
print("List of Federal Entities of the Mexican Republic.")
for item in federal_entities_MX:
    print(f"{item} : {federal_entities_MX[item]}.")

print()
print("Dictionary of Mexican Republic Federal Entities.")
for row in federal_entities_MX.items():
    print(f"{row}.")
