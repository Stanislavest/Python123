import re
import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""

    def __init__(self, url):
        self.url = url

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        elements = self.html.find_all('div', class_='model-price-range')  # []
        prices = []
        for elem in elements:
            pr1 = elem.find_all('span')[0].text
            price_1 = re.sub(r"\D", "", pr1)
            pr2 = elem.find_all('span')[1].text
            price_2 = re.sub(r"\D", "", pr2)
            if price_2.isnumeric():  # содержит ли строка только цифры
                prices.append((int(price_1) + int(price_2)) / 2)
            else:
                prices.append(int(price_1))

        return sum(prices) / len(prices)

    def run(self):
        self.get_html()
        return self.parsing()


avg = []
for i in range(15):
    pars = Parser(f'https://www.e-katalog.ru/list/206/{i}/')
    avg.append(pars.run())
    # print(f'Средняя цена {round(sum(avg) / len(avg), 2)} руб')
    # print(avg)
print(f'Средняя цена {round(sum(avg) / len(avg), 2)} руб')