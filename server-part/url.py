import string
import json
from random import sample
from datetime import datetime
from db_helper import DB_HELPER


url_error_tpl = 'URL Class error:\n\tmethod - {}\n\tdescription: {}'  # шаблон строки ошибки
token_length = 6  # длина генерируемого токена
char_alphabet = list(string.digits + string.ascii_letters)  # алфавит символов для генерации токенов (цифры + заглавные и строчные ASCII символы)


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
    
    def url_2_json(self) -> str:
        """
        Преобразование объекта URL в JSON

        Returns:
            json: объект в формате json
        """
        ex_data = {
            'id': self.id,
            'original_url': self.original_url,
            'short_token': self.short_token,
            'created': self.created,
            'active': self.active,
        }
        return json.dumps(ex_data)

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
            db = DB_HELPER()
            db.execute_non_query(query, params=(original_url, new_token, dt_created))
        except Exception as e:
            print(url_error_tpl.format('generate_new', e))

        res = URL(id=None, original_url=original_url, short_token=new_token, created=dt_created, active=1)

        return res
        