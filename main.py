from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user
from forms.user import RegisterForm, LoginForm
from data import db_session
from data.users import User

# Импорт всех нужных классов и модулей

app = Flask(__name__)
# Инициализирую LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'your_secret_key'


# Запуск сервера
def main():
    db_session.global_init("db/users.db")
    app.run(port=8080, host='127.0.0.1', debug=True)


# Функция получения пользователя
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():  # вместо reqister
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(email=form.email.data,
                    password=form.password.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        login_user(user, remember=True)  # Автоматически авторизуем пользователя после регистрации
        return redirect('/resume')  # Перенаправляем на страницу создания резюме
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect('/resume')  # Перенаправляем на страницу создания резюме
        return render_template('login.html', title="Неправильный пароль", form=form)
    return render_template('login.html', title="Авторизация", form=form)


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    main()
