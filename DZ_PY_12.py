# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

color = ['red', 'green', 'blue']
code = ['#FF000', '#008000', '#0000FF']
dict_1 = {keys_1: values_2 for (keys_1, values_2) in zip(color, code)}
print(dict_1)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

a = {i: i ** 3 for i in range(1, 11)}
print(a)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

a_1 = ['color', 'fruit', 'pet']
b_2 = ['blue', 'apple', 'dog']
# sss = {x: b_2 for x in a_1}
sss = {keys_1: values_2 for (keys_1, values_2) in zip(a_1, b_2)}
print(sss)
