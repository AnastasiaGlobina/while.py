#Приложение БАНК для отслеживания накапливаемых на счетах клиентов банка
#сумм. Таблица Клиент должна содержать следующую информацию: Код клиента,
#Клиент (Ф.И.О.), Периодический платеж, Годовой %, Срок вклада, Пластиковая карта
#(логическое поле), Конечная сумма.
import sqlite3 as sq

with sq.connect('Tour_Agency.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Tourist")
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Tourist (
            client_id INTEGER PRIMARY KEY,
            client_name TEXT NOT NULL,
            phone TEXT NOT NULL,
            country_name TEXT NOT NULL,
            region TEXT NOT NULL,
            trip_duration INTEGER NOT NULL,
            tour_cost REAL NOT NULL
        )
    ''')

info = [
    (1, 'Иванов', '123-456-7890', 'Италия', 'Тоскана', 7, 50000.0),
    (2, 'Петров', '987-654-3210', 'Франция', 'Париж', 5, 40000.0),
    (3, 'Сидоров', '456-789-0123', 'Греция', 'Афины', 10, 60000.0)
]

with sq.connect('Tour_Agency.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO Tourist VALUES (?, ?, ?, ?, ?, ?, ?)", info)

with sq.connect('Tour_Agency.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Tourist WHERE tour_cost > 40000")
    result = cur.fetchall()

for tourist in result:
    print(f"Код клиента: {tourist[0]}, Клиент: {tourist[1]}, Телефон: {tourist[2]}, Название страны: {tourist[3]}, Регион: {tourist[4]}, Продолжительность поездки: {tourist[5]} дней, Стоимость путевки: {tourist[6]} руб.")