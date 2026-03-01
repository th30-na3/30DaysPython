# Day 8: 30 days of Python

dog = dict()
dog['name'] = 'Azorel'
dog['breed'] = 'German Shepard'
dog['legs'] = 4
dog['age'] = 10
print(dog)

student = {
    'first_name':'John',
    'last_name':'Doe',
    'gender':'male',
    'age':20,
    'marital_satus':False,
    'skills':['Juggling','Whistling','Tennis'],
    'country':'Germany',
    'city':'Hamburg',
    'address': {
        'street':'Schmetterling',
        'number':67
    }
}

print(len(student))
print(type(student.get('skills')))
student['skills'].append('Gaming')
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())
student.pop('age')
print(student.get('age'))
del student