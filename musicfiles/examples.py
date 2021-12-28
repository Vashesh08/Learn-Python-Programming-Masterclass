text = "what have the romans ever done for us"

capitals = [char.upper() for char in text]
print(capitals)

capitals = [char.upper() for char in text.split()]
print(capitals)

lc_words = text.split(" ")
print(lc_words)