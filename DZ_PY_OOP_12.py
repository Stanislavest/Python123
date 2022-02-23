import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('plugins111.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\r')
        writer.writerow(data)  # ((data['name'], data['url'], data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, "lxml")

    p1 = soup.find("div", class_="row no-gutters")
    # write_csv(p1.text)  # не записывает в файл, но данные выводит (текст из блоков)
    for i in p1:
        print(i.text)

    # return p1

def main():
    url = "https://www.4pc.by/"
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()
