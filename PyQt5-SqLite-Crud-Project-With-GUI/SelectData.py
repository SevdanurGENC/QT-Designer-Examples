import sqlite3 as lit

db = lit.connect('TelefonDefteri.db')

with db:
    cur = db.cursor()
    selectquery = "SELECT * FROM Kullanicilar"
    cur.execute(selectquery)

    rows = cur.fetchall()

    for data in rows:
        print(data)
