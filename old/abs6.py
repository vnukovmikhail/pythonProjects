def is_even(number):
    try:
        number = int(number)
    except (ValueError, TypeError):
        return f'нет, ты ввел что то не то... что то тут не так ({number}) '
    if number % 2 == 0:
        return 'да, четное '
    else:
        return 'нет, не четное '


s = input('введите натуральное число, и определим четное ли оно ')
print(is_even(s))