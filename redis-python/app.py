from flask import Flask, request, redirect, url_for
import redis
from rq import Queue

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)
q = Queue(connection=r)

def background_task(n):
    """Funkcja, która zostanie wykonana w tle."""
    print(f'Wykonuję zadanie w tle: {n}')
    return f'zadanie {n} wykonane'

@app.route('/')
def index():
    return '<form action="/submit" method="post"><input name="n"><button type="submit">Dodaj zadanie</button></form>'

@app.route('/submit', methods=['POST'])
def submit():
    n = request.form.get('n', 1)
    job = q.enqueue(background_task, n)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)