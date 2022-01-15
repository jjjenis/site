from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def draw_main_page():
    conn = get_db_connection()
    posts = conn.execute('SELECT * from posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/about')
def open_about():
    return render_template('about.html')


@app.route('/sth else')
def open_sth_else():
    return render_template('sthelse.html')


@app.route('/<int:post_id>')
def post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


if __name__ == '__main__':
    app.run()
