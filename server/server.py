from flask import Flask, render_template, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def page():
    flats = get_flats()
    return render_template('index.html', flats=flats)

def get_db_connection():
    hostname = 'db'
    port = '5432'
    username = 'postgres'
    password = 'mojeGeslo1'
    database = 'sreality_flats'

    connection = psycopg2.connect(host=hostname, port=port, user=username, password=password, dbname=database)

    return connection

def get_flats():
    connection = get_db_connection()
    cur = connection.cursor()

    cur.execute("""
    SELECT title,images FROM flats
    """)

    flats = cur.fetchall()

    cur.close()
    connection.close()

    return flats

if __name__ == "__main__":
    app.run(host="web", port=8080, debug=True)