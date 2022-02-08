import json
from random import choice, randint

def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'b', 'd', 'e', 'f', 'e', 'g']
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


def write_json(person_dict, num):
    try:
        data = json.load(open('persons1.json'))
    except FileNotFoundError:
        data = {}

    data[num] = person_dict

    with open('persons1.json', 'w') as f:
        json.dump(data, f, indent=2)

# for i in range(5):
#     write_json(gen_person())


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])

with open('persons1.json', 'r') as f:
    print(json.load(f))


# def gen_persom():
#     name = ''
#     tel = ''
#     letters = ['a', "b", 'b', 'd', 'e', 'f', 'e', 'g']
#     num = [str(j) for j in range(10)]
#
#     while len(name) != 7:
#         name += choice(letters)
#     while len(tel) != 11:
#         tel += choice(num)
#     person = {'name': name, "tel": tel}
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = {}
#     data.update(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=5)
#
#
# person2 = {}
# for i in range(5):
#     gen_persom()
#     person2[i] = (gen_persom())
#
# print(person2)
#
# write_json(person2)

