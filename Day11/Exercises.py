# Day 11: 30 days of Python

import math

# Level 1

def add_two_numbers(n1, n2):
    return n1 + n2

print(add_two_numbers(6, 7))

def area_of_circle(radius, pi = 3.14):
    return radius*radius*pi

print(area_of_circle(4))

def add_all_numbers(*nums):
    sum = 0
    for n in nums:
        if(type(n) == int):
            sum += n
        else:
            print('One of the elements is not a number!')
            return
    return sum

print(1, 2, 4, 6)

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

convert_celsius_to_fahrenheit(18)

def check_season(season):
    s = 'season'
    if (type(season) == str):
        s = season.lower()
    if s == 'september' or s == 'october' or s == 'november':
        return 'Autumn'
    elif s == 'december' or s == 'january' or s == 'febuary':
        return 'Winter'
    elif s == 'march' or s == 'april' or s == 'may':
        return 'Spring'
    elif s == 'june' or s == 'july' or s == 'august':
        return 'Summer'
    else:
        return 'Season not recognized'
    
print(check_season('Febuary'))
    
def calculate_slope(a,b):
    return -1 * a/b

print(calculate_slope(-2, 4))

def solve_quadratic_eqn(a,b,c):
    delta = (b**2) - (4*a*c)
    if delta > 0:
        sol1 = (-b + math.sqrt(delta)) / (2*a)
        sol2 = (-b - math.sqrt(delta)) / (2*a)
        print("The equation has two solutions:", sol1, sol2)
    elif delta == 0:
        sol = (b + math.sqrt(delta)) / (2*a)
        print("The equation has one solution:", sol)
    else:
        print("The solution has no real solutions")

print(solve_quadratic_eqn(-2, 3, 2))

def print_list(l):
    for e in l:
        print(e)

print_list(['banana', 'mango','oats'])

def reverse_list(l):
    if (type(l) == list):
        start_index = 0
        end_index = len(l) - 1
        while start_index < end_index:
            aux = l[start_index]
            l[start_index] = l[end_index]
            l[end_index] = aux
            start_index += 1
            end_index -= 1
        return l
    else:
        print('Parameter is not a list')
        return
    
print(reverse_list([1, 2, 3, 4, 5]))
    
def capitalize_item_list(l):
    if type(l) == list:
        for i in range(len(l)):
            if type(l[i]) == str:
                l[i] = l[i].capitalize()
    return l

print(capitalize_item_list(['grandpa', 3, True, 'sAuce']))

def add_item(l,e):
    if(type(l) == list):
        l.append(e)
    return l

print(add_item([1, 2, 3], 4))

# I looked online and found you can impose a type on parameters

def remove_item(l: list, e):
    if e in l:
        l.remove(e)
    return l

print(remove_item(['Pikachu', 'Raichu', 'Pichu', 'Emolga'], 'Emolga'))

def sum_of_numbers(n: int):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(sum_of_numbers(5))

def sum_of_odds(n: int):
    sum = 0
    for i in range(1, n+1, 2):
        sum += i
    return sum

print(sum_of_odds(5))

def sum_of_even(n: int):
    sum = 0
    for i in range(0, n+1, 2):
        sum += i
    return sum

print(sum_of_even(5))

# Level 2

def evens_and_odds(n: int):
    evens = 0
    odds = 0
    for i in range(n+1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    print("There are {} even numbers".format(evens))
    print("There are {} odd numbers".format(odds))

evens_and_odds(100)

def factorial(n: int):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(5))

def is_empty(e):
    if (type(e) == int or type(e) == complex or type(e) == float):
        print("It's not empty")
    else:
        if (len(e) == 0):
            print("It's empty")
        else:
            print("It's not empty")

is_empty(1)
is_empty([3,4,5])
is_empty([])

def calculate_mean(l: list[int]):
    nr_of_items = len(l)
    sum_of_items = 0
    for i in l:
        sum_of_items += i
    return sum_of_items / nr_of_items

print(calculate_mean([1,2,3,4,5,6]))

def greet(name = 'Guest'):
    print('Hello, {}!'.format(name))

greet()
greet('Jane')

# Level 3

def is_prime(n: int):
    if (n == 1 or n == 2):
        return True
    if (n == 0):
        return False

    prime = True
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
            return prime
    return prime

print("Are numbers prime?")
print(is_prime(9))
print(is_prime(7))
print(is_prime(41))

def is_same_type(l: list):
    t = type(l[0])
    for e in l:
        if type(e) != t:
            return False
    return True
print("Are lists same data type?")
print(is_same_type([1,'two',3,4]))
print(is_same_type([1,2,3]))

def is_unique(l: list):
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] == l[j]:
                return False
    return True

print("Are elements unique?")

print(is_unique(['Ana', 'Ion', 'Pascalopol']))
print(is_unique([1,1,2]))

    
