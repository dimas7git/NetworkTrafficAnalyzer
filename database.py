import sqlite3

class NetworkDatabase:
    def __init__(self, db_name='network_traffic.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS captured_traffic (
                src_ip TEXT,
                dst_ip TEXT,
                protocol TEXT,
                port INTEGER
            )
        ''')
        self.conn.commit()

    def insert_data(self, src_ip, dst_ip, protocol, port):
        self.cursor.execute('''
            INSERT INTO captured_traffic (src_ip, dst_ip, protocol, port)
            VALUES (?, ?, ?, ?)
        ''', (src_ip, dst_ip, protocol, port))
        self.conn.commit()

    def close(self):
        self.conn.close()
