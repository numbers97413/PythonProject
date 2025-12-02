from pathlib import Path

rotationer = Path('input.txt').read_text(encoding='utf-8').splitlines()

nollor = 0
position = 50
for rotation in rotationer:
    riktning = rotation[0] # Höger eller vänster
    lengd = len(rotation)
    heltal = int(rotation[1:lengd]) # Antal steg

    # print(rotation[0], heltal, rotation)

    if riktning == 'L':
        position = position - heltal

    else:
        position = position + heltal

    print(riktning, position)

    if position == 0:
        nollor = nollor + 1
print(nollor)
