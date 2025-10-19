x = input("Tal: ")
lista = x.split()
print(lista)
for i in range(0, len(lista)):
    lista[i] = int(lista[i])
print(lista)
a = 0 # Elementet som skal testat mot de andra elementen
b = 1 # De andra
dubbletter = 0
for i in range(a, len(lista)):
    b = i + 1
    for n in range(b, len(lista)):
        print(i, n, lista[i], lista[n], dubbletter)
        if lista[i] == lista[n]:
            dubbletter = dubbletter + 1
print(dubbletter)