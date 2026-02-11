# Day 4: 30 days of Python

s = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(s)

s = 'Coding ' + 'For ' + 'All'
print(s)

company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.title())
print(company.capitalize())
print(company.swapcase())
print(company[7:14])
print(company.index('Coding'))
company = company.replace('Coding', 'Python')
print(company)
text = 'Python For Everyone'
text = text.replace('Everyone', 'All')
print(text)
print('Coding For All'.index('C'))
print('Coding For All'.index('F'))
print('Coding For All People'.rfind('l'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))
print('Coding For All'.startswith('Coding'))
print('Coding For All'.startswith('coding'))
print('   Coding For All      '.strip(' '))
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())
_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(_list))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')
radius = 10
print('radius = {}\narea = 3.14 * radius ** 2\nThe area of a circle with radius {} is {:.0f} meters square'.format(radius, radius, 3.14 * radius ** 2))
a = 8
b = 6
print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))