from flask import Flask, render_template, request, redirect, url_for # Импортируем необходимые функции из библиотеки Flask
import random # Импортирем для перемешивание карточек
import json # Импортируем для передачи порядка карт

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
] # Список содержит правильный порядок карт, с которым будет сравниваться пользовательский порядок карт.

@app.route('/')
@app.route('/index') 
def index():
    return render_template('index.html') # Отображает страницу index.html

@app.route('/about') 
def about():
    return render_template('about.html') # Отображает страницу about.html

@app.route('/rules') 
def rules():
    return render_template('rules.html') # Отображает страницу rules.html

@app.route('/theory') 
def theory():
    return render_template('theory.html') # Отображает страницу theory.html

@app.route('/game', methods=['GET', 'POST']) # Этот маршрут может обрабатывать GET и POST запросы
def game():
    return render_template('game.html') # Отображает страницу game.html

@app.route('/control', methods=['GET', 'POST']) # Маршрут может обрабатывать GET и POST запросы
def control():
    if request.method == 'POST': # Если форма запроса POST , то:
        
        first_name = request.form.get('first_name') # Получеам имя , то которое ввёл пользователь
        last_name = request.form.get('last_name') # Получеам фамилию  , то которое ввёл пользователь

        shuffled_cards = CARDS_ORDER.copy() # Создаем копию списка CARDS_ORDER , чтобы сохранить оригинальный порядок карт
        random.shuffle(shuffled_cards) # Перемешиваем карты в случайном порядке

        return render_template('game.html', first_name=first_name, last_name=last_name, cards=shuffled_cards, moves=0) # Отображаем страницу game.html с переменными , которые ввёл пользователь(имя, фамилия) и количество ходов.
    return render_template('control.html') # Если метод GET , то отображается страница control.html

@app.route('/check_order', methods=['POST']) # Обрабатываем только POST запросы , поскольку метод POST используется для получения порядка карт от пользователя
def check_order():
    cards = request.form.get('cardsOrder') # Получаем пользовательский порядок карт из отправленной формы, используем ключ cardsOrder , чтобы извлечь значение
    moves = int(request.form.get('moves')) + 1 # Получаем из формы кол-во ходов и увеличиваем его на 1
    first_name = request.form.get('first_name') # Получаем из формы имя
    last_name = request.form.get('last_name') # Получаем из формы фамилию
    if cards: # Если карты переданы , то
        cards = json.loads(cards) # Преобразуем строку json в список Python

    if cards == CARDS_ORDER: # Если пользовательский порядок карт совпадает с оригинальным , то
        return render_template('victory.html', first_name=first_name, last_name=last_name, moves=moves) # Отображаем страницу victory.html
    else:
        return render_template('game.html', first_name=first_name, last_name=last_name, cards=cards, moves=moves) # Иначе отображаем страницу game.html с текущим порядком карт и количеством ходов

if __name__ == '__main__': # Данный блок выполняется , когда файл запускается напрямую
    app.run(debug=True, host='0.0.0.0') # Запускаем приложение
