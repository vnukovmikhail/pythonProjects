n = 10 #kolicestvo povtorenii 333
numbers = []
s = 0
while (n > 0):
    numbers.append(input(f'vvedite {n} cislo '))
    n-=1

for num in numbers:
    if int(num) % 2 == 0:
        s+=1

print(f'cetnih u nas {s}')