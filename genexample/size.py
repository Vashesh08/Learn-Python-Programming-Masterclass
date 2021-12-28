import sys


def my_range(n: int):
    start = 0
    while start < n:
        print(start)
        yield start
        start += 1


big_range = range(5)
# big_range = my_range(5)
# _ = input("line 14")

print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# creating a list containing all the values iin big_range
big_list = []

# _ = input("line 22")
for val in big_range:
    # _ = input("line 24 - inside loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)
print("Looping again or not")

for i in big_range:
    print("i is {}".format(i))
