# -*- coding: utf-8 -*-

import sqlite3
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

reports = [
    (0, "Nid-de-poule", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ut risus ac neque porttitor egestas. Nulla placerat id purus vel elementum.", "Doe", "Nantes", "2019-12-25"),
    (1, "Ampoule bureau à changer", "Aenean felis augue, malesuada sit amet ante in, sagittis bibendum nibh. In tristique gravida magna at suscipit. In commodo facilisis ipsum, ac aliquet purus lobortis quis. ", "Bordes", "Rennes", "2020-05-07")
]

def create_table(cur):
    try:
        # Create the table
        cur.execute('CREATE TABLE reports (id integer primary key, label text, description text, pro_lastname text, place text, date text)')
        # Fill the table
        cur.executemany('INSERT INTO reports VALUES(?, ?, ?, ?, ?, ?)', reports)
    except:
        print "SQLite warning: Table 'reports' already exists"

def main():
    conn = sqlite3.connect('reports.db')
    # Controls what objects are returned for the 'text' data type
    conn.text_factory = lambda x: x.decode('latin-1')
    # Create a cursor instance that allow to call methods to execute SQLite statements
    cur = conn.cursor()

    create_table(cur)

    # Save
    conn.commit()

    # REMOVE: Check reports
    cur.execute('SELECT * FROM reports')
    print cur.fetchall()

    conn.close()

# Ensure this module has not been imported
if __name__ == '__main__':
    main()

@app.route('/', methods=['GET'])
def home():
    return  '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for distant reading of science fiction novels.</p>'''


app.run()