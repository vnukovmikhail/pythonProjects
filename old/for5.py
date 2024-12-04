#555 factorial
def factorial(number):
    i = 1
    for n in range(number):
        i *= n + 1
    return i

print(factorial(int(input('vvedite cislo '))))