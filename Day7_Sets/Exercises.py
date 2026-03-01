# Day 7: 30 days of Python

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


# Level 1
print('it_companies len:', len(it_companies))
it_companies.add('Twitter')
it_companies.update(['JetBrains', 'Nintendo'])
print(it_companies)
it_companies.remove('Nintendo')
print(it_companies)

# Difference between remove and discard is 
# Remove throws an error when the element doesn't exist
# While discard does not
it_companies.discard('Iono')

# Level 2
print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
A.clear()
B.clear()
del A
del B

# Level 3
ageset = set(age)

print(len(age))
print(len(ageset))
# List size is begger than set because list contains duplicate items

text = 'I am a teacher and I love to inspire and teach people'
unique_words = set(text.split(' '))
print('Number of unique words of text:', len(unique_words))


