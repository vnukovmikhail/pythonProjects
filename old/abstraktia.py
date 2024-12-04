n = []
print(len(n))
while len(n) < 2:
    i = int(input('n = ?, zero to stop '))
    if i == 0:
        break
    n.append(i)

def sum(n1, n2):
    s = n1 + n2
    return s

def uj(n1, n2):
    u = n1 * n2
    return u

print(f'summa = {sum(n[0], n[1])} ')
print(f'umnoj = {uj(n[0], n[1])}  ')