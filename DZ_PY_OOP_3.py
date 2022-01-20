class Student:
    def __init__(self, name):
        self.name = name


    class Computer:
        def __init__(self, vender, cpu, ddr, a):
            self.vender = vender
            self.cpu = cpu
            self.ddr = ddr
            self.a = a

        def print_all(self):
            n = self.a
            print(n.name, '=>', self.vender, self.cpu, self.ddr)


a = Student("Roman")
pc2 = a.Computer("HP", "i7 8700", "16Gb", a)
pc2.print_all()
a = Student("Vladimir")
pc2 = a.Computer("Asus", "i9 12900", "32Gb", a)
pc2.print_all()

# код с последующего урока
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.bd = self.Comp()
#
#     def info(self):
#         f = self.bd.ret()
#         print(f"{self.name} => {str(f)[1:-1]}")
#
#     class Comp:
#         def __init__(self):
#             self.model = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def ret(self):
#             return self.model, self.cpu, self.ram
#
#
# pc1 = Student("Иван")
# pc1.info()

