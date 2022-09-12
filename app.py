from flask import Flask, render_template, request, redirect
from game_of_life import GameOfLife
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['GET', 'POST'])
def index(width=50, height=50, error_text=''):
    if request.method == 'POST':
        if request.form['input_width'].isdigit() and request.form['input_height'].isdigit():
            width = int(request.form['input_width'])
            height = int(request.form['input_height'])
            GameOfLife(width, height)
            return redirect('/live')
        else:
            error_text = ' Параметры поля заданы неверно'
    GameOfLife(width, height)
    return render_template('index.html', error_text=error_text)


@app.route('/live')
def live():
    game = GameOfLife()
    game.form_new_generation()
    game.counter += 1
    return render_template('live.html', game=game)


if __name__ == '__main__':
    app.run(debug=True)
