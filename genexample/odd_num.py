def odd_numbers():
    i = 1
    while True:
        yield i
        i += 2


def pi_series():
    num = odd_numbers()
    number = 0
    while True:
        number += (4/next(num))
        yield number
        number -= (4/next(num))
        yield number


pi = pi_series()

for i in range(10000000):
    next(pi)

print(next(pi))
