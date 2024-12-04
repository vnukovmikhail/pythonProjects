# number 6

n1 = []
n2 = []

print('введите час, минуту, секунду и милисекунду')
while(len(n1) != 4):
    n1.append(int(input()))
print('введите час, минуту, секунду и милисекунду, для второго значения')
while(len(n2) != 4):
    n2.append(int(input()))

s3 = n1[3] + n2[3]
s2 = n1[2] + n2[2]
s1 = n1[1] + n2[1]
s0 = n1[0] + n2[0]

while (s3 >= 1000):
    s2 += 1
    s3 -= 1000

while (s2 >= 60):
    s1 += 1
    s2 -= 60


while (s1 >= 60):
    s0 += 1
    s1 -= 60

print(f'{s0}ч,{s1}м,{s2}с,{s3}мс')



# s1 = n1[0] * 60 * 60 * 1000 + n1[1] * 60 * 1000 + n1[2] * 1000 + n1[3]
# print(s1)
#
# s2 = ((n2[0] * 60 + n2[1]) * 60 + n2[2]) * 1000 + n2[3]
# print(s2)
#
# s = s1 + s2
# s = s / (60 * 60 * 1000)
# print(f'{s}:hours ')
#
# s = s /  ((60 * 60 * 1000) + (60 * 1000))
# print(f'{s}:minutes ')
#
# s = s /  60
# print(f'{s}:seconds ')
#
# s = s /  1000
# print(f'{s} miliseconds')