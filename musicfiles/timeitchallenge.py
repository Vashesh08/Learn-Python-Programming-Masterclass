# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
import statistics
import timeit
 

def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result


def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


# time_fact = timeit.timeit(lambda: fact(130), number=10000)
# time_factorial = timeit.timeit(lambda: factorial(130), number=10000)

# print("Fact:  \t{}".format(time_fact))
# print("Factorial: {}".format(time_factorial))

if __name__ == '__main__':
    # print(timeit.timeit('x = fact(130)', setup="from __main__ import fact", number=10000))
    # print(timeit.timeit('x = factorial(130)', setup="from __main__ import factorial", number=10000))
    list1 = timeit.repeat('x = fact(130)', setup="from __main__ import fact", number=10000, repeat=6)
    list2 = timeit.repeat('x = factorial(130)', setup="from __main__ import factorial", number=10000, repeat=6)
    print(sum(list1))
    print(sum(list2))
    print()
    print(statistics.mean(list1), statistics.stdev(list1))
    print(statistics.mean(list2), statistics.stdev(list2))


