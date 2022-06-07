import random

print(random.randint(3,6))

# zakres 0.0 do 1.0
print(random.random())

# losowa wartość z listy
lista = ['a', 'b', 'c']
print(random.choice(lista))

# przemieszaj wartości w liście
random.shuffle(lista)
print(lista)

# wylosuj k wartości z listy
lista = ['red', 'blue', ';p']
print(random.sample(lista, k=1))

# wagi (1 - 10%, 2 - 10%, 3 - 80% szans na wylosowanie)
print(random.choices(lista, weights=[10, 10, 80], k=1))