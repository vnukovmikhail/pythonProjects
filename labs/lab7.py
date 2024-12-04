def CIFRA_PARA(n):
    n_str = str(n)

    for digit in reversed(n_str):
        if int(digit) % 2 == 0:
            print(f'последняя четная цифра3: {digit}')
            return True
    print('четных цифр в числе нет.')
    return False

n = int(input("введите n (не более 6 цифр): "))
if len(str(n)) > 6:
    print('тебе кто позволил?')
else:
    CIFRA_PARA(n)
