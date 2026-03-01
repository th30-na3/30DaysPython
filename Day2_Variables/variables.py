# Day 2: 30 days of Python

first_name = "Ambu"
last_name = "Sked"
full_name = "Ambu Sked"
country = "Romania"
city = "Constangeles"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = False
fav_pokemon, color, _type, dex_number, is_legendary = 'Buizel', 'Orange', 'Water', 418, False

print("Favorite Pokemon:",fav_pokemon,"\nColor:",color,"\nDex Number:",str(dex_number))

print(type(first_name))
print(type(age))
print(type(is_married))

print('First name length:', len(first_name))
print('Last name length:', len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
divison = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(num_one,num_two,total,diff,product,divison,remainder,exp,floor_division)

radius = int(input('Enter Radius: '))
print('Circle area:',radius**2 * 3.14)
input_name = input("Enter name: ")
input_age = input("Enter age: ")
print("Name:",input_name,"Age:",input_age)