import sqlite3 as lit

db = lit.connect('TelefonDefteri.db')

with db:

    newname = "updated name"
    user_id = 2

    cur = db.cursor()
    cur.execute('UPDATE Kullanicilar SET isim = ? WHERE id = ?', (newname, user_id))
    db.commit()
    print("Data Updated Successfully")
