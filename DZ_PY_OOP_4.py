# ================== > < >= <=
class Clock:
    __DAY = 86400  # секунд в одном дне

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")

        self.__secs = secs % self.__DAY

    def get_format_time(self):
        s = self.__secs % 60  # ____________секунды
        m = (self.__secs // 60) % 60  # _____минуты
        h = (self.__secs // 3600) % 24  # _____часы
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом данных \"Clock\"")

        return Clock(self.__secs + other.__secs)

    def __gt__(self, other):  # метод >
        return self.__secs > other.__secs

    def __lt__(self, other):  # метод <
        return self.__secs < other.__secs

    def __ge__(self, other):  # метод >=
        return self.__secs >= other.__secs

    def __le__(self, other):  # метод <=
        return self.__secs <= other.__secs


c1 = Clock(100)
c2 = Clock(200)
c3 = Clock(300)
print(c1.get_format_time())
print(c2.get_format_time())
print(c3.get_format_time())
print(c3 > c1)
print(c3 < c1)
print(c3 >= c1)
print(c3 <= c1)

# numpy
