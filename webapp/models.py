import requests
from bs4 import BeautifulSoup


list_of_interest = [
'Название марки',
'Название модели',
'Название комплектации',
'Период выпуска',
'Тип привода',
'Тип кузова',
'Тип трансмиссии',
'Объем двигателя, куб.см',
'Страна сборки',
'Марка двигателя',
'Максимальная мощность, л.с. (кВт) при об./мин.',
'Максимальный крутящий момент, Н*м (кг*м) при об./мин.',
'Тип двигателя',
'Используемое топливо',
'Расход топлива в городском цикле, л/100 км',
'Расход топлива за городом, л/100 км',
'Расход топлива в смешанном цикле, л/100 км',
'Передняя подвеска',
'Задняя подвеска',
# 'Шины',
'Передние колеса',
'Задние колеса',
# 'Микроклимат салона',
'Кондиционер',
# 'Салонный фильтр',
# 'Климат-контроль',
# 'Средняя стоимость'
]


def get_html(url):
    try:
        result = requests.get(url)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_auto_specifications(html):

    characteristics = {}
    
    soup = BeautifulSoup(html, 'html.parser')
    path_line = soup.find_all(class_="b-breadcrumbs__item")

    characteristics['Название марки'] = path_line[2].text
    characteristics['Название модели'] = path_line[3].text

    table1 = soup.find_all(class_='b-table b-table_mobile-size-s b-table_text-size-s b-table_text-left')[0]

    row_class_ = 'b-table__row b-table__row_padding_l-r-size-xs '+\
               'b-table__row_cols_2 b-table__row_border_bottom b-table__row_border_light '+\
               'b-table__row_padding_t-b-size-s b-table_align_top'

    for row in table1.find_all('tr', class_=row_class_):
        key = row.find_all('td')[0].text
        value = row.find_all('td')[1].text
        if key in ['Передние колеса','Задние колеса']:
            value = value.split('Отзывы')[0]
        characteristics[key] = value.strip('\n ')
    
    return {key:value for key, value in characteristics.items() if key in list_of_interest}


if __name__ == "__main__":

    html = get_html("https://www.drom.ru/catalog/ford/focus/156523/")

    if html:
        characteristics = get_auto_specifications(html)
