a = "*"
for i in range(6):
    print(a * i)
    if i == 5:
        for i in range(5, 0, -1):
            print(a * i)