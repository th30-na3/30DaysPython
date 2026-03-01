# Day 5: 30 days of Python

empty = []

lst = ['Gran', 'Vira', 'Kat', 'Wilnas', 'Galeon']
print('list length:', len(lst))
first = lst[0]
middle = lst[2]
last = lst[-1]
print(first, middle, last)

mixed_data_types = ['Theo', 20, False, 'my address']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print('Number of companies:', len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
it_companies[0] = 'Instagram'
print(it_companies)
it_companies.append('JetBrains')
it_companies.insert(len(it_companies)//2, 'Mojang')
print(it_companies)
it_companies[0] = it_companies[0].upper()
companies = '#; '.join(it_companies)
print(companies)

print('Mojang' in it_companies)

it_companies.sort()
it_companies.reverse()
print(it_companies)

first_three_companies = it_companies[0:3]
last_index = len(it_companies) - 1
last_three_companies = it_companies[last_index - 2:last_index + 1]
print(first_three_companies)
print(last_three_companies)

middle_company = it_companies[len(it_companies) // 2]
print(middle_company)

it_companies.pop(0)
it_companies.pop(len(it_companies) // 2)
it_companies.pop(len(it_companies) - 1)
print(it_companies)

it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

joined = front_end + back_end
insert_index = joined.index('Redux') + 1
joined.insert(insert_index, 'Python')
joined.insert(insert_index, 'SQL')
print(joined)
