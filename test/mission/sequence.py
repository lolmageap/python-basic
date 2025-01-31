from typing import MappingProxyType
from dis import dis # disassemble -> 바이트 코드를 보여준다.

x, y, *remain = range(10)

l = (15, 20, 25)
m = [15, 20, 25]

fruits = ["apple", "banana", "cherry", "grape"]

# immutable dict

frozen_dict = MappingProxyType({'key': 'value'})

# immutable set
frozen_set = frozenset([1, 2, 3, 4, 5])


if __name__ == "__main__":
    print(x)
    print(y)
    print(remain)

    print(l, id(l))
    print(m, id(m))

    l = l * 2
    m = m * 2

    print(l, id(l))
    print(m, id(m))

    l *= 2
    m *= 2

    # tuple은 id가 변하지 않고 list는 id가 변한다.
    print(l, id(l))
    print(m, id(m))

    # sort는 가변, sorted는 불변(내부적으로 새로운 객체를 생성)
    print(fruits.sort() is None)
    print(fruits)

    print(sorted(fruits))
    print(sorted(fruits, key=len))
    print(sorted(fruits, key=lambda x: x[-1]))
    print(sorted(fruits, reverse=True))

    # hash는 불변 객체에 대해서만 가능하다.
    hash((1, 2, 3, (4, 5))) # OK, Tuple은 불변 객체
    # hash([1, 2, 3, [4, 5]]) # TypeError: unhashable type: 'list'

    print(frozen_dict)
    print(frozen_dict.append(3)) # AttributeError: 'mappingproxy' object has no attribute 'append'

    print(frozen_set)
    dis(frozen_set)