# 아래 배열 3개를 dictionary 형태로 만든다. `a : b * c`

a = ["one", "two", "three", "four"]
b = [1.4, 2.1, 3.5, 4.8]
c = [10, 20, 30, 40]


def from_dictionary(
        key: list[str],
        first_value: list[float],
        last_value: list[int],
) -> dict[str, int]:
    result = {}
    for x, y, z in zip(key, first_value, last_value):
        result[x] = int(y * z)
    return result


def from_dictionary_v2(
        key: list[str],
        first_value: list[float],
        last_value: list[int],
) -> dict[str, int]:
    return {x: int(y * z) for x, y, z in zip(key, first_value, last_value)}


if __name__ == "__main__":
    print(
        from_dictionary(
            key=a,
            first_value=b,
            last_value=c,
        )
    )

    print(
        from_dictionary_v2(
            key=a,
            first_value=b,
            last_value=c,
        )
    )

    print(
        from_dictionary_v3(
            key=a,
            first_value=b,
            last_value=c,
        )
    )
