# __________________________________________15.02.2022
# from bs4 import BeautifulSoup
# import re
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding='utf-8').read()
# soup = BeautifulSoup(f, 'html.parser')
# row = soup.find_all("div", {"data-set": "salary"})  # .text
# for i in row:
#     get_salary(i.text)
#
#
# # print(row)
#
# # def get_copywriter(tag):
# #     whois = tag.find('div', class_="whois")
# #     if "Copywriter" in whois:
# #         return tag
# #     return None
# #
# #
# # f = open('index.html', encoding='utf-8').read()
# # soup = BeautifulSoup(f, 'html.parser')
# # copywriter = []
# # row = soup.find_all("div", class_="row")
# # for i in row:
# #     cw = get_copywriter(i)
# #     if cw:
# #         copywriter.append(cw)
# # print(row)
#
#
# # row = soup.find("div", class_="name")  # первый найденный элемент
# # row = soup.find_all("div", class_="row")  # все найденные элементы
# # row = soup.find_all("div", class_="row")[1].find("div", class_="links")  # элемент
# # row = soup.find("div", {"data-set": "salary"})
# # print(row)
# # alena = soup.find("div", text="Alena").parent.parent
# # alena = soup.find("div", text="Alena").find_parent(class_="row")
# # print(alena)
# # row = soup.find("div", id="whois3")  # найти элемент
# # row = soup.find("div", id="whois3").find_next_sibling()  # найти следующий элемент
# # row = soup.find("div", id="whois3").find_previous_sibling()  # найти следующий предыдущий элемент
# # print(row)


# import requests
#
# r = requests.get("https://ru.wordpress.org/")
# # print(r.text)  # html разметка
# # print(r.content)
# # print(r.status_code)
# # print(r.headers)
# # print(r.headers['content-type'])

# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# ====================================================================
# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r'\D+', '', s)
#     return res
#
# def write_csv(data):
#     with open('plugins.csv', 'a', encoding='utf-8') as f:
#         writer = csv.writer(f, lineterminator='\r')
#         writer.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     s = soup.find_all("section", class_="plugin-section")[1]
#     plugins = s.find_all('article')
#     for plugin in plugins:
#         name = plugin.find('h3').text
#         url = plugin.find('h3').find('a').get('href')
#         rating = plugin.find('span', class_='rating-count').find('a').text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#     # return plugins
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# ==================================================================== 17.02.2022

# import requests
# from bs4 import BeautifulSoup
# import re
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("plugins1.csv", "a", encoding='utf-8') as f:
#         writer = csv.writer(f, lineterminator="\r")
#         writer.writerow((data['name'],
#                          data['url'],
#                          data['snippet'],
#                          data['active'],
#                          data['cy']))
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#         try:
#             url = el.find("h3").find('a').get('href')
#         except ValueError:
#             url = ""
#         try:
#             snippet = el.find("div", class_="entry-excerpt").text
#         except ValueError:
#             snippet = ""
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#         try:
#             c = el.find("span", class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 26):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# ========================================================= "подход через классы" PARSE.PY

# import requests
# from bs4 import BeautifulSoup
#
# from parse import Parser
#
#
# def main():
#     pars = Parser("https://www.ixbt.com/live/index/type/news/", "news.txt")
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# ================================================================================== MVC
# Model - модель
# Viev - вид или представление
# Controller - контроллер

# ================================================================ DZ:

from bs4 import BeautifulSoup
import requests
import re


class Parser:
    html = ""

    def __init__(self, url):
        self.url = url

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        elements = self.html.find_all("div", class_="model-price-range")  # []
        prices = []
        for element in elements:
            pr1 = element.find_all('span')[0].text
            price_1 = re.sub(r"\D", "", pr1)
            pr2 = element.find_all('span')[1].text
            price_2 = re.sub(r"\D", "", pr2)
            if price_2.isnumeric():  # содержит ли строка только числа
                prices.append((int(price_1) + int(price_2)) / 2)
            else:
                prices.append(int(price_1))
        return sum(prices) / len(prices)

    def run(self):
        self.get_html()
        return self.parsing()


av = []
for i in range(18):
    pars = Parser(f"https://www.e-katalog.ru/list/206/{i}/")
    av.append(pars.run())

print(av)
print(f"Средняя цена: {round(sum(av) / len(av), 2)} руб.")













