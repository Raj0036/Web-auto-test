
import sqlite3, time, json
class Store:
    def __init__(self, path='aas_results.sqlite'):
        self.path = path
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self._init_db()
    def _init_db(self):
        cur = self.conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS findings (id INTEGER PRIMARY KEY, ts REAL, target TEXT, name TEXT, details TEXT)''')
        self.conn.commit()
    def save(self, target, name, details):
        cur = self.conn.cursor()
        cur.execute('INSERT INTO findings (ts,target,name,details) VALUES (?,?,?,?)', (time.time(), target, name, json.dumps(details)))
        self.conn.commit()
