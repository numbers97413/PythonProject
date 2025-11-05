lista = [-2,2,5,7,10,11,15]
target = 9

antal = len(lista)
hashmap = {}
for i in range(0, antal):
    hashmap[lista[i]] = i
print(hashmap)

for i in range(antal):
    komplement = target - lista[i]
    if komplement in hashmap:
        print(komplement, lista[i])