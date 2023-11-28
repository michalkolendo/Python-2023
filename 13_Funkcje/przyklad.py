def dodaj_2(x):
    wynik = x + 2
    return wynik


dodaj_2(5)
n = dodaj_2(5)
print(n)


def is_odd(x):
    print("*" * x)
    return (x % 2) == 1


is_odd(25)
is_odd(8)


def slownie(n):
    jednosci = {0: "zero", 1: "jeden", 2: "dwa", 3: "trzy", 4: "cztery", 5: "pięć", 6: "sześć", 7: "siedem", 8: "osiem",
                9: "dziewięć"}
    return jednosci[n]


slownie(6)


def dodaj_2_slownie(n):
    wynik = dodaj_2(n)
    return slownie(wynik)


dodaj_2_slownie(4)


def give_a_and_b():
    a = 1
    b = 2
    return a, b


a, b = give_a_and_b()
a
b
t = give_a_and_b()
t

int("10")
int("10", base=2)

int("10", base=16)


def wiecej(x, ile_razy=2):
    return ile_razy * x


wiecej(100)
wiecej(100, ile_razy=10)


def choinka(poziom, separator=" ", znak="*"):
    S = separator
    G = znak
    for i in range(1, poziom + 1):
        print(S * (poziom - i) + G * (2 * i - 1))
    print(S * (poziom - 1) + G)
    print(S * (poziom - 2) + G * 3)


choinka(5)
choinka(znak='#', poziom=6)

#stworzyc słownik { 'first': funkcja1, 'second': funkcja2 }, wczytać przez input klucz, wywołać funkcję

def dodaj3(x):
    wynik = x + 3
    return wynik

def dodaj4(x):
    wynik = x + 3
    return wynik

slownik =  { 'first': dodaj3, 'second': dodaj4 }

t = input('Podaj klucz')
funkcja = slownik[t]
print(funkcja(4))


# stworzyc funckcję alphabet_range działająca jak range ale dla liter (z trzema parametrami - start, end, step)
#przykład: alphabet_range('E') -> ['A', 'B', 'C', 'D'] - albo jeszcze lepiej generator
# użyć
# ord - podaje kod calkowity danego znaku
# chr - podaje znak odpowiadający danemu kodowi całkowitemu

def alphabet_range(start = 'a',end = 'e',step = 0):
    st = ord(start)
    en = ord(end)
    stp = step
    result = ""
    for i in range(st,en+1, stp):
        result += chr(i)
    return result

print(alphabet_range("a","l",2))