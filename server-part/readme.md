# СЕРВЕРНАЯ ЧАСТЬ URL SHORTENER

## структура серверной части

- [app.py](app.py) - основной файл логики Flask приложения;
- [url.py](url.py) - класс URL приложения;
- [db_helper.py](db_helper.py) - класс для работы с SQLite базой данных;
- [utils.py](utils.py) - файл с важными функциями;
- [requirements.txt](requirements.txt) - библиотеки для формирования окружения python;
- [perplexity-review.md](perplexity-review.md) - отзыв о структуре серверной части от Perplexity.ai

## порядок запуска

1. Сформировать виртуальное окружение для приложения и скачать необходимые для работы библиотеки:
    ```
    $ python -m venv env
    $ env\Scripts\activate
    $ pip install -r requirements.txt
    ```
2. В [конфигурационном файле](config.py) указать HOST, PORT на которых предполагается запуск приложения для корректной работы формирования QR кодов.
3. Запуск проекта с выбранными параметрами HOST и PORT: `$ python -m flask run -h HOST -p PORT`.