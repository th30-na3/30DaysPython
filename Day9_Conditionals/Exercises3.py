# Day 9: 30 days of Python

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skill_list = person['skills']
    print(skill_list[len(skill_list) // 2])
    print('Python' in skill_list)

    list_len = len(skill_list)
    if list_len == 2 and 'JavaScript' in skill_list and 'React' in skill_list:
        print('He is a front end developer')
    elif 'Node' in skill_list and 'Python' in skill_list and 'MongoDB' in skill_list:
        print('He is a backend developer')
    elif 'React' in skill_list and 'Node' in skill_list and 'MongoDB' in skill_list:
        print('He is a fullstack developer')
    else:
        print('Title unknown')

if person['is_married']:
    print("{} {} lives in {} and is married.".format(person['first_name'], person['last_name'], person['country']))