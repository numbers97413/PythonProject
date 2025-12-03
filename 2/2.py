from pathlib import Path

# Each line becomes a list of strings, split by comma
ranges = [
    line.split(",")                  # split the line
    for line in Path('input.txt').read_text(encoding='utf-8').splitlines()
    if line.strip()                  # optional: skip empty lines
]

print(ranges)

for range in ranges:
    #print(range)
    a, b = range.split("-")
    print(a, b)
