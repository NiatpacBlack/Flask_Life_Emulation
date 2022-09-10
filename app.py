from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index(width=35, height=35):
    GameOfLife(width, height)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(debug=True)
