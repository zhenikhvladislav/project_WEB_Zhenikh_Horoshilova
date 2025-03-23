from flask_wtf import FlaskForm
from wtforms.fields import EmailField
from wtforms.validators import DataRequired
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, BooleanField


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Создать')


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class MainInfoForm(FlaskForm):
    surname = TextAreaField('Фамилия *обязательное поле*')
    name = TextAreaField('Имя *обязательное поле*')
    patronymic = TextAreaField('Отчество *обязательное поле*')
