#888
n = int(input('vvedite cislo '))

def inverse(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return reversed_num

print(inverse(n))