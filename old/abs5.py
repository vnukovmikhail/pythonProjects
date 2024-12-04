def is_vowel(char):
    if len(char) == 1 and char.isalpha():
        return char.lower() in 'aeiouyoауеыоэяи'
    else:
        print('ввести необходимо именно 1 символ и именно букву')

i = is_vowel(input('введите символ \n'))
if i:
    print('да, это гласная')
else:
    print('нет, это не гласная')