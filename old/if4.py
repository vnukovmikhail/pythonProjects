# number 7

ms = [31, 28, 31, 30,
      31, 30, 31, 31,
      30, 31, 30, 31]
y = int(input('vvedite year[xxxx] '))
m = int(input('vvedite month[xx] '))

if (y % 4 == 0):
    if (m == 2):
        print(f'v {m}month {ms[m - 1] + 1}dney')
    else:
        print(f'v {m}month {ms[m - 1]}dney')
else:
    print(f'v {m}month {ms[m - 1]}dney')