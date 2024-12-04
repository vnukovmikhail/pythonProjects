def find_cont_sum(n):
    if n % 2 == 0:
        print("нереально!")
    else:
        x = (n - 1) // 2
        print(f"{n} = {x} + {x + 1}")

n = int(input("ну давай мне свое число - "))
find_cont_sum(n)
