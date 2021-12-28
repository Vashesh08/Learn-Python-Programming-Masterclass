def build_tuple(*args):
    return args


def average_word_length(*args):
    length = 0
    for arg in args:
        length += len(arg)
    length /= len(args)
    return length


def smallest(*args):
    small = args[0]
    for arg in args:
        if arg < small:
            small = arg
    return small


def largest(*args):
    large = args[0]
    for arg in args:
        if arg > large:
            large = arg
    return large


def rev(*args):
    for arg in args[::-1]:
        print(arg, end=" ")


message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6)
print(type(number_tuple))
print(number_tuple)

print(largest(1, 2, 3, 4, 5, 6))
print(smallest(1, 2, 3, 4, 5, 6))

rev("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print()

words = ["hello", "planet", "earth", "take", "me", "to", "your", "leader"]
print(words)
print(*words)



