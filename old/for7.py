#14
n = []
while True:
    i = int(input('n = ?, zero to stop '))
    if i == 0:
        break
    n.append(i)

p = int(input('p = ? '))
k = int(input('k = ? '))
d = 0

for item in n:
    if item / p == k:
        d+=1

print(f'cisla [n] delatsa na [p] i poluceaut [k] {d}raz ')