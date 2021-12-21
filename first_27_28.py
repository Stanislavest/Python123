# ************************** 21.12.2021 *** Задача
class Account:
    rate_usd = 0.013
    rate_eur = 0.011
    suffix = "RUB"
    suffix_usd = "USD"
    suffix_eur = "EUR"

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname
        self.num = num
        self.percent = percent
        self.value = value
        print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
    @classmethod
    def set_usd_rate(cls, rate):  # редактировать курс Руб по отн. к $
        cls.rate_usd = rate

    @classmethod
    def set_eur_rate(cls, rate):  # редактировать курс Руб по отн. к Euro
        cls.rate_eur = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname):  # смена владельца счета
        self.surname = surname

    def convert_to_usd(self):  # перевод в $
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):  # перевод в $
        eur_val = Account.convert(self.value, Account.rate_eur)
        print(f'Состояние счета: {eur_val} {Account.suffix_eur}')

    def add_percents(self):  # начисление процентов
        self.value += self.value * self.percent
        print("Проценты были успешно начислены!")
        self.print_balance()

    def withdraw_money(self, val):  # снятие заданной суммы
        if val > self.value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):  # добавление денег на счет
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):  # вывод инф-ии о счете
        print("Информация о счете:")
        print("-" * 20)
        print(f'#{self.num}')
        print(f'Владелец: {self.surname}')
        # print(f'Текущий баланс: {self.value}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print("-" * 20)


acc = Account('Долгих', 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_eur()
Account.set_usd_rate(2)
Account.set_eur_rate(3)
print()
acc.convert_to_usd()
acc.convert_to_eur()
print()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_percents()
acc.withdraw_money(3000)
acc.withdraw_money(100)
acc.add_money(5000)
acc.withdraw_money(3000)
print()
