text = input("Ange heltal: ")
lista = text.split()

for i in range(0, len(lista)):
    lista[i] = int(lista[i])

print("Här listan:", lista)
print("Första elementet i listan:", lista[0])
omvänt = []
for i in range(len(lista)-1, -1, -1):
    omvänt[i] = lista[i]

print("Omvänd ordning: ", omvänt)