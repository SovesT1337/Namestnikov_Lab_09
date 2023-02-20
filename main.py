def numbers_range():
    af, factorial, i_ = 0, 1, 1
    while True:
        factorial = factorial * i_
        af = factorial - af
        i_ += 1
        yield af


if __name__ == '__main__':
    a = numbers_range()
    print(type(a))
    for i in range(10):
        print(next(a))
