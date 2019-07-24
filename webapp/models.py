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
    all_specific = soup.findAll(class_="b-model-specs__label")

    characteristics = {}
    
    for tag in soup.find_all(class_="bm-modelSpecsGroup"):
        label = tag.find(class_="b-model-specs__label").text
        value = tag.find(class_="b-model-specs__text").text.strip()
        characteristics[label] = value
    
    # print(characteristics['Объем'])
    return characteristics


def process_raw_characteristics(raw_characteristics):
    raw_characteristics =   {'Передние шины': '195/65 R15', 'Задние шины': '195/65 R15', 'Объем': '1.4 л', 'Мощность': '80 л.с.', 'Расход': '6,6 л', 'Тип топлива': 'Бензин', 'Трансмиссия': 'МКПП', 'Привод': 'Передний (FF)', 'Кол-во мест': '5 мест', 'Кол-во дверей': '3 двери', 'Клиренс': '155 мм', 'Объем багажника': '385 л'}    
    
    processed_characteristics = {}

    for charact in raw_characteristics:
        raw_characteristics['volume'] = raw_characteristics.pop('Объем')
        raw_characteristics['power'] = raw_characteristics.pop('Мощность')
        raw_characteristics['consumption'] = raw_characteristics.pop('Расход')
        print(raw_characteristics)

        
    # processed_characteristics = {'volume': 1.4, 'power': 6.6}
    # return processed_characteristics

if __name__ == "__main__":
    html = get_html("https://www.drom.ru/catalog/ford/focus/156523/")
    if html:
        get_auto_specifications(html)


# dictionary[new_key] = dictionary.pop(old_key)