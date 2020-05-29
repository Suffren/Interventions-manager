# -*- coding: utf-8 -*-

import sqlite3

def main():
    conn = sqlite3.connect('reports.db')
    # Controls what objects are returned for the 'text' data type
    conn.text_factory = lambda x: x.decode('latin-1')
    cur = conn.cursor()
    cur.execute('CREATE TABLE reports (label text)')
    cur.execute("INSERT INTO reports VALUES('Ampoule defecteuse')")
    # Save
    conn.commit()
    cur.execute('SELECT * FROM reports')
    print cur.fetchall()
    conn.close()

# Ensure this module has not been imported
if __name__ == '__main__':
    main()