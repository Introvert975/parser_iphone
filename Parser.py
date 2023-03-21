from bs4 import BeautifulSoup  # импортируем библиотеку BeautifulSoup
import requests  # импортируем библиотеку requests

def parse():
    price_list = []
    page_nums = int(input()) # Ввод кол-ва страниц
    for page in range(page_nums):

        url = 'https://kcentr.ru/catalog/smartfony/proizvoditel=apple/?page=' + str(page)
        try:
            page = requests.get(url)  # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
            status = page.status_code
            print(status)
            soup = BeautifulSoup(page.text, "html.parser")
        except:
            print("ConnectionError... page:"+str(page))
            return -1
        block = soup.findAll('meta', itemprop='price')
        for price in block:
            price_list.append(int(price.get('content')))  # получаем содержимое content и записываем его в список

    print("Найдено Iphone:" + str(len(price_list)))
    print("Максимальная цена:" + str(max(price_list)))
    print("Минимальная цена:" + str(min(price_list)))
    print("Cреднее цена:" + str(sum(price_list)//len(price_list)))
    return 0
