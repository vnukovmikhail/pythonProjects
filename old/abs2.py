num = int(input('input ur number '))

def mirk(num):
    s = 0
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)
            s+=1

    return s

print(f'cislo delitelei ravno {mirk(num)} ')