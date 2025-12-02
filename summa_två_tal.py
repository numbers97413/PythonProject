lista = [2, 5, 5, 10, 15]
target = 10

antal = len(lista)
a=0
for i in range(a, antal):
    for k in range(a+1, antal):
        summa = lista[i] + lista[k]
        print(lista[i], lista[k])

        if k != i and summa == target:
            print(f'[{i}, {k}]')