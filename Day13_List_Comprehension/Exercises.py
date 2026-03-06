# Day 13: 30 days of Python

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([i for i in numbers if i <= 0])

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([i for row in list_of_lists for i in row])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print([(i, 1, i, i**2, i**3, i**4, i**5) for i in numbers])

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print([[tup[0].upper(), tup[0].upper()[0:3], tup[1].upper()] for lst in countries for tup in lst])

print([{'country':i[0].upper(), 'city':i[1].upper()} for lst in countries for i in lst])

names = [[('Asabeneh', 'Yetayeh')], [('Lady', 'Gaga')], [('Kamala', 'Harris')], [('John', 'Doe')]]

print([(i[0] + ' ' + i[1]) for lst in names for i in lst])

f = lambda m, n: n
print('y-intercept:', f(2, -3))