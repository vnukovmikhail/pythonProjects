v = input()
cmd = list(map(str, v))
print(cmd)
for el in cmd:
    match el.upper():
        case 'S':
            print('Юг ждет!', end=',')
        case 'N':
            print('Какой холодный север', end=',')
        case 'E':
            print('На восток!', end=',')
        case 'V':
            print('Запад!', end=',')
        case '0':
            print('Идем по-тихоничку...', end=',')
        case '1':
            print('Налево <-', end=',')
        case '2':
            print('На-пра-во!', end=',')
        case _:
            print('Ничего не понял...')