def print_backwards(*args, **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    sep = kwargs.get('sep', ' ')
    kwargs.pop('sep', None)
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=end_character, **kwargs)


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader", end="\n")
    print_backwards("Hello", "planet", "earth", "take", "me", "to", "your", "leader")


print()
print("Hello", "planet", "earth", "take", "me", "to", "your", "leader",  end="", sep="\n**\n")
backwards_print("Hello", "planet", "earth", "take", "me", "to", "your", "leader", end="", sep="\n**\n")
print("="*10)
