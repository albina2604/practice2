text = input("Введите текст, который хотите зашифровавать: ")
k = int(input("Укажите ключ: "))


def ceaser_cipher(user, key):
    """
    Возвращает предыдущею дату

    Arg:
        user(int): пользователь
        key(int): ключ

    Returns:
        (day, month, year):предыдущая дата
    """
    res, n = [], ""
    dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for i in range(len(user)):
        if user[i] in dictionary:
            n = dictionary
        elif user[i] in dictionary_upper:
            n = dictionary_upper
        else:
            res.append(user[i])
        if user[i] in n:
            for j in range(len(n)):
                if 0 <= j + key < len(n) and user[i] == n[j]:
                    res.append(n[j + key])
                elif j + key >= len(n) and user[i] == n[j]:
                    res.append(n[(1 - j - key) % (len(n) - 1)])
                elif j + key < 0 and user[i] == n[j]:
                    res.append(n[(j + key) % len(n)])
    return ''.join(res)


print(ceaser_cipher(text, k))
