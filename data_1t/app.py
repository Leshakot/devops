import psycopg2
import os
import time

# Подключение к базе данных PostgreSQL с повторными попытками
def connect_to_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=os.getenv("POSTGRES_DB"),
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host="db"
            )
            return conn
        except Exception as e:
            print(f"ошибка: {e}")
            time.sleep(5)

def query_min_max_age():
    conn = connect_to_db()  # Подключаемся к базе данных с повторными попытками
    cur = conn.cursor()
    cur.execute("SELECT MIN(age), MAX(age) FROM test_table WHERE LENGTH(name) < 6;")
    result = cur.fetchone()
    print(f"Минимальный возраст: {result[0]}, Максимальный возраст: {result[1]}")
    cur.close()
    conn.close()

if __name__ == "__main__":
    query_min_max_age()

