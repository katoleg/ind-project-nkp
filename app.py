from flask import Flask, render_template, request, redirect, url_for
import random
import json

app = Flask(__name__)

CARDS_ORDER = [
    "Поиск «мишени» для лекарства",
    "Выбор вещества, которое будет действовать на мишень",
    "Доклинические исследования Исследование на клетках",
    "Доклинические исследования Улучшение веществ-кандидатов",
    "Доклинические исследования лекарств Исследование на уровне целого организма",
    "Клинические исследования лекарств Первая фаза",
    "Клинические исследования лекарств Вторая фаза",
    "Клинические исследования лекарств Третья фаза",
    "Регистрация лекарств",
    "Производство лекарств",
    "Применение лекарств",
    "Клинические исследования лекарств Четвертая фаза"
]
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

@app.route('/theory')
def theory():
    return render_template('theory.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html')

@app.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')

        shuffled_cards = CARDS_ORDER.copy()
        random.shuffle(shuffled_cards)

        return render_template('game.html', first_name=first_name, last_name=last_name, cards=shuffled_cards, moves=0)
    return render_template('control.html')

@app.route('/check_order', methods=['POST'])
def check_order():
    cards = request.form.get('cardsOrder')
    moves = int(request.form.get('moves')) + 1
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')

    if cards:
        cards = json.loads(cards)

    if cards == CARDS_ORDER:
        return render_template('victory.html', first_name=first_name, last_name=last_name, moves=moves)
    else:
        return render_template('game.html', first_name=first_name, last_name=last_name, cards=cards, moves=moves)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
