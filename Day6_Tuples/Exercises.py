# Day 6: 30 days of Python

# Exercises Level 1:

empty = tuple()

brothers = ('Ionut', 'Alejandro')
sisters = ('Maya', 'Vivienne')
print(brothers)
print(sisters)
siblings = brothers + sisters
print(siblings)
print("Nr of siblings:",len(siblings))
family_members = siblings + ('Mother', 'Father')
print(family_members)

# Exercises Level 2:
siblings = family_members[0:4]
parents = family_members[4:6]
print(siblings)
print(parents)

fruits = ('banana', 'apple')
vegetables = ('carrot', 'potato', 'cucumber')
animal_products = ('eggs', 'meat')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
food_stuff_lt.pop(len(food_stuff_lt) // 2)
print(food_stuff_lt)
first3 = food_stuff_lt[0:3]
last_index = len(food_stuff_lt) - 1
last3 = food_stuff_lt[last_index - 2: last_index + 1]
print(first3)
print(last3)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)