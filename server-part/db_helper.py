import sqlite3


# configure db file
db_name = 'url_app_database.db'


class DB_HELPER:
    """
    Класс для работы с базой данных SQLite приложения URL_Shortener
    """

    def __init__(self, data_base: str = db_name):
        self.data_base = data_base  # название базы присваиваем атрибуту data_base класса DB_HELPER

    def db_create(self):
        """
        Создание БД в случае ее отсутствия
        """
        with sqlite3.connect(self.data_base) as conn:
            cursor = conn.cursor()  # инициируем курсор для взаимодействия с базой данных

            with open('./queries/generate_table.sql', 'r', encoding='utf-8') as query_file:
                query = query_file.read()  # читаем запрос SQL из файла

            cursor.execute(query)  # выполняем запрос
            conn.commit()

    def execute_non_query(self, query: str, params=()):
        """
        Метод для выполнения SQL запроса без возвращения результатов запроса

        Args:
            query (str): текст SQL запроса
            params (tuple, optional): параметры для выполнения запроса.
        """
        with sqlite3.connect(self.data_base) as conn:
            cursor = conn.cursor()  # инициируем курсор для взаимодействия с базой данных
            cursor.execute(query, params)  # выполняем запрос с заданными параметрами
            conn.commit()

    def execute_query(self, query: str, params=()):
        """
        Метод для выполнения SQL запроса, возвращающего результат запроса

        Args:
            query (str): текст SQL запроса
            params (tuple, optional): параметры для выполнения запроса.
        """
        with sqlite3.connect(self.data_base) as conn:
            cursor = conn.cursor()  # инициируем курсор для взаимодействия с базой данных
            cursor.execute(query, params)  # выполняем запрос с заданными параметрами
            conn.commit()
            result = cursor.fetchall()
            return result

