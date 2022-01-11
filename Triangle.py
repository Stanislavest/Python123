class Pair:
    def __init__(self, A, B):
        self.A = A
        self.B = B

    def izm_A(self, val_A):
        self.A = val_A

    def izm_B(self, val_B):
        self.B = val_B

    def print_info(self):
        print(f'\nСумма: {self.A+self.B} \nПроизведение:{self.A*self.B}')


class Triangle(Pair):
    def __init__(self, A, B):
        super().__init__(A, B)

    def info_abc(self):
        res3 = (self.A ** 2 + self.B ** 2) ** 0.5
        print(f'Гипотенуза {round(res3,2)}')
        print(f'Прямоугольный треугольник ABC: {self.A,self.B,round(res3,2)}')
        print(f'Площадь ABC: {self.A*self.B*0.5}')


abc = Triangle(5, 8)
abc.info_abc()
abc.print_info()

abc.izm_A(10)
abc.izm_B(20)
print()
abc.info_abc()
abc.print_info()