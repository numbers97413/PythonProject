from pathlib import Path

joltages = Path('test.txt').read_text(encoding='utf-8').splitlines()
# print(joltages)

'''
loopa genom varje element i listan och jämför med de andra, 
alternativt använd set som automatiskt tar bort dubbletter och där man kan välja största värdet snabbt

först finna de två högsta talen och sedan beräkna summan 
'''

# läs in varje element från listan
for jolt in joltages:
    lengd = len(jolt)
    #  Läs in det första talet i varje element och jämför med alla de andra
    a = 0  # starta med första talet
    for i in range(a, lengd):
        # jämför detta tal med alla andra talen i elementet
        for j in range(a, lengd):
            högst =

