import sqlite3 as lit

def main():
    try:
        db = lit.connect('myemployee.db')
        cur = db.cursor()
        tablequery = "CREATE TABLE users (id INT, name TEXT, email TEXT)"

        cur.execute(tablequery)
        print("Table Created Succesfully")

    except lit.Error as e:
        print("Unable To Create Table")

    finally:
        db.close()
        
if __name__ == "__main__":
    main()