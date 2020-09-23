import sqlite3 as lit

def main():
    try: 
        db = lit.connect('TelefonDefteri.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE Kullanicilar (id INT, isim TEXT, soyisim TEXT, sehir TEXT, telefon TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Table")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()