#     * * * * *     * * * * *     * * * * *     1

f = open("DZ_19_1.txt", "w")
f.write("Замена строки в текстовом файле;\nизменить строку"
        " в списке;\nзаписать список в файл;\n")
f.close()
pos = int(input("pos = "))
f = open("DZ_19_1.txt", "r")
r = f.readlines()
for i in range(len(r)):
    r[pos] = ""
f.close()
f = open("DZ_19_1.txt", "w")
f.writelines(r)
f.close()

#     * * * * *     * * * * *     * * * * *     2

# f = open("DZ_19_2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку"
#         " в списке;\nзаписать список в файл;\n")
# f.close()
# pos1 = int(input("pos1 = "))
# pos2 = int(input("pos2 = "))
# f = open("DZ_19_2.txt", "r")
# r = f.readlines()
# a = r[pos1]
# r[pos1] = r[pos2]
# r[pos2] = a
# f.close()
# f = open("DZ_19_2.txt", "w")
# f.writelines(r)
# f.close()

#     * * * * *     * * * * *     * * * * *     3

# f = open("DZ_19_3.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку"
#         " в списке;\nзаписать список в файл;\n")
# f.close()
# f = open("DZ_19_3.txt", "r")
# r = f.readlines()
# rev = reversed(r)
# f.close()
# f = open("DZ_19_3.txt", "w")
# f.writelines(rev)
# f.close()
