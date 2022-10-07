from flask import request, redirect
from app import app
from app.db import get_db
import sqlite3 
import sqlite3 as sql
from flask import g
from app.user import User

@app.route('/')
def route():
    return 'Hi!'

@app.route('/example', methods=['GET', 'POST'])
def example():
    db = get_db()
    if request.method == 'POST':
        db.execute('INSERT INTO Example (contents) VALUES (?)', (request.form['message'],))
        db.commit()
    messages = db.execute('SELECT * FROM Example').fetchall()
    return {'messages': list(map(dict, messages))}

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = get_db()
    if request.method == 'POST':
        email = request.form['email']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        password = request.form['password']
        address = request.form['address']
    User.registerUser(firstName, lastName, email, password, address, db)
    return redirect('/register')

@app.route('/search', methods=['GET', 'POST'])
def search():
    db = get_db()
    if request.method == 'POST':
        messages = db.execute("SELECT * FROM Example WHERE contents like ?", ["%" + request.form['message'] + "%"] ).fetchall()
    else:
        messages = db.execute('SELECT * FROM Example').fetchall()
    return {'messages': list(map(dict, messages))}
    
    
@app.route('/Create_Group', methods=['POST', 'GET'])
def Create_Group():
    db = get_db()
    if request.method == 'POST':
        db.execute("CREATE TABLE Groups (id INTEGER PRIMARY KEY AUTOINCREMENT, Size INTEGER, Username TEXT, User_id TEXT)")
        db.execute('''
            INSERT INTO Groups ( Size, Username, User_id )
            VALUES
            ( 1, "ding", "2")
            ''')
        db.commit()
    
        
    return {'messages': [request.method]}
if __name__ == '__main__':
    app.debug = True
    app.run()
