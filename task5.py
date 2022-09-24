import random


def random_carriage(coupe_amount=9):
    """
    Определяет все места в вагоне

    Arg:
        coupe_amount(int): количество купе - 9

    Returns:
        (carriage): все места в вагоне
    """
    carriage = []
    coupe = {}
    for place in range(1, coupe_amount * 4 + 1):
        coupe[place] = random.choice([None, 'м', 'ж'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage


def print_carriage(carriage):
    """
    Выводит все места в вагоне

    Arg:
        carriage(int): вагон
    """
    for index, coupe in enumerate(carriage):
        print(index + 1, ':', coupe)


def empty_coupe_list(carriage):
    """
    Определяет свободные места в вагоне

    Arg:
        carriage(int): вагон

    Returns:
        (answer): ответ на первый вопрос
    """
    answer = {}
    for index, coupe in enumerate(carriage):
        if not any(coupe.values()):
            answer[index + 1] = coupe
    return answer


def empty_place_list(carriage):
    """
    Определяет свободные места в купе

    Arg:
        carriage(int): вагон

    Returns:
        (answer): ответ на второй вопрос
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place]:
                answer.append(place)
    return answer


def empty_lh_place_list(carriage, low=True):
    """
    Определяет свободные нижние/верхние места в вагоне

    Arg:
        carriage(int): вагон

    Returns:
        (answer): ответ на третий вопрос
    """
    answer = []
    for coupe in carriage:
        for place in coupe:
            if not coupe[place] and place % 2 == int(low):
                answer.append(place)
    return answer


def empty_places_in_gender_coupe(carriage, gender):
    """
    Определяет свободные места в вагоне исключительно с мужской/женской компанией

    Arg:
        carriage(int): вагон

    Returns:
        (answer): ответ на четвертый/пятый вопрос
    """
    answer = []
    for coupe in carriage:
        answer1 = []
        for place in coupe:
            if not coupe[place]:
                answer1.append(place)
            elif coupe[place] != gender:
                break
        else:
            if len(answer1) < 4:
                answer += answer1
    return answer


carriage = random_carriage()
print_carriage(carriage)

print('Список полностью свободных купе')
print(empty_coupe_list(carriage))
print('Список свободных мест в вагоне')
print(empty_place_list(carriage))
print('Список свободных нижних мест в вагоне')
print(empty_lh_place_list(carriage))
print('Список свободных верхних мест в вагоне')
print(empty_lh_place_list(carriage, False))
print('Список свободных мест в купе с исключительно мужской компанией')
print(empty_places_in_gender_coupe(carriage, 'м'))
print('Список свободных мест в купе с исключительно женской компанией')
print(empty_places_in_gender_coupe(carriage, 'ж'))
