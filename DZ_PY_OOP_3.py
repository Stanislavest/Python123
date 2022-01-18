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



