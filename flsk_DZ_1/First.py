from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ijqweshnfdciwuehdfioqwuhef'
menu = [{"name": "Главная", "url": "index"},
        {"name": "О нас", "url": "about"},
        {"name": "Обратная связь", "url": "contact"}]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="О нас", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        # print(request.form)  # можно указать ключ ([username])
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        # return render_template('contact.html', **context, title="Обратная связь", menu=menu)
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено успешно', category="success")
        else:
            flash('Ошибка отправки', category="error")
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/profile/<path:username>")
def profile(username):
    return f'Пользователь: {username}'


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('about'))
#     print(url_for('profile', username='Stas'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)

if __name__ == "__main__":
    app.run(debug=True)
