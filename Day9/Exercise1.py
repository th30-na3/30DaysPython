# Day 9: 30 days of Python

age = int(input("Enter your age: "))

if age >= 18:
    print('You are old enough to drive')
else:
    print('You need to wait {} more years to be able to drive'.format(18 - age))

my_age = 20

if age > my_age:
    if age - my_age == 1:
        print("You are 1 year older than me")
    else:
        print("You are {} years older than me".format(age - my_age))
elif age < my_age:
    if my_age - age == 1:
        print("I am 1 year older than you")
    else:
        print("I am {} years older than you".format(my_age - age))
else:
    print("We are the same age")

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

if number1 > number2:
    print('{} is greater than {}'.format(number1, number2))
elif number1 < number2:
    print('{} is smaller than {}'.format(number1, number2))
else:
    print('{} is equal to {}'.format(number1, number2))
    