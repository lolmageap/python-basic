data = """
            park 800905-1049118
            kim  700905-1059119
        """.strip()

def read_key_value(string: str) -> dict[str, str]:
    result = {}
    for line in string.split('\n'):
        if line:
            key, value = line.split()
            result[key] = value
    return result

def hide_second_registration_number(
        dictionary: dict[str, str],
) -> dict[str, str]:
    result = {}
    for key, value in dictionary.items():
        result[key] = value[0:8] + '******'
    return result

if __name__ == '__main__':
    dictionary = read_key_value(data)

    hided_dictionary = hide_second_registration_number(dictionary)
    print(hided_dictionary)