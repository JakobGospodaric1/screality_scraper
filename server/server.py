from flask import Flask, render_template, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def page():
    flats = get_flats()
    #print first flat
    images_string = flats[0][1]

    images_string = images_string.strip('{}')

    images = images_string.split('"')
    #remove empty strings, and string with only comma
    images = [x for x in images if x != '']
    images = [x for x in images if x != ',']

    #change flats[i][1] to array of images
    for i in range(len(flats)):
        images_string = flats[i][1]

        images_string = images_string.strip('{}')

        images = images_string.split('"')
        #remove empty strings, and string with only comma
        images = [x for x in images if x != '']
        images = [x for x in images if x != ',']

        flats[i] = (flats[i][0], images)
        
    return render_template('index.html', flats=flats)

def get_db_connection():
    hostname = 'localhost'
    username = 'postgres'
    password = 'mojeGeslo1'
    database = 'sreality_flats'

    connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)

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
    app.run(debug=True)