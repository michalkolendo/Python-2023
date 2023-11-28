l = [3, 5, 6, 7]
l

l[1]
l[0]
len(l)
l[0:2]
l[1:2]
l[1:]
l[:2]
l[-1]
l[1:-1]
l[-4]
l[1:-1] + l[0:-1]

for i in range(len(l)):
    print(l[i])

for i in l:
    print(i)

l * 4

l.index('3')  # Błąd
l.index(3)

l[1] = 17
l
del l[3]
l
l.append(19)
l
l += ['A', 'B']
l
l.pop()
l

" - ".join(["Ala", "ma", "kota"])
"".join(["Ala", "ma", "kota"])
" ".join(["Ala", "ma", "kota"])
s2 = '.|.'
s2.join(["Ala", "ma", "kota"])

'.' in s2

lista = []
parzysta = 0
while True:
    element = input("Dodaj element:")
    if not element:
        break
    lista.append(element)
lista.sort(reverse=True)
for a in lista:
    if (int(a) % 2 == 0):
        parzysta = a
        break

print(parzysta)







i = 0
wysokosc = int(input("Wysokosc Choinki:"))
while (i < wysokosc):
    choinka= "*" * i
    print(choinka.center(wysokosc, " "))
    i += 1