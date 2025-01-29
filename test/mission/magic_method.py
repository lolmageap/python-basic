class Fruit:
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price

    def __str__(self) -> str:
        return "Fruit Class is {} {}".format(self._name, self._price)

    def __add__(self, fruit: "Fruit") -> int:
        return self._price + fruit._price

    def __sub__(self, fruit: "Fruit") -> int:
        return self._price - fruit._price


fruit1 = Fruit("딸기", 1000)
fruit2 = Fruit("바나나", 3000)

total_price = fruit1 + fruit2
total_price2 = fruit2 - fruit1


class Vector(object):
    _instance = None

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, integer: int) -> "Vector":
        return Vector(self.x * integer, self.y * integer)

    def __max__(self) -> int:
        return max(self.x, self.y)


vector1 = Vector(10)
vector2 = Vector(20, 30)

if __name__ == "__main__":
    print(total_price)
    print(total_price2)
    print(vector1)
    print(vector1 + vector2)
    print(vector1.__max__())
    print(vector2 * 3)
