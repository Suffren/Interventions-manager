# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect('reports.db')

cur = conn.cursor()
cur.execute('CREATE TABLE reports (label text)')
cur.execute("INSERT INTO reports VALUES('Ampoule defecteuse')")

# Save
conn.commit()

conn.close()