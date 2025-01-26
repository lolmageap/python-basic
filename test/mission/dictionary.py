# dictionary에서 모든 value의 합을 구하는 함수를 작성하세요.

dictionary1 = {'a': '1', 'b': '2', 'c': '3', 'd': '4'}


def sum_values(dictionary: dict[str, str]) -> int:
    return sum(map(int, dictionary.values()))


# dictionary에 value 값이 25 이하인 key-value 쌍을 제거하는 함수를 작성하세요.

dictionary2 = {'a': '1', 'b': '22', 'c': '33', 'd': '44'}


def remove_values_under_25(dictionary: dict[str, str]) -> dict[str, str]:
    for key, value in list(dictionary.items()):
        if int(value) <= 25:
            del dictionary[key]
    return dictionary


def remove_values_under_25_v2(dictionary: dict[str, str]) -> dict[str, str]:
    return {key: value for key, value in dictionary.items() if int(value) > 25}


def remove_values_under_25_v3(dictionary: dict[str, str]) -> dict[str, str]:
    return dict(((key, value) for key, value in dictionary.items() if int(value) > 25))


def remove_values_under_25_v4(dictionary: dict[str, str]) -> dict[str, str]:
    return dict(filter(lambda d: int(d[1]) > 25, dictionary.items()))


if __name__ == '__main__':
    print(sum_values(dictionary1))
    print(remove_values_under_25(dictionary2))
    print(remove_values_under_25_v2(dictionary2))
    print(remove_values_under_25_v3(dictionary2))
    print(remove_values_under_25_v4(dictionary2))