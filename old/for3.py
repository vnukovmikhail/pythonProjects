nums = []#444
summary = 0
while True:
    num = int(input('vvedite cislo '))
    if num == 0:
        break

    nums.append(num)

for n in nums:
    summary += n

print(summary/len(nums))