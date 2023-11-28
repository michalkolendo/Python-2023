range(10)

list(range(10))

(x * x for x in range(10))

[x for x in range(10)]

[x * x for x in range(10)]

[x for x in range(10) if x % 2 == 0]

[x * x for x in range(10) if x % 2 == 0]

[(x, y, x * y) for x in range(3) for y in range(4)]

{x for x in range(10)}

{x // 2 for x in range(10)}

{x: x * x for x in range(10) if x % 2 == 0}

# Stworzyć list comprehension na podstawie jednej listy z liczbami całkowitymi, ale z elementami o 6 większymi

[x + 6 for x in range(10)]

# Stworzyć list comprehension tupli składających się z w/w liczb całkowitych i ich reprezentacji jako napis


t = [(x, str(x)) for x in range(15)]
print(t)

# biorąc słownik {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110} stworzyć list comprehension nazw pojazdów cięższych niż 5000
# Nazwy podać dużymi literami (uppercase) `

dane = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
t = [(x.upper(), dane(x)) for x in dane if dane(x) > 5000]
print(t)