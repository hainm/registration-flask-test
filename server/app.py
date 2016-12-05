from flask import Flask
from flask import jsonify, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello there'

@app.route('/conda/name/<path:name>/institution/<path:institution>', methods=['GET', 'POST'])
def handle_registration(name, institution):
    user_info = dict(name=name, institution=institution)
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("INSERT INTO users (name,institution) VALUES (?,?)", (name, institution))
    return jsonify(user_info)

@app.route('/list')
def list_user():
   con = sqlite3.connect("database.db")
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   cur.execute("select * from users")
   rows = cur.fetchall()
   return render_template('user_list.html', rows=rows)

if __name__ == '__main__':
    app.run(port=8000)
