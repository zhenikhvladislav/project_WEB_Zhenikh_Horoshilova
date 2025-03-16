from flask import Flask, render_template
from flask_login import LoginManager, login_user
from forms.user import RegisterForm
from data import db_session
from data.users import User
# Импорт всех нужных классов и модулей

app = Flask(__name__)
# Инициализирую LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'resume_web_secret_key'


# Запуск сервера
def main():
    app.run(port=8080, host='127.0.0.1')


# Функция получения пользователя
@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(email=form.email.data,
                    password = form.password.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    main()
