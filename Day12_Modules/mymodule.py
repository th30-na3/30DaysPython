# Day 12: 30 days of Python

import random
import string

def random_used_id():
    id = ''.join(random.choices(string.ascii_letters + string.digits, k = 6))
    return id

def used_id_gen_by_user():
    idlen = int(input("How long should the ids be?: "))
    idnr = int(input('How many ids do you want?: '))
    idlist = []
    for i in range(idnr):
        id = ''.join(random.choices(string.ascii_letters + string.digits, k = idlen))
        idlist.append(id)
    return idlist

def rgb_color_gen():
    color1 = random.randint(0,255)
    color2 = random.randint(0,255)
    color3 = random.randint(0,255)
    return 'rgb({},{},{})'.format(color1, color2, color3)

def list_of_hexa_colors(nr: int):
    lst = []
    for i in range(nr):
        hexa = '#'
        chars = (random.choices('1234567890abcdef', k = 6))
        for c in chars:
            hexa += c
        lst.append(hexa)
    return lst

def list_of_rgb_colors(nr : int):
    lst = []
    for i in range(nr):
        lst.append(rgb_color_gen())
    return lst

def generate_colors(type: str, nr: int):
    if (type == 'rgb'):
        return(list_of_rgb_colors(nr))
    elif (type == 'hexa'):
        return(list_of_hexa_colors(nr))
    else:
        return 'Unknown color type'

def shuffle_list(l: list):
    list_len = len(l)
    for i in range(10):
        pos1 = random.randint(0, list_len - 1)
        pos2 = random.randint(0, list_len - 1)
        aux = l[pos1]
        l[pos1] = l[pos2]
        l[pos2] = aux

