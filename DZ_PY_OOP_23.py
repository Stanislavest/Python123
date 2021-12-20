class Temp:
    count = 0

    def check_value(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    @staticmethod
    def far_in_cel(x):
        if Temp.check_value(x):
            Temp.count += 1
            return (x - 32) * 5 / 9
        else:
            raise ValueError("Неправильный формат")

    @staticmethod
    def cel_in_far(x):
        if Temp.check_value(x):
            Temp.count += 1
            return (x * 9 / 5) + 32
        else:
            raise ValueError("Неправильный формат")

    @staticmethod
    def count_izm():
        return Temp.count


t = Temp
print(round(t.far_in_cel(97.9), 1))
print(round(t.cel_in_far(36.6), 1))
