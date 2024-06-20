import sqlite3


def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()


def add_products():
    products = [
        ("Product 1", 99.99, 10),
        ("Product 2", 49.99, 20),
        ("Product 3", 29.99, 30),
        ("Product 4", 19.99, 40),
        ("Product 5", 9.99, 50),
        ("Product 6", 199.99, 5),
        ("Product 7", 299.99, 2),
        ("Product 8", 399.99, 3),
        ("Product 9", 89.99, 15),
        ("Product 10", 79.99, 25),
        ("Product 11", 69.99, 35),
        ("Product 12", 59.99, 45),
        ("Product 13", 49.99, 55),
        ("Product 14", 39.99, 65),
        ("Product 15", 29.99, 75),
    ]

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products')

    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()


def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE products 
        SET quantity = ? 
        WHERE id = ?
    ''', (new_quantity, product_id))

    conn.commit()
    conn.close()


def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE products 
        SET price = ? 
        WHERE id = ?
    ''', (new_price, product_id))

    conn.commit()
    conn.close()


def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM products 
        WHERE id = ?
    ''', (product_id,))

    conn.commit()
    conn.close()


def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    conn.close()

    for product in products:
        print(product)


def get_products_below_price_and_above_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM products 
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()

    conn.close()

    for product in products:
        print(product)


def search_products_by_title(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM products 
        WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    products = cursor.fetchall()

    conn.close()

    for product in products:
        print(product)


if __name__ == "__main__":
    create_database()
    add_products()

    update_quantity(1, 50)
    update_quantity(2, 60)

    update_price(1, 150.0)
    update_price(2, 250.0)

    delete_product(15)

    print("All products:")
    get_all_products()

    print("\nProducts below price 100 and above quantity 5:")
    get_products_below_price_and_above_quantity(100, 5)

    print("\nProducts with title containing 'мыло':")
    search_products_by_title("мыло")
