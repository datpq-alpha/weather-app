import sqlite3

def create_table():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
    # Tạo bảng favorite_cities (lưu tên TP).
    # UNIQUE để đảm bảo không lưu trùng tên 1 thành phố 2 lần.
    c.execute('''
        CREATE TABLE IF NOT EXISTS favorite_cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()