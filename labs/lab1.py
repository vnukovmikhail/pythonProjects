h = int(input('стоимость старого авто: '))
k = int(input('денег в банке: '))
x = int(input('стоимость нового авто: '))

res = h+k-x
print(f'итого {h}$ + {k}$ равно {h+k}$ \nостаток {res}$')

if res > 0:
    print('ну хоть что то осталось')
elif res == 0:
    print('семьянин какой? - всю жизнь с протянутой рукой')
elif res < 0:
    print('ну все, семья в долговой яме.')