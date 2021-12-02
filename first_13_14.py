# ******************************************************** 26_10_2021

# lst = [1, 2, 3, 4, 5]
# itr = iter(lst)
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))

# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst, 1)
# c = next(b)
# print(c)
# print(type(c))
# print(next(b))

# c = [7,8,9]
# a = (1, 2, 3)
# b = [*a, 4, 5, 6, *c]
# print(b)


# def fun(*arg):
#     return arg
#
#
# print(fun(1))
# print(fun(1, 2, 3, "abc"))
# print(fun())


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#     # return sum(params)
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 5, 1))

# ******************************************************** TASK 1

# def fun(*arg):
#     return {i: i for i in arg}
#
#
# print(fun(1, 2, 3, 4))
# print(fun("abc", 3.55 , 1))


# ******************************************************** TASK 2  * * * * *  1


# def fun(*args):
#     s = sum(args) / len(args)
#     print(s)
#     return [i for i in args if i < s]
#
#
# print(fun(1, 2, 3, 4))
# print(fun(3 , 1))


# def print_scores(student, *scores):
#     print("Имя студента:", student)
#     for s in scores:
#         print(s, end=" ")
#     print()
#
#
# print_scores("Валентин", 100, 90, 88, 92, 99)
# print_scores("Роман", 96, 20, 33, 56)


# ******************************************************** TASK 3

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2 != 0):
#
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 1234, 323, 4456, 5687, 62, 7345, 81, 91))
# print(func(12, 1234, 323, 4456, 5687, 62, 7345, 81, 91, only_add=True))


# def fun(**qwerty):
#     return qwerty
#
#
# print(fun(a=1, b=2, c=3))

# ******************************************************** TASK 4


# def info(**data):
#     for k, v in data.items():
#         print(k, "is", v)
#     print()
#
#
# info(first_name="Irina", last_name="Sharma", age=22, phone="1234567890")
# info(first_name="Igor", last_name="Sharma",
#      email="mail@mail.ru", country="Russia", age=22, phone="1234567890")


# ******************************************************** TASK 5 * * * * * 1

# my_dict = {'one': 'first'}
#
# def db(**data):
#     my_dict.update(**data)
#     return my_dict
#
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict, db(k1=22, k2=31, k3=11, k4=91))

# my_dict = {'one': 'first'}
#
# def db(**kwargs):
#     my_dict.update(**kwargs)
#     return my_dict
#
#
# db(k1=22, k2=31, k3=11, k4=91)
# print('my_dict = ', db(name='Bob', age=31, weight=61, eyes='grey'))


# def func(name, *args, odd=False, **kwargs):
#     return name, args, odd, kwargs
#
# print(func("Irina", 1,2,3,4, odd=True, one="1", three="3"))


# def func(name, *args, **kwargs):
#     print(args[0])
#     print(kwargs['odd'])
#
# func("Irina", 1,2,3,4, odd=True, one="1", three="3")


# x = {"a":1,'b':2}
# y = {"b":3,'c':4}
# z = {**x, "one":1,'two':2, **y}
# print(z)

# *********************************** NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW NEW

# name = "Tom"
# print(name)
#
# def hi():
#     global name
#     name = "Sam"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
# print(name)
# hi()
# print(name)
# bye()


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5


# def add_two(a):
#     x = 2
#     return a + x
#
# print(add_two(3))
# print(x)


# def add_five(a):
#     x = 2
#
#     def wrap():
#         print("x =", x)
#         return a + x
#     return wrap()
#
# print(add_five(5))


# x = 4
#
#
# def func():
#     a = 3
#     print(x + a)
#
# func()


# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)


# ******************************************************** 28_10_2021


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world!")
# outer_func("star!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("Сумма внутренней фенкции:", a + b)
#
#     print("Значение внешней переменной a:", a)
#
#     fun2(4)
#
#
# fun1()


# ************************************** un
# x = 25
#
#
# def fn():
#     global t  # не очень хороший тон
#     a = 30
#
#     print("global:", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal", a)
#         return
#     inner()
#     t = a
#     return
#
#
# fn()
#
#
# z = x + t
# print(z)


# def fn1():
#     x1 = 25
#
#     def fn2():
#          x1 = 33
#
#          def fn3():
#             nonlocal x1
#             x1 = 55
#
#          fn3()
#          print("fn2.x1 =", x1)
#
#     fn2()
#     print("fn1.x1 =", x1)
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print("result =", result)


# *********************************************************** TASK 1

# s = 0
#
#
# def rect_paral_square(a, b, c):
#
#     def rect_square(i, j):
#         return i * j
#     global s
#     s = 2 * rect_square(a, b) + rect_square(a, c) + rect_square(c, b)
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print("s =", s)
# print(rect_paral_square(5, 8, 2))
# print("s =", s)
# print(rect_paral_square(1, 6, 8))
# print("s =", s)


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# #print("s =", s)
# print(rect_paral_square(5, 8, 2))
# #print("s =", s)
# print(rect_paral_square(1, 6, 8))
# #print("s =", s)


# ************************************************* closure (замыкание)

# def increment(n):
#     def inner_increment(x):
#         return n + x
#     return inner_increment
#
#
# a = increment(12)
# print(a(5))
# # print(increment(12)(5)) # не очень хороший тон


# def func1():
#     a = 1
#     b = "line"
#     c = [1,2,3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_1"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# *********************************************************** TASK 2

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Moscow')
# res1()
# res1()
# res2 = func('Sochi')
# res2()
# res2()
# res1()


# ******************************************************* STUDENTS
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classfilter(lower, upper):
#     def class_student(exam):
#         return {k: v for (k, v) in exam.items() if lower <= v <= upper}
#
#     return class_student
#
#
# a = make_classfilter(80, 100)
# b = make_classfilter(70, 80)
# c = make_classfilter(50, 70)
# d = make_classfilter(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# ************************************************ !!!

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass  # print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
#
# obj2 = func(5, 2)
# print(obj1.sub())
#
# obj3 = func(5, 2)
# print(obj1.mul())


# ********************************************* Anonimus Functions - Lambda

# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y # не очень хороший тон, но работает
# print(func(1, 2))
# print(func("a", "b"))

# print((lambda x, y: (x ** 2) + (y ** 2))(2, 5))


# summ = lambda a=1, b=2, c=3: a + b + c # пример
#
# print(summ())
# print(summ(10))
# print(summ(10, 20))
# print(summ(10, 20, 30))


# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1("a", "b", "c", "d"))


# ************************************************** крутой
# c = (lambda x: x*2,
#      lambda x: x*3,
#      lambda x: x*4)
#
# for t in c:
#     print(t("abc"))


# **************************************************

# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: (lambda x: x + n))
#
#
# f = inc(42)
# print(f(0))
# print(f(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))


print((lambda x: (lambda y: lambda z: x + y + z))(2)(4)(6))

sum3 = (lambda x: lambda y: lambda z: x + y + z)

print(sum3(2)(4)(6))

# || равно

def f1(x):
    def f2(y):
        def f3(z):
            return x + y + z
        return f3
    return f2


print(f1(2)(4)(6))