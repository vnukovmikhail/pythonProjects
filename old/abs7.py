def is_prime(number):
    if not isinstance(number, int) or number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

s = input('введите число а я узнаю является ли оно простым ')
if is_prime(int(s)):
    print('ура, оно действительно простое ')
else:
    print('нет, что то не выходит ')