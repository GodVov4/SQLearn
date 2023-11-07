import sqlite3

from prettytable import PrettyTable


def select(script_number):
    with open(f'query_{script_number}.sql') as f:
        sql = f.read()

    with sqlite3.connect('university.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == '__main__':
    for i in range(1, 13):
        table = PrettyTable(title=f'Вибірка №{i}', header=False)
        table.add_rows(select(i))
        print(table)

