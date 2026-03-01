# Day 10: 30 days of Python

# Level 1

for i in range(10):
    pass

count = 0
while count <= 10:
    count += 1

for i in range(10,-1,-1):
    print('{} '.format(i), end='')
print()

count = 10
while count >= 0:
    count -= 1

for i in range(1,8):
    for j in range(i):
        print('#', end='')
    print()

for i in range(8):
    for j in range(8):
        print('# ', end='')
    print()

for i in range(11):
    print('{} x {} = {}'.format(i, i, i*i))

for l in ['Python', 'Numpy','Pandas','Django', 'Flask']:
    print(l)

for i in range(101):
    if i % 2 == 0:
        print('{} '.format(i), end='')
print()

for i in range(101):
    if i % 2 != 0:
        print('{} '.format(i), end='')
print()

# Level 2

sum = 0
for i in range(101):
    sum += i
print('Sum of all numbers is', sum)

sum_odd = 0
sum_even = 0
for i in range(101):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print('Sum of all even is {}. Sum of all odd is {}'.format(sum_even, sum_odd))

# Level 3

l = ['banana', 'orange', 'mango', 'lemon']

start = 0
end = len(l) - 1

while start < end:
    aux = l[start]
    l[start] = l[end]
    l[end] = aux
    start += 1
    end -= 1

print(l)
