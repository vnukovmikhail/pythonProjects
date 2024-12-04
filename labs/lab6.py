n = input('введите число любое которое пожелает ваше сердце: ')
try:
    arr = list(map(int, n))
    necet = []
    cet = []

    for i in arr:
        if i % 2 == 0:
            cet.append(i)
        else:
            necet.append(i)

    max = 0
    for i in necet:
        max += i
    necet = max
    max = 0
    for i in cet:
        max += i
    cet = max

    print('сумма нечетных элементов равна ', necet)
    print('сумма четных элементов равна ', cet)


except (TypeError, ValueError):
    print(f'и что это за бред?')
