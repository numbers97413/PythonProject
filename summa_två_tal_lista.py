lista = [2,7,11,15]
target = 9

antal = len(lista)
antal_rätt_summa = 0
for i in range(0, antal):
    for k in range(i+1, antal):
        summa = lista[i] + lista[k]
        # print(i, k, lista[i], lista[k])
        if summa == target:
            print(f'[{lista[i]}, {lista[k]}]')
            antal_rätt_summa = antal_rätt_summa + 1
print(antal_rätt_summa)