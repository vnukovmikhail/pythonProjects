monitor = int(input('стоимость монитора '))
pc = int(input('стоимость пк '))
keyboard = int(input('стоимость клавиатуры '))
mouse = int(input('стоимость мышки, пи пи пи '))
printer = int(input('стоимость принтера '))

n = int(input('сколько будем покупать? '))

s = 0
for i in range(n):
    s += monitor + pc + keyboard + mouse + printer

print(f'{s} лей.')