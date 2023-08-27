import sqlite3

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(e)


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_product(conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_quantity_products(conn, change_quantity):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, change_quantity)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def change_price_products(conn, change_price):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, change_price)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_product(conn, deleted_id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (deleted_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_product(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_price_and_quantity(conn):
    try:
        sql = '''SELECT * FROM products WHERE price < 100 AND quantity > 5'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_search(conn, search_term):
    try:
        sql = '''SELECT * FROM products WHERE product_title LIKE ? '''
        cursor = conn.cursor()
        cursor.execute(sql, (search_term,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


database = r'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER (8) NOT NULL DEFAULT 0
)
'''

connection = create_connection(database)  # Cоздание БД
if connection is not None:
    print('Connected successfully')
    # create_table(connection, sql_create_products_table)  # Cоздание таблицы
    # create_product(connection, ("Жидкое мыло с запахом ванили", 99.99, 20)) # Cоздание товара 1
    # create_product(connection, ("Мыло детское", 60.99, 8)) # Cоздание товара 2
    # create_product(connection, ("Шампунь для волос", 250.99, 5)) # Cоздание товара 3
    # create_product(connection, ("Зубная паста 'Освежение дыхания'", 600.99, 90)) # Cоздание товара 4
    # create_product(connection, ("Средство для чистки стеко", 50.99, 6)) # Cоздание товара 5
    # create_product(connection, ("Крем для рук", 95.99, 2)) # Cоздание товара 6
    # create_product(connection, ("Моющее средство для посуды", 75.99, 11)) # Cоздание товара 7
    # create_product(connection, ("Масло для волос с аргановым маслом", 55.99, 8)) # Cоздание товара 8
    # create_product(connection, ("Детский порошок", 100.99, 3)) # Cоздание товара 9
    # create_product(connection, ("Зубная щетка для детей", 88.99, 1)) # Cоздание товара 10
    # change_quantity_products(connection, (50, 1))  # Функцию, которая меняет количество товара по id
    # change_price_products(connection, (1000.00, 5))  # Функцию, которая меняет цену товара по id
    # delete_product(connection, 10)  # Функцию, которая удаляет товар по id
    # select_all_product(connection)  # Функцию, которая бы выбирала все товары из БД и распечатывала бы их
    # select_products_price_and_quantity(connection)  # Функцию, которая бы выбирала из БД которые (>=<)
    # select_products_search(connection, '%([А-Яа-я], )*[Мм]ыло')
