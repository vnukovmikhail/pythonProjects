def calculate_average_between_min_max():
    arr = list(map(float, input("Введите элементы вектора через пробел: ").split()))

    min_value = min(arr)
    max_value = max(arr)

    mini = arr.index(min_value)
    maxi = arr.index(max_value)

    start_index = min(mini, maxi) + 1
    end_index = max(mini, maxi)

    if start_index < end_index:
        sum_elements = sum(arr[start_index:end_index])
        count_elements = end_index - start_index
        average = sum_elements / count_elements
        print(f"среднее арифметическое элементов между мин и макс: {average}")
    else:
        print("между мин и макс нет элементов для вычисления среднего арифметического...")

calculate_average_between_min_max()
