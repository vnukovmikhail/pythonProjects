nums = []#666
max = 0
while True:
    i = int(input('vvedite number '))
    if i == 0:
        break
    nums.append(i)

def max_of():
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num

    return max_value

print(f'our max number of numbers is {max_of()} ')