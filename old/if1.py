# номер 4

i = int(input('ishodnoe '))
n1 = int(input('num 1 '))
n2 = int(input('num 2 '))
n3 = int(input('num 3 '))

if ((i % n1 == 0) & (i % n2 == 0) & (i % n3 == 0)):
    print(f'number {i} is good!')
else:
    print(f'number {i} is bad!')