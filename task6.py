import random


def create_votes(parties, people):
    """
    Создает голоса для голосований

    Arg:
        parties(int): партии
        people(int): люди

    Returns:
        (result): результат
    """
    result = []
    for _ in range(people):
        vote = random.randint(0, parties)
        result.append(vote if vote > 0 else -1)
    return result


def election_results(parties, votes):
    """
    Возвращает результат голосования

    Arg:
        parties(int): партии
        votes(int): голоса

    Returns:
        (result): результат голосования
    """
    results = {}
    for party in range(1, parties+1):
        results[party] = (votes.count(party))
    index = 0
    for party, vote_number in sorted(results.items(), key=lambda item: item[1], reverse=True):
        index += 1
        print(f'{index:>2}. Партия №{party:<3} | {vote_number:>8} |',
              f'{(vote_number/len(votes)*100):>10.2f}%')


votes = create_votes(10, 10000)
election_results(10, votes)
