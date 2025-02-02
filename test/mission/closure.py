class Averager:
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

averager = Averager()


def closer_average():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


def closer_average_v2():
    total = 0
    count = 0

    def averager(new_value):
        nonlocal total, count
        count += 1
        total += new_value
        return total/count

    return averager

if __name__ == "__main__":
    print(averager(10))
    print(averager(20))
    print(averager(30))
    print(averager.series)
    print(Averager()(20))