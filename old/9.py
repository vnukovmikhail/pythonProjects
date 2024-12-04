r = int(input('какая сумма вложена под процент '))
w = int(input('какой процент '))
n = int(input('сколько месяцев '))


for i in range(n):
    r += r * (w/100)

print('%.2f' % r)