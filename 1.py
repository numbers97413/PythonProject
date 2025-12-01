from pathlib import Path

rotationer = Path('input.txt').read_text(encoding='utf-8').splitlines()

position = 50
for rotation in rotationer:
    lengd = len(rotation)
    heltal = int(rotation[1:lengd])
    print(rotation[0], heltal, rotation)
    if rotation[0] == 'L':
        position = position - heltal
        print(position)
    else:
        position = position + rotation
        print(position)

