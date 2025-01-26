# 아래 배열에서 중복되는 요소를 제거하시오.
from typing import OrderedDict

input = ['a', 1, 2, 3, 4, 'a', 5, 5, 'a', 6, 6, 7, 8, 'b']

if __name__ == '__main__':
    print(list(set(input)))
    print(list(OrderedDict.fromkeys(input).keys()))

    result = []
    for i in input:
        if i not in result:
            result.append(i)
    print(result)