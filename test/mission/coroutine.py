from inspect import getgeneratorstate

def coroutine1():
    print('coroutine1 started')
    i = yield
    print('coroutine1 ended {}'.format(i))


def coroutine2(x):
    print('coroutine2 started {}'.format(x))
    y = yield x
    print('coroutine2 received {}'.format(y))
    z = yield x + y
    print('coroutine2 end {}'.format(z))


if __name__ == "__main__":
    cr1 = coroutine1()
    next(cr1)
    try:
        cr1.send(100)
    except StopIteration:
        pass

    cr2 = coroutine2(100)

    print(getgeneratorstate(cr2))

    print(next(cr2))

    print(getgeneratorstate(cr2))

    print(cr2.send(200))

    print(getgeneratorstate(cr2))

    # StopIteration 은 await keyword를 사용하면 발생하지 않는다. 현재 yeild를 사용하고 있기 때문에 발생한다.
    try:
        print(cr2.send(300))
    except StopIteration:
        pass

    print(getgeneratorstate(cr2))