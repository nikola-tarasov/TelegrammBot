import sqlite3 as sq




db = sq.connect('tg.db')

cur = db.cursor()

async def db_start():
        cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "tg_id INTEGER,"
                   "cart_id TEXT)")
        cur.execute("CREATE TABLE IF NOT EXISTS items("
                    "i_id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "name TEXT,"
                    "desc TEXT)")
        db.commit()
