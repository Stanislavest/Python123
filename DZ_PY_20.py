# * * * * * * * * * * * * * * * * * * * * 1

with open('file1.txt', 'r') as a, open('file2.txt', 'r') as b, open('file3.txt', 'a+') as c:
    c.write('\n')
    c.writelines(a)
    c.write('\n')
    c.writelines(b)
f = open('file3.txt', 'r', encoding='utf-8')
print(f.read())

# * * * * * * * * * * * * * * * * * * * * 2

with open('file4.txt', 'r', encoding='utf-8') as d:
    reg = 0
    for line in d:
        slv = len(line.split(' '))
        smv = line.count('')-1
        print(f'{line} {smv} симв. {slv} сл.')
