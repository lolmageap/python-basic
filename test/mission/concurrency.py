a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

b = iter(a)

while True:
    try:
        print(next(b))
    except StopIteration:
        break

class WordSplitter:
    def __init__(self, text):
        self.idx = 0
        self.words = text.split(' ')

    def __next__(self):
        try:
            word = self.words[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return word


# Generator Pattern

class WordSplitGenerator:
    def __init__(self, text):
        self.words = text.split(' ')

    def __iter__(self):
        for word in self.words:
            yield word


if __name__ == "__main__":
    text = "Do today what you could do tomorrow"
    splitter = WordSplitter(text)

    gen = WordSplitGenerator(text)
    print("Generator:", [word for word in gen])