import sqlite3
import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'weather.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

# 1. Thêm thành phố vào danh sách yêu thích
def add_city(city_name):
    try:
        with get_connection() as conn:
            conn.execute(
                'INSERT INTO favorite_cities (city_name) VALUES (?)',
                (city_name,)
            )
        return True
    except sqlite3.IntegrityError:
        return False
    except Exception as e:
        print('DB ERROR:',e)
        return False

# 2. Lấy danh sách tất cả thành phố đã lưu
def view_all_cities():
    with get_connection() as conn:
        return pd.read_sql_query(
            "SELECT * FROM favorite_cities",
            conn
        )

# 3. Xóa thành phố
def delete_city(city_name):
    with get_connection() as conn:
        conn.execute(
            'DELETE FROM favorite_cities WHERE city_name=?',
            (city_name,)
        )
