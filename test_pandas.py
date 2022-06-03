import pandas as pd

df = pd.read_csv('data/plik.csv')

# print(df.head(2))

# wybranie tylko 2 kolumn
df2 = df.loc[:, ['name', 'win']]
# print(df2.head(10))

# zapis nowego DataFrame do pliku
df2.to_csv('data/nowy_plik.csv', index=False)

# sortowanie wartości od największej liczby wygranych do najmniejszej
df.sort_values(by='win', inplace=True, ascending=False)
# print(df.head(10))

# wyświetlanie jedynie tych rzędów, które mają co najmniej 25 wygranych
for i, row in df.iterrows():
    if row['win'] >= 25:
        print('{} {}'.format(row['win'], row['name']))

