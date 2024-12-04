# номер 5
x = int(input('x '))
y = int(input('y '))

if((x<0) & (y>0)):
    print('I', end='')
elif((x>0) & (y>0)):
    print('II', end='')
elif((x>0) & (y<0)):
    print('III', end='')
elif((x<0) & (y<0)):
    print('IV', end='')

elif(( x== 0) & (y == 0)):
    print('(0;0) ', end='')
elif(x == 0):
    print('osi x ', end='')
elif(y == 0):
    print('osi y ', end='')

print(f'({x};{y})')