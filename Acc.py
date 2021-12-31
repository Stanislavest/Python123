class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_euro = "EURO"

    def __init__(self, surname="Д", nam="#123", persent= 0.0, value = 0):
        self.__surname = surname # фамилия владельца
        self.__nam = nam # номер счета
        self.__persent = persent # процент начисления
        self.__value = value # сумма в рублях

    def __del__(self):
        return (f'Счет {self.__nam} принадлежащий {self.__surname} был закрыт')

    def set_surname(self, surname):
        self.__surname = surname

    def set_nam(self, nam):
        self.__nam = nam

    def set_persent(self, persent):
        self.__persent = persent

    def set_value(self, value):
        self.__value = value

    def get_surname(self):
        return self.__surname

    def get_nam(self):
        return self.__nam

    def get_persent(self):
        return self.__persent

    def get_value(self):
        return self.__value

    @classmethod
    def set_usd_rate(cls, rate):
        cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate):
        cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        return usd_val

    def convert_to_euro(self):
        return Account.convert(self.__value, Account.rate_euro)

    def add_persent(self):
        self.__value +=self.__value *self.__persent
        return self.__value

    def withdraw_money(self, val):
        if val >self.__value:
            return f"К сожалению у вас нет такой суммы {val} {Account.suffix}"
        else:
            self.__value-=val
            return (f"{val} {Account.suffix} были успешно сняты!")

    def add_money(self, val):
        self.__value +=val
        return (f"{val} {Account.suffix} были успешно добавлены!")

acc = Account()
acc.set_surname("Долгих")
acc.set_nam("#12345")
acc.set_persent(0.03)
acc.set_value(1000)
print("Счет ", acc.get_nam(), " принадлежащий ", acc.get_surname(), " был открыт")
print("*"*50)
print("Информация о счете\n", "-"*20)
print(acc.get_nam(), "\nВладелец: ", acc.get_surname(), "\nТекущий балланс: ", acc.get_value(), Account.suffix, "\nПрценты: ", acc.get_persent()*100, "%")
print("\nСостояние счета: ", acc.convert_to_usd(), Account.suffix_usd)
print("Состояние счета: ", acc.convert_to_euro(), Account.suffix_euro)
print("\nПроценты были успешно начислены!", "\nТекущий балланс: ", acc.add_persent(), Account.suffix)
acc1 = acc.withdraw_money(3000)
print("\n", acc1, "\nТекущий балланс: ", acc.get_value(), Account.suffix)
acc1 = acc.withdraw_money(100)
print("\n", acc1, "\nТекущий балланс: ", acc.get_value(), Account.suffix)
acc2 = acc.add_money(5000)
print("\n", acc2, "\nТекущий балланс: ", acc.get_value(), Account.suffix)
acc.set_surname("Дюма")
acc.set_persent(0.05)
print("\n", acc.get_persent()*100, "%", "были успешно начислены!", "\nТекущий балланс: ", acc.add_persent(), Account.suffix)
print("\nИнформация о счете", acc.get_nam(), "\nВладелец: ", acc.get_surname(), "\nТекущий балланс: ", acc.get_value(), Account.suffix, "\nПрценты: ", acc.get_persent()*100, "%")
print("*"*50, "\n",acc.__del__())