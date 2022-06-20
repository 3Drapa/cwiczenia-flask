plik = 'data/plik_tekstowy.txt'
# tekst = open(plik).read()
# print(tekst)

# tekst_linie = open(plik).readlines()
# print(tekst_linie)

# odczyt pliku
mode = 'r+'
with open(plik, mode) as f:
    text = f.read() # f.readlines()

# zapis do pliku
plik2 = 'data/plik_tekstowy_02.txt'
mode = 'w+'
string = 'Testowy zapis do pliku'
with open(plik2, mode) as f:
    f.write(string)

# zapis do pliku listy stringów
lista_stringow = [
    'aaaaaa\n',
    'bbbbbb\n',
    'cccccc\n',
]
with open(plik2, mode) as f:
    f.writelines(lista_stringow)