#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

str1 = "I am learning Python. hello, WORLD!"
print(str1)
print(str1.replace(str1[str1.find('h'):str1.rfind('h') + 1], ''))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# str1 = "I am learning Python. hello, WORLD!"
# a = str1[:str1.find('h')]
# b = str1[str1.find('h'):str1.rfind('h') + 1]
# c = str1[str1.rfind('h') + 1:]
# str2 = a + b[::-1] + c
# print(str2)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

# str1 = '11 23 44 55 23 22'
# print('Строка: ', str1)
# a = input('Её заменяемая подстрокка: ')
# b = input('Новая подстрока: ')
# str1 = str1.replace(a, b)
# print('Строка: ', str1)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 4

# str1 = 'Ежевику для ежат \nПринесли два ежа' \
#       ' \nЕжевику еле-еле \nЕжата возле ели съели'
# print(str1)
# s1 = []
# s = str1.split()
# # print(s)
# for i in s:
#       if i[0] == 'е' or i[0] == 'Е':
#           s1.append(i)
# print('Количество слов на \"Е\":', len(s1))
