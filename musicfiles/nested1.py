burgers = ["beef", "chicken", "spicy beans"]
toppings = ["cheese", "egg", "beans", "spam"]

# print([(burger, topping) for burger in burgers for topping in toppings])

for meals in [(burger, topping) for burger in burgers for topping in toppings]:
    print(meals)
# meals = [(burger, topping) for burger in burgers for topping in toppings]
# print(meals)

print()
# # meals = []
    # for burger in burgers:
    #     for topping in toppings:
    #         print((burger, topping))
        # meals.append((burger, topping))
# print(meals)

for nested_meals in [[(burger, topping) for burger in burgers] for topping in toppings]:
    print(nested_meals)

print()

for nested_meals in [[(burger, topping) for topping in toppings]for burger in burgers]:
    print(nested_meals)
