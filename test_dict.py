slownik = {
    'klucz': 'wartość',
    'model': 'Mustang',
    'year': 1964,
}

print(len(slownik)) # 3

slownik['a'] = 1
slownik['b'] = [1, 2]
slownik['c'] = True

print(slownik)

slownik['klucz'] = 'WARTOŚĆ' #zmiana wartości klucza

print(slownik['klucz'])

# usunięcie klucza i wartości
del slownik['a']
del slownik['b']
del slownik['c']

print(slownik)

# dostęp do słownika po kluczach (V1)
wartosc = slownik.get('klucz', 'nima')
print(wartosc)

wartosc2 = slownik.get('blabla', 'nima') # wartosc2 przyjmie 2 argument jeżeli klucz nie istnieje
print(wartosc2)
print(slownik)

# dostęp do słownika po kluczach (V2)
wartosc = slownik['klucz']
print(wartosc)

# zmiana wartości klucza
slownik['klucz'] = 'abc'
print(slownik)

# klucze
print(slownik.keys())

for k in slownik.keys():
    print(k)

# wartości
print(slownik.values())

for v in slownik.values():
    print(v)

# klucze i wartości
print(slownik.items())

for i in slownik.items():
    print(i)

for k, v in slownik.items():
    print("{} - {}".format(k, v))

# żeby działac na indeksach trzeba zamienić słownik w listę:
list(slownik.items())

print(list(slownik.items())[1]) # klucz i wartość indeksu 1
print(list(slownik.items())[1][1]) # wartość indeksu 1

# kopia slownika
slownik2 = slownik.copy()
print(slownik2)

# pusty słownik
slownik.clear()
# albo
slownik = {}

print(slownik)
print(slownik2)

# dodawanie tych samych wartości do kluczy
lista_kluczy = ['a', 'b', 'c']
wartosc = True
d = slownik.fromkeys(lista_kluczy, wartosc)
print(d)

slownik = {
    "klucz":"wartosc",
    "model":"Mustang",
    "year":1964,
}

slownik['xd'] = 134
print(slownik)

# pobiera i usuwa ze słownika podany klucz
klucz = 'year'
wartosc = slownik.pop(klucz)

print(slownik)
print(wartosc)

# pobiera i usuwa ostatnią parę (klucz - wartość)
slownik['nowy_klucz'] = 2314312412

print(slownik)
klucz_wartosc = slownik.popitem()
print(slownik)
print(klucz_wartosc)

# dodawanie słownika do słownika lub więcej par (klucz, wartość)
slownik_1 = {'x':67, 'y':87}
slownik_2 = {'z':48, 'f':44}

# Sposób 1
slownik_1.update(slownik_2)
print(slownik_1)

# Sposób 2
slownik_1.update(a=1, b=2, c=3)
print(slownik_1)

# Włóż do słownika parę klucz-wartość, a jeżeli klucz istnieje, to zwóć jego wartość
slownik_1 = {'z':48, 'f':44}
klucz = 'z'
wartosc_domyslna = 'xD'

# klucz jest w słowniku:
rezultat = slownik_1.setdefault(klucz, wartosc_domyslna)

print("Rezultat: ", rezultat)
print("Słownik: ", slownik_1)

# klucza nie ma w słowniku
del slownik_1['z']

rezultat = slownik_1.setdefault(klucz, wartosc_domyslna)

print("Rezultat2: ", rezultat)
print("Słownik: ", slownik_1)