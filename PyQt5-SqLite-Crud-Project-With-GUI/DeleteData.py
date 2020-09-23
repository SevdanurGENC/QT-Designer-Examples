import sqlite3 as lit

db = lit.connect('TelefonDefteri.db')

with db:

    newname = "updated name"
    user_id = 1

    cur = db.cursor()
    cur.execute('DELETE FROM Kullanicilar WHERE id = ?  ', (user_id,) )
    db.commit()
    print("Data Deleted Successfully")
