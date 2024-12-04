def sort_words_in_text():
    text = input("Пройдитесь пальцами по клавиатуре будто играете на пианино: ").strip()

    if text[-1] == ".":
        text = text[:-1]

    words = text.split()
    words.sort()
    print(" ".join(words))

sort_words_in_text()