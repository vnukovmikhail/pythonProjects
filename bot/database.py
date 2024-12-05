import sqlite3 as sq

db = sq.connect('C:\\Users\\User\\Downloads\\pythonProjects-main\\pythonProjects-main\\bot\\tg.db')
cur = db.cursor()

async def start():
    cur.execute('CREATE TABLE IF NOT EXISTS users('
                'id INTEGER,'
                'kisses INTEGER DEFAULT 0)')
    db.commit()

async def kiss(user_id):
    user = cur.execute('SELECT * FROM users WHERE id  == {key}'.format(key=user_id)).fetchone()
    if not user:
        cur.execute('INSERT INTO users (id) VALUES ({key})'.format(key=user_id))

    cur.execute('UPDATE users SET (kisses) = kisses + 1 WHERE (id) = {key}'.format(key=user_id))
    db.commit()