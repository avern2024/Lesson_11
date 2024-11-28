import requests


def response_site(url):
    # Выполнение GET-запроса информации с сайта
    response = requests.get(url)
    # Проверка успешности запроса
    if response.status_code == 200:
        # Вывод содержимого ответа в консоль
        print(response.text)
        print()
        # Возврат кодировки, используемой для декодирования содержимого ответа
        print(response.encoding)
        print()
        # Возврат заголовков ответа от сервера
        print(response.headers)
        print()
        # Возврат cookies, используемые для авторизации на сайте
        print(response.cookies)
    else:
        print(f'Error: {response.status_code}')


if __name__ == '__main__':
    response_site('https://novosibirsk.e2e4online.ru/')  # Замените на нужный вам URL
