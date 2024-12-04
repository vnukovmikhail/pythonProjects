def check_pairs():
    arr = list(map(int, input("через пробел все введи, спустя секунду ответ свой получи: ").split()))
    for i in range(len(arr) - 1):  # Проходим по всем элементам, кроме последнего
        if arr[i] == arr[i + 1]:
            print("Пара!")
            return True

    print("Мда тут ничего похожего на соседние пары")
    return False

check_pairs()