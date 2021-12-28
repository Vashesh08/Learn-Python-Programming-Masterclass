def divide_two(a: str, b: str):
    a = int(a)
    b = int(b)
    return a/b


c = input("First Number:")
d = input("Second Number:")

try:
    print(divide_two(c, d))
# except TypeError:
#     print("Please Enter a Number")
except ZeroDivisionError:
    print("Cannot be divide be zero")
except ValueError:
    print("Do not Enter a string")


def multiply_by_2(x):
    return 2*x


y = 1
print(multiply_by_2(y))
