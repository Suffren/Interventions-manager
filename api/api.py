# -*- coding: utf-8 -*-

import datetime
import sqlite3
import flask
from flask import request, abort, jsonify
# Make cross-origin AJAX possible
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
cors = CORS(app)
app.config["DEBUG"] = True
# Allow POST requests with a JSON content type to browsers
app.config['CORS_HEADERS'] = 'Content-Type'

reports = [
    (0, "Nid-de-poule", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ut risus ac neque porttitor egestas. Nulla placerat id purus vel elementum.", "Doe", "Nantes", "2020-06-25", 'valid'),
    (1, "Ampoule bureau à changer", "Aenean felis augue, malesuada sit amet ante in, sagittis bibendum nibh. In tristique gravida magna at suscipit. In commodo facilisis ipsum, ac aliquet purus lobortis quis. ", "Bordes", "Rennes", "2020-10-07", 'valid'),
    (2, "Mobilier cassé", "", "Dupond", "Vannes", "2019-05-07", 'archived')
]

def create_table(cur):
    try:
        # Create the table
        cur.execute('CREATE TABLE reports (id integer primary key, label text, description text, pro_lastname text, place text, date text, status text)')
        # Fill the table
        cur.executemany('INSERT INTO reports VALUES(?, ?, ?, ?, ?, ?, ?)', reports)
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
    conn.close()

# Return an object with columns names as keys
# See https://docs.python.org/2.7/library/sqlite3.html#connection-objects, 'row_factory' section
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Ensure this module has not been imported
if __name__ == '__main__':
    main()

@app.errorhandler(404)
def error_handler(err):
    return jsonify(error = str(err)), 404

@app.route('/', methods=['GET'])
def home():
    return  '''<h1>Distant Reading Archive</h1>
            <p>A prototype API for distant reading of science fiction novels.</p>'''

# route() decorator binds a function to a URL
@app.route('/api/v1/reports', methods=['GET'])
# Allow all origins, all methods
@cross_origin()
def api_all():
    conn = sqlite3.connect('reports.db')
    # Format a SQL row to a readable dictionary
    conn.row_factory = dict_factory
    # Cursor allows to perform database operations
    cur = conn.cursor()
    all_reports = cur.execute('SELECT * FROM reports').fetchall()

    return jsonify(all_reports)

@app.route('/api/v1/report', methods=['GET'])
@cross_origin()
def report_by_id():
    query_parameters = request.args
    id = query_parameters.get('id')

    if id:
        id = str(id)
    else:
        return abort(404, description = "Resource not found.")

    conn = sqlite3.connect('reports.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    query = 'SELECT * FROM reports WHERE id={}'.format(id)
    report = cur.execute(query).fetchone()
    return jsonify(report)

@app.route('/api/v1/delete_report', methods=['POST'])
@cross_origin()
def delete_report():
    query_parameters = request.args
    id = query_parameters.get('id')

    if id:
        id = str(id)
    else:
        return abort(404, description = "Resource not found.")

    conn = sqlite3.connect('reports.db')
    cur = conn.cursor()
    query = 'DELETE FROM reports WHERE id={}'.format(id)
    cur.execute(query)
    conn.commit()
    conn.close()

    return jsonify(data = "success")

@app.route('/api/v1/add_report', methods=['POST'])
@cross_origin()
def add_report():
    label = request.form.get('label')
    description = request.form.get('description')
    date = request.form.get('date')
    pro_lastname = request.form.get('pro_lastname')
    place = request.form.get('place')
    status = "draft"

    report_ISODate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    now = datetime.date.today()

    # Set the status to 'valid' if all inputs have been registered
    if all(request.form.values()):
        status = 'valid'
    # The intervention has passed
    if now > report_ISODate:
        status = 'archived'

    conn = sqlite3.connect('reports.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute('INSERT INTO reports VALUES(?, ?, ?, ?, ?, ?, ?)', (None, label, description, pro_lastname, place, date, status))

    conn.commit()
    conn.close()

    return jsonify(data = "success")

@app.route('/api/v1/update_report', methods=['POST'])
@cross_origin()
def update_report():
    label = request.form.get('label')
    description = request.form.get('description')
    date = request.form.get('date')
    pro_lastname = request.form.get('pro_lastname')
    place = request.form.get('place')

    query_parameters = request.args
    id = query_parameters.get('id')

    if id:
        id = str(id)
    else:
        return abort(404, description = "Resource not found.")

    report_ISODate = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    now = datetime.date.today()

    conn = sqlite3.connect('reports.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    # Update the status if all inputs have been registered
    if all(request.form.values()) and report_ISODate > now:
        status = 'valid'
    # The intervention has passed
    elif now > report_ISODate:
        status = 'archived'
    else:
        status = 'draft'

    cur.execute('UPDATE reports SET label=?, description=?, date=?, pro_lastname=?, place=?, status=? WHERE id=?', (label, description, date, pro_lastname, place, status, id))

    # Get & return the updated report
    query = 'SELECT * FROM reports WHERE id={}'.format(id)
    report = cur.execute(query).fetchone()

    conn.commit()
    conn.close()
    return jsonify(report)

app.run()