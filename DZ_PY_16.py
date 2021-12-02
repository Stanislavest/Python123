#  * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 1

str = "Я изучаю Nuthon. Мне нравится Nuthon. " \
       "Nuthon очень интересный язык программирования"


def rnm(s, s_1, s_2):
    a = ''
    for i in range(len(s)):
        if s[i] == s_1:
            a = a[:i] + s_2
        else:
            a = a[:i] + s[i]
    return a


print(str)
print(rnm(str,'N','P'))

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 2

# s = '0123456789'
# print(s)
# d = int(input('Номер позиции: '))
# s2 = s[:d] + s[d + 1:]
# print(s2)

# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 3

# s = '0123_456_123_456_123_456_789_789_7890'
# print(s)
# d = input('Символ на удаление: ')
# s2 = ''
# i = 0
# while i < len(s):
#     if s[i] == d:
#         pass
#     else:
#         s2 = s2 + s[i]
#     i += 1
# print(s2)


# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * 4

# num = int(input('->'))
# binnum = ''
# while num > 0:
#     binnum = str(num % 2) + binnum
#     num = num // 2
# print(binnum)


