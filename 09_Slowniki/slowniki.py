s = {"a": 1, 'b': 2}
s
s = {1: "a", 2: 'b'}
s

s = {[1]: "a", 2: 'b'}  # Błąd
s = {tuple([1]): "a", 2: 'b'}
s
s = {"a": 1, 'b': 2}
s
s['a']
s['c']  # Błąd
s.get('a')
s.get('c', 0)
s['c'] = 3
s
del s['b']
s

s = {"a": 1, 'b': 2, 'c': 3}

for k in s.keys():
    print(k)

for k in s.values():
    print(k)

for k in s.items():
    print(k)

for k, v in s.items():
    print(k, v)

nazwy_jednosci = {0: "", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                  9: "dziewięć"}
nazwy_jednosci.get(7, 'tej liczby nie znam')

n = 3
if n == 1:
    print('jeden')
elif n == 2:
    print('dwa')
elif n == 3:
    print('trzy')
elif n == 4:
    print('cztery')
elif n == 5:
    print('pięc')
else:
    print('tej liczby nie znam')

s2 = {'d': 4}
s|s2

s|={'e':5}
s

'a' in s

s = {1: "a", 2: 'b', "ala": [3, 4]}

from collections import defaultdict
s = defaultdict(int)
while True:
    element = input("Dodaj element:")
    if not element:
        break
    s[element] += 1
print("Dictionary: " + str(dict(s)))


ndef liczba_slownie(liczba):
    jednosci = ["", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
    nastki = ["", "jedenaście", "dwanaście", "trzynaście", "czternaście", "piętnaście", "szesnaście", "siedemnaście",
              "osiemnaście", "dziewiętnaście"]
    dziesiatki = ["", "dziesięć", "dwadzieścia", "trzydzieści", "czterdzieści", "pięćdziesiąt", "sześćdziesiąt",
                  "siedemdziesiąt", "osiemdziesiąt", "dziewięćdziesiąt"]
    setki = ["", "sto", "dwieście", "trzysta", "czterysta", "pięćset", "sześćset", "siedemset", "osiemset",
             "dziewięćset"]

    jednostka = jednosci[liczba % 10]
    dziesiatka = dziesiatki[(liczba // 10) % 10]
    nastka = nastki[liczba % 100] if 10 < liczba % 100 < 20 else ""
    setka = setki[(liczba // 100) % 10]

    wynik = f"{setka} {dziesiatka} {nastka} {jednostka}".strip()
    return wynik.capitalize()
while True:
    liczba = int(input("Podaj liczbę (1-999): "))
    if 1 <= liczba <= 999:
        break

postac_slowna = liczba_slownie(liczba)
print(f"{liczba} - {postac_slowna}")






from collections import defaultdict
s = defaultdict(int)
while True:
    element = input("Dodaj element:")
    if not element:
        break
    s[element] += 1
print("Dictionary: " + str(dict(s)))



l = []
d = {}
while True:
    napis = input("Podaj napis, a dodam go do listy: ").strip()
    if napis == "":
        break
    l.append(napis)
#l = ['Ala', 'ma', 'kota', 'kota']
for i in l:
    if d.get(i, 0) == 0:
        d[i]=1
    else:
        print (i)
        d[i] += 1
print(f"Tak się sprawy mają: {d}")
