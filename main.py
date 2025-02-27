from flask import Flask, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/image_sample')
def image():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.<p>
                  </body>
                </html>"""


@app.route('/')
def func():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/promotion')
def promotion():
    a = ['<h1>Человечество вырастает из детства.<h1>', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми '
                                                                                          'безжизненные '
                                                                                          'пока планеты.', 'И начнем с '
                                                                                                           'Марса!',
         'Присоединяйся!']
    countdown_list = [str(x) for x in a]
    return '<h1>'.join(countdown_list)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
