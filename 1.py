from pathlib import Path

rotationer = Path('input.txt').read_text(encoding='utf-8').splitlines()

nollor = 0
position = 50
for rotation in rotationer:
    riktning = rotation[0] # Höger eller vänster
    lengd = len(rotation)
    heltal = (rotation[1:lengd]) # Antal steg
    if lengd == 4:
        heltal = heltal[-2:]
        heltal = int(heltal)
    else:
        heltal = int(heltal)

    #print(rotation[0], heltal, rotation, lengd)

    if riktning == 'L':
        print(position, riktning, heltal, rotation)
        if position < heltal:
            position = 100 - abs(position - heltal)
        else:
            position = position - heltal

    else:
        print(position, riktning, heltal, rotation)
        position = position + heltal
        if position > 99:
            position = abs(100 - position)

    # print(position)

    if position == 0:
        nollor = nollor + 1
print(nollor)
