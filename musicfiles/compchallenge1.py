
n = int(input())

fizz_buzz = ["fizzbuzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
             for x in range(1, n+1)]

print(fizz_buzz)

for buzz in fizz_buzz:
    print(buzz.center(12, '*'))
