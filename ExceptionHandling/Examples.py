def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)


try:
    print(factorial(992))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorial that large")
# except ZeroDivisionError:
#     print("Division by Zero")

print("Program Terminated")
