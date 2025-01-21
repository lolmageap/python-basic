class MyIterator:
    def __init__(self, max: int):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1
            return self.n
        else:
            raise StopIteration

def my_generator(max: int):
    n = 0
    while n < max:
        n += 1
        yield n

if __name__ == '__main__':
    it = MyIterator(5)
    for i in it:
        print(i, end=' ')
    print()
    print("=" * 15)
    for i in my_generator(6):
        print(i, end=' ')