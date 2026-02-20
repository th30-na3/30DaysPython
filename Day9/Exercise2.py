# Day 9: 30 days of Python

score = int(input("Enter your test score: "))

if score >= 90 and score <= 100:
    print("Your grade is A")
elif score >= 80 and score <= 89:
    print("Your grade is B")
elif score >= 70 and score <= 79:
    print("Your grade is C")
elif score >= 60 and score <= 69:
    print("Your grade is D")
else:
    print("Your grade is F")

month = str(input("What month is it? : "))
month = month.lower()
if month == 'september' or month == 'october' or month == 'november':
    print("The season is Autumn")
elif month == 'december' or month == 'january' or month == 'febuary':
    print("The season is Winter")
elif month == 'march' or month == 'april' or month == 'may':
    print("The season is Spring")
elif month == 'june' or month == 'july' or month == 'august':
    print("The season is Summer")
else:
    print("Invalid month")

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = str(input("What fruit do you want to add to the basket? : "))

if fruit in fruits:
    print('The fruit already exists in the list')
else:
    fruits.append(fruit)
    print(fruits)