nat = [] #222
i = 1
s = 0

def is_two_digit_number(number):
    return (10 <= abs(number) < 100)

while True:
    i = int(input('vvedite cislo [0 to exit] '))
    if i == 0:
        break
    nat.append(i)

    if is_two_digit_number(i):
        s += 1

print(f'vislo dvuhznacnih {s} ')