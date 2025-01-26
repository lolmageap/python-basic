# 1부터 15까지 `원소 * 10`, 결과는 문자열의 배열로 출력해라

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def mission_lambda(array: list[int]) -> list[str]:
    return list(map(lambda i: str(i * 10), array))

if __name__ == '__main__':
    print(mission_lambda(array))
    print(list(map(lambda i: str(i * 10), range(1, 16))))