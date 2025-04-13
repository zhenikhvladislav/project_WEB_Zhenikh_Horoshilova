from flask import Flask, render_template, redirect, send_file
from flask_login import LoginManager, login_user, logout_user, login_required
from forms.user import RegisterForm, LoginForm
from data import db_session
from data.users import User
from flask_login import current_user
import pdfkit
from docx import Document

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'your_secret_key'


def main():
    db_session.global_init("db/users.db")
    app.run(port=8080, host='127.0.0.1', debug=True)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def register():
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
        login_user(user, remember=True)
        return redirect('/resume')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            return redirect('/resume')
        return render_template('login.html', title="Неправильный пароль", form=form)
    return render_template('login.html', title="Авторизация", form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@app.route('/download_pdf')
@login_required
def download_pdf():
    rendered = render_template('resume.html', user=current_user)
    pdf_path = 'static/resume.pdf'
    pdfkit.from_string(rendered, pdf_path)
    return send_file(pdf_path, as_attachment=True)


@app.route('/download_docx')
@login_required
def download_docx():
    doc = Document()
    doc.add_heading(f"Резюме — {current_user.email}", 0)
    doc.add_paragraph("Навыки: Python, Flask, SQL")
    doc.add_paragraph("Опыт: 2 года веб-разработки")
    doc_path = 'static/resume.docx'
    doc.save(doc_path)
    return send_file(doc_path, as_attachment=True)


@app.route('/samples')
def samples():
    return render_template('samples.html')


if __name__ == '__main__':
    main()
