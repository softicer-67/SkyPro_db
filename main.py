from settings import DB_PASS
import psycopg2
from psycopg2 import Error
from functions import *


def main():
    try:
        # Подключиться к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password=DB_PASS,
                                      host="127.0.0.1",
                                      port="5432",
                                      database="new_db")
        cursor = connection.cursor()

        while True:
            print('[1] Вывести все объявления\n'
                  '[2] Вывести объявления конкретного пользователя\n'
                  '[3] Вывести объявления в диапазоне цен, сортировка данных в порядке возрастания цены\n'
                  '[4] Вывести объявления для конкретного города\n'
                  '[5] Вывести информацию для определенного пользователя и цены\n'
                  '[0] - Выход\n')

            user_input = input('Выбрать вариант: ')
            match user_input:
                case '1':
                    get_ads(cursor)
                case '2':
                    get_user_ads(cursor)
                case '3':
                    get_sort(cursor)
                case '4':
                    get_city(cursor)
                case '5':
                    get_user_price(cursor)
                case _:
                    exit('Exit')

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


if __name__ == '__main__':
    main()
