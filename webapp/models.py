import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False

def get_auto_specifications(html):
    soup = BeautifulSoup(html, 'html.parser')
    # all_specific = soup.find(class_="b-model-specs").findAll(class_="bm-modelSpecsGroup")
    all_specific = soup.findAll(string=["Мощность", "Объем", "Расход"])
    all_specific = all_specific.find_all_next(class_="b-model-specs__text")
    print(all_specific)

if __name__ == "__main__":
        html = get_html("https://www.drom.ru/catalog/ford/focus/156523/")
        if html:
            get_auto_specifications(html)

