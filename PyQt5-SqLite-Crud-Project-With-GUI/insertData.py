import sqlite3 as lit

myuser = (
# Kullanicilar (id INT, isim TEXT, soyisim TEXT, sehir TEXT, telefon TEXT, email TEXT)
    (1, 'Sevdanur', 'GENC', 'Kastamonu', '05557777777', 'sgenc@kastamonu.edu.tr'),
    (2, 'Huseyin', 'Sahin', 'Bursa', '05448888888', 'hsahin@gmail.com')    
)

db = lit.connect('TelefonDefteri.db')

with db:
    cur = db.cursor()
    cur.executemany('INSERT INTO Kullanicilar VALUES (?,?,?,?,?,?)', myuser)

    print("Data Inserted Successfully")