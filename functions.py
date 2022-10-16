
def get_ads(cursor):
    postgreSQL = "select * from new"

    cursor.execute(postgreSQL)
    shop = cursor.fetchall()

    print("Вывод каждой строки и ее столбцов")
    for row in shop:
        print("-" * 100)
        print("Id: ", row[0], )
        print("Товар: ", row[1])
        print("Описание: ", row[4])
        print("Цена: ", row[3], '\n')


def get_user_ads(cursor):
    user_input = input("Введи имя: ")
    postgreSQL = f"SELECT * FROM new JOIN author on author.c1 = new.c3 where author.c2 = '{user_input}'"

    cursor.execute(postgreSQL)
    shop = cursor.fetchall()

    print("Вывод каждой строки и ее столбцов")
    for row in shop:
        # if row[8] == user_input:
        print("-" * 100)
        print("Id: ", row[0], )
        print("Товар: ", row[1])
        print("Автор: ", row[8])
        print("Цена: ", row[3], '\n')


def get_sort(cursor):
    print("Введи интервал цен")
    min_input = int(input("От: "))
    max_input = int(input("До: "))

    postgreSQL = "select * from new order by c4"

    cursor.execute(postgreSQL)
    shop = cursor.fetchall()

    print("Вывод каждой строки и ее столбцов")
    for row in shop:
        if min_input <= row[3] <= max_input:
            print("-" * 100)
            print("Id: ", row[0])
            print("Товар: ", row[1])
            print("Описание: ", row[4])
            print("Цена: ", row[3], '\n')


def get_city(cursor):
    user_input = input("Введи город: ")

    postgreSQL = f"SELECT * FROM new JOIN address on address.c1 = new.c3 where address.c2 like '{user_input}%'"

    cursor.execute(postgreSQL)
    shop = cursor.fetchall()

    print("Вывод каждой строки и ее столбцов")
    for row in shop:
        # if row[8] == user_input:
        print("-" * 100)
        print("Id: ", row[0], )
        print("Товар: ", row[1])
        print("Автор: ", row[8])
        print("Цена: ", row[3], '\n')


def get_user_price(cursor):
    user_input = input("Введи имя: ")

    postgreSQL = f"SELECT * FROM new JOIN author on author.c1 = new.c3 where author.c2 = '{user_input}'"

    cursor.execute(postgreSQL)
    shop = cursor.fetchall()

    print("Вывод каждой строки и ее столбцов")
    for row in shop:
        print("-" * 100)
        print("Id: ", row[0], )
        print("Товар: ", row[1])
        print("Автор: ", row[8])
        print("Цена: ", row[3], '\n')
