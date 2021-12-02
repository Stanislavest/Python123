# *** *** *** *** *** *** *** *** *** *** 1

fucn_compute = (lambda n: (lambda x: x * n))

res = fucn_compute(2)
print(res(15))
print(res(20))
res = fucn_compute(3)
print(res(15))
print(res(20))


# *** *** *** *** *** *** *** *** *** *** 2

# sum3 = (lambda x: lambda y: lambda z: x + y + z)
# print(sum3(2)(4)(6))

# *** *** *** *** *** *** *** *** *** *** 3

# st = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# res1 = sorted(st, key=lambda item: item['name'])
# res2 = sorted(st, key=lambda item: item['final'], reverse=True)
# print(res1)
# print(res2)

# *** *** *** *** *** *** *** *** *** *** 4

# st = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# n = []
#
# for i in st:
#     n.append(i['final'])
# print("Min:", min(n), "Max:", max(n))
# print(n)
# for j in st:
#     if j['final'] == min(n):
#         print("Min:", j)
#     elif j['final'] == max(n):
#         print("Max:", j)







