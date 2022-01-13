import math
from abc import ABC, abstractmethod

# class Koren
#     def __init__(self, x=0):
#         self.x = x



class Chess(ABC):  # Абстрактный класс
    def draw(self):
        print("Нарисовал шахматную фигуру")

    @abstractmethod
    def move(self):  # Абстрактный метод
        print("Метод move() в базовом классе")

class Queen(Chess):
    def move(self):
        super().move()
        print("Ферзь перемещен на е2е4")


q = Queen()
q.draw()
q.move()
