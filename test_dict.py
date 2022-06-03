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