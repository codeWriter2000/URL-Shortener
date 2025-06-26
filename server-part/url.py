import string
import json
from random import sample
from datetime import datetime
from utils import get_origin
from db_helper import DB_HELPER


url_error_tpl = 'URL Class error:\n\tmethod -> {}\n\tdescription -> {}'  # шаблон строки ошибки
token_length = 6  # длина генерируемого токена
approved_url_cnt = [5, 10, 15, 30]  # число доступных для одновременного вывода ссылок
char_alphabet = list(string.digits + string.ascii_letters)  # алфавит символов для генерации токенов (цифры + заглавные и строчные ASCII символы)


db = DB_HELPER()

db.db_create()  # создали основную таблицу

db.log_create()  # создали таблицу для логирования


class URL:
    """
    Класс для работы с объектами приложения URL_Shortener
    """

    def __init__(self, id: int, original_url: str, short_token: str, created: str, active: int):
        self.id = id  # первичный ключ URL в таблицы БД приложения
        self.original_url = original_url  # оригинальная строка URL, переданная пользователем
        self.short_token = short_token  # короткая ссылка, сгенерированная в приложении
        self.created = created  # момент создания (ISO-datetime)
        self.active = active  # статус короткого токена

    def __repr__(self):
        # Более информативное представление для отладки
        return f"<URL id={self.id}, original_url={self.original_url}, short_token='{self.short_token}', created={self.created}, active={self.active}>"
    
    def url_2_dict(self) -> dict:
        """
        Преобразование объекта URL в JSON

        Returns:
            dict: объект в формате словаря
        """
        ex_data = {
            'id': self.id,
            'original_url': self.original_url,
            'short_token': self.short_token,
            'created': self.created,
            'active': self.active,
        }
        return ex_data

    @staticmethod
    def generate_new(original_url: str) -> 'URL':
        """
        Метод класса URL для создания объекта приложения URL_Shortener

        Args:
            original_url (str): оригинальная строка URL, переданная пользователем

        Returns:
            URL: объект класса URL
        """
        dt_created = datetime.now().isoformat()  # дата и время генерации в формате ISO
        new_token = ''.join(sample(char_alphabet, token_length))  # короткий токен

        with open('./queries/add_new_url.sql', 'r', encoding='utf-8') as query_file:
            query = query_file.read()

        try:
            db.execute_non_query(query, params=(original_url, new_token, dt_created))
        except Exception as e:
            print(url_error_tpl.format('generate_new', e))

        res = URL(id=None, original_url=original_url, short_token=new_token, created=dt_created, active=1)

        return res

    @staticmethod
    def get_original_by_token(short_token: str) -> str:
        """
        Метод для получения оригинальной ссылки из БД проекта

        Args:
            short_token (str): уникальный короткий токен, присвоенный данной ссылке и хранимый в БД

        Returns:
            str: оригинальная ссылка на ресурс
        """
        original_url = ''  # строка URL оригинального ресурса (по умолчанию пустая)
        
        with open('./queries/get_original_url.sql', 'r', encoding='utf-8') as query_file:
            query = query_file.read()

        try:
            res = db.execute_query(query, params=(short_token,))
        except Exception as e:
            print(url_error_tpl.format('get_original_by_token', e))

        if res:
            original_url = res[0][0]

        return original_url

    @staticmethod
    def weekly_deactivate() -> bool:
        """
        Метод для деактивации коротких токенов по истечении срока

        Returns:
            bool: статус выполнения запроса
        """
        flag = False

        with open('./queries/periodic_deactivate.sql', 'r', encoding='utf-8') as query_file:
            query = query_file.read()

        try:
            db.execute_non_query(query, params=())
            flag = True
        except Exception as e:
            print(url_error_tpl.format('weekly_deactivate', e))

        return flag

    @staticmethod
    def get_nearest_urls(count: int) -> json:
        """
        Метод для получения определенного пользователем количества недавно добавленных URL

        Args:
            count (int): количество URL, которое необходимо вывести

        Returns:
            json: результат выводится в виде json строки
        """
        out_data = []

        if count in approved_url_cnt:

            with open('./queries/get_top_of_nearest_urls.sql', 'r', encoding='utf-8') as query_file:
                query = query_file.read()

            try:
                res = db.execute_query(query, params=(count,))
            except Exception as e:
                print(url_error_tpl.format('get_nearest_urls', e))

        if res:
            for r in res:
                url_str, created = r
                out_data.append({
                    'original_url': url_str,
                    'created': created,
                })

        return json.dumps(out_data)

    @staticmethod
    def log_url_data(url_str: str) -> None:
        d_time = datetime.now().isoformat()  # дата и время посещения
        
        with open('./queries/log_url.sql', 'r', encoding='utf-8') as query_file:
            query = query_file.read()

        try:
            db.execute_non_query(query, params=(url_str, d_time))
        except Exception as e:
            print(url_error_tpl.format('log_url_data', e))

    @staticmethod
    def distinct_origins() -> dict:
        """
        Получение всех ссылок из базы для подсчета уникальных интернет ресурсов

        Returns:
            dict: возвращает словарь словарей ключ - ресурс, значение - число сформированных токенов на этот ресурс
        """
        ex_data = {}

        with open('./queries/get_all_urls.sql', 'r', encoding='utf-8') as query_file:
            query = query_file.read()

        try:
            res = db.execute_query(query, params=())
        except Exception as e:
            print(url_error_tpl.format('distinct_origins', e))

        if res:
            work_with = list(map(lambda x: x[0], res))
            work_with = list(map(get_origin, work_with))

            for _ in work_with:
                ex_data[_] = 1 if _ not in ex_data.keys() else (ex_data[_] + 1)

        return ex_data

    @staticmethod
    def origin_statistic_by_logs() -> dict:
        """
        Получение всех ссылок из таблицы с логами для подсчета  посещения уникальных интернет ресурсов

        Returns:
            dict: возвращает словарь словарей ключ - ресурс, значение - число сформированных токенов на этот ресурс
        """
        ex_data = {}

        with open('./queries/get_origins_from_logs.sql', 'r', encoding='utf-8') as query_file:
            query = query_file.read()

        try:
            res = db.execute_query(query, params=())
        except Exception as e:
            print(url_error_tpl.format('origin_statistic_by_logs', e))

        if res:
            work_with = list(map(lambda x: x[0], res))
            work_with = list(map(get_origin, work_with))

            for _ in work_with:
                ex_data[_] = 1 if _ not in ex_data.keys() else (ex_data[_] + 1)

        return ex_data
