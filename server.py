from flask import Flask, render_template, request
from flask_cors import CORS

app = Flask(__name__)


cors = CORS(app, resources={r"/<genre>/*": {"origins": "*"}})

# All the python functions to create app routes on the flask server. All of these are referenced in the javascript
# functions in the HTML File

@app.route('/<genre>/<num>', methods = ["GET"])
def select_by_genre(genre, num):
    import sqlite3
    conn = sqlite3.connect('instance/songs.db')
    c = conn.cursor()
    c.execute("SELECT track_name, artist_name, genre FROM songs WHERE genre = ? ORDER BY RANDOM() LIMIT ?;", (genre, num))
    results = c.fetchall()
    list = []
    for row in results:
        list.append(row)
    conn.close()
    return list

@app.route('/artist/<artist>/<num>', methods = ["GET"])
def select_by_artist(artist, num):
    import sqlite3
    conn = sqlite3.connect('instance/songs.db')
    c = conn.cursor()
    c.execute("SELECT track_name, artist_name, genre FROM songs WHERE artist_name = ? ORDER BY RANDOM() LIMIT ?;", (artist, num))
    results = c.fetchall()
    list = []
    for row in results:
        list.append(row)
    conn.close()
    return list

@app.route('/all', methods = ["GET"])
def get_all():
    import sqlite3
    conn = sqlite3.connect('instance/songs.db')
    c = conn.cursor()
    c.execute("SELECT * FROM songs")
    results = c.fetchall()
    return results

genreList = ['Movie', 'R&B', 'A Capella', 'Alternative', 
             'Country', 'Dance', 'Electronic', 'Anime', 
             'Blues', 'Folk', 'Opera', 'Soul', 'Hip-Hop', 
             'Pop', 'Classical', 'Reggae', 'Jazz']

@app.route('/random', methods = ["GET"])
def recommendGenre():
    import random
    rgenre = random.choice(genreList)
    return rgenre


if __name__ == '__main__':
    app.run(debug=True, port=8000)
