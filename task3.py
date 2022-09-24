def symbol_statistics(text):
    """Возвращает статистику символов в тексте

    Arg:
        text(str):текст

    Returns:
        dict: статистика символов в виде словаря
    """
    stat = {}
    for letter in text:
        letter = letter.lower()
        stat[letter] = stat.get(letter, 0) + 1
    return stat


text = input('Input text -->')
stat = symbol_statistics(text)
for symbol in sorted(stat):
    print(symbol, '=', stat[symbol])
