import os

# scieżka do aplikacji
print(os.getcwd())

# listowanie katalogów i plików
print(os.listdir())

# dowolnego katalogu
sciezka_folderu = '/home/lubuntu'
print(os.listdir(sciezka_folderu))

# uruchom linuxową komendę
os.system('ls -la')

os.system('echo "testowy wpis" > test.txt')
# os.system('code test.txt')
os.system('rm test.txt')
os.system('ls -la')

# zmienne środowiskowe
# print(os.environ) # wszystkie zmienne
print(os.environ['SHELL']) # konkretna zmienna
print(os.environ['USER'])
print(os.environ['HOME'])
print(os.environ['PWD'])

# nowa zmienna środowiskowa
os.environ['nowa'] = '1'
print(os.environ['nowa'])

# nazwy wszystkich zmiennych
# print(list(os.environ))

# zmień nazwę pliku jeżeli istnieje
os.system('echo "test" > tf3.txt')
os.system('ls -la')
os.replace('tf3.txt', 'tf.txt')
os.system('ls -la')

# zmiana nazwy jeżeli istnieje
os.rename('tf.txt', 'tf3.txt')
os.system('ls -la')

# łączenie ścieżek
sciezka_projektu = '/home/user'
nazwa_folderu = 'folder'
nazwa_pliku = 'program.py'

print(os.path.join(sciezka_projektu, nazwa_folderu, nazwa_pliku))

sciezka_folderu = os.getcwd()

print(os.path.join(sciezka_folderu, nazwa_pliku))

# separator właściwy dla WIN i Linuxa
print(os.sep)

# iterowanie po drzewie katalogów
folder_path = os.getcwd()

# print('1 zmienna - ścieżka folderu:')
# for folder, folders_in, files_in in os.walk(folder_path, topdown=True):
#     print('-', folder)

# print('2 zmienna - lista folderów w tym folderze:')
# for folder, folders_in, files_in in os.walk(folder_path, topdown=True):
#     if folders_in != []:
#         print('-', folders_in)

# print('3 zmienna - lista plików w tym folderze:')
# for folder, folders_in, files_in in os.walk(folder_path, topdown=True):
#     if files_in != []:
#         print('-', files_in)

# iteracja po folderach i plikach jako obiekcie ze swoimi metodami
with os.scandir(folder_path) as it:
    for entry in it:
        if entry.is_file(): # jeżeli to plik
            pass
        if entry.is_dir(): # jeżeli do folder
            pass
        print(entry.name) # nazwa pliku
        print(entry.path) # ścieżka pliku
        print('----------------------')
