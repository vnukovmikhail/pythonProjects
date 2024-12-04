# from collections import namedtuple
#
# record = namedtuple('record', ['x', 'y'])
# p = record(x=1, y=3)
# print(p)

# lines1 = ['kurkuma\n', '!<off>\n', 'im bored...\n']
# lines2 = ['kiki\n', 'hello\n', 'how are u?\n']
# with open('k.txt', 'w+') as file:
#     file.writelines(lines1)
# with open('k.txt', 'r+') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end='')

def write():
    value = input()
    with open('file.txt', 'a+') as file:
        file.write(value + '\n')

def read():
    with open('file.txt', 'r+') as file:
        lines = file.readlines()
        lc = len(lines)
        max = 5
        if lc >= max:
            print('<---------->')
            for l in range(max):
                print(lines[l], end='')
            print('<---------->')
            while True:
                slt = int(input('1.See all\t2.Skip\n'))
                match slt:
                    case 1: pass
                    case 2: break
                    case _: break
                print('<---------->')
                for line in lines:
                    print(line, end='')
                print('<---------->')
                break

while True:
    try:
        selection = int(input('1.Write in file\t2.Read file\t3.Exit\nSelect: '))
    except ValueError:
        print('<Value_Error>')
        break
    match selection:
        case 1: write()
        case 2: read()
        case 3: break
        case _: print('incorrect value')