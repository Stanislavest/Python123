import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase

# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '58b70843644df96b63bd463de34754f7e72ca77a'
# в консоли: import os  ==>  os.urandom(20).hex()

# from flsk.first import create_db
# create_db()


app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'flsk.db')))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g, 'link_db'):  # g - контекст приложения
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if len(request.form['name']) > 4 and len(request.form['post']) > 10:
            res = dbase.add_post(request.form['name'], request.form['post'])
            if not res:
                flash("Ошибка добавления статьи", category='error')
            else:
                flash("Статья добавлена успешно", category='success')
        else:
            flash("Ошибка добавления статьи", category='error')

    return render_template("add_post.html", title="Добавление статьи", menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)
    return render_template("post.html", title=title, post=post, menu=dbase.get_menu())


# @app.route("/about")
# def about():
#     return render_template("about.html", title="О нас", menu=[])
#
#
# @app.route("/contact", methods=["POST", "GET"])
# def contact():
#     if request.method == "POST":
#         # print(request.form)  # можно указать ключ ([username])
#         # context = {
#         #     'username': request.form['username'],
#         #     'email': request.form['email'],
#         #     'message': request.form['message']
#         # }
#         # return render_template('contact.html', **context, title="Обратная связь", menu=menu)
#         if len(request.form['username']) > 2:
#             flash('Сообщение отправлено успешно', category="success")
#         else:
#             flash('Ошибка отправки', category="error")
#     return render_template('contact.html', title="Обратная связь", menu=[])
#
#
# @app.route("/profile/<path:username>")
# def profile(username):
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#     return f'Пользователь: {username}'
#
# # with app.test_request_context():
# #     print(url_for('index'))
# #     print(url_for('about'))
# #     print(url_for('profile', username='Stas'))
#
#
# # @app.route("/login", methods=["POST", "GET"])
# # def login():
# #     if 'userLogged' in session:
# #         return redirect(url_for('profile', username=session['userLogged']))
# #     elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['passw'] == '123456':
# #         session['userLogged'] = request.form['username']
# #         return redirect(url_for('profile', username=session['userLogged']))
# #     return redirect(url_for('login.html', title="Авторизация", menu=menu))
#
#
# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if 'userLogged' in session:
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['passw'] == '123456':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for('profile', username=session['userLogged']))
#     return render_template('login.html', title="Авторизация", menu=[])
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page404.html', title="Страница не найдена", menu=[])


if __name__ == "__main__":
    app.run(debug=True)
