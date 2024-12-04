def main():
    sum_odd = 0
    count_odd = 0

    number = int(input("введите положительное число (или 0 для завершения): "))
    if number == 0:
        pass
    else:
        while True:
            number = int(input("введите положительное число (или 0 для завершения): "))
            if number == 0:
                break
            if number % 2 != 0:
                sum_odd += number
                count_odd += 1
    if count_odd > 0:
        avg_odd = sum_odd / count_odd
        print(f"сумма нечетных чисел: {sum_odd}")
        print(f"среднее арифметическое нечетных чисел: {avg_odd}")
    else:
        print("нечетных чисел не было введено.")

main()
