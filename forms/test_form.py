from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField


class TestForm(FlaskForm):
    name = StringField('ник')
    task_1 = TextAreaField('Первое правило штурма')
    task_2 = TextAreaField('Назовите виды штурма и их особенности')
    task_3 = TextAreaField('Напишите рп ареста человека')
    task_4 = TextAreaField('''Вы привели задержанного в допросную, обыскали его, прикрепили к стулу.
    Как вы будете проводить допрос?''')
    task_5 = TextAreaField('''У вас ник Agent0...
    Вы видите как к вам подходит человек с ником Djulietta666. Что нужно ему сказать?''')
    task_6 = TextAreaField('Что нужно говорить, когда вас хвалит начальство?')
    task_7 = TextAreaField('Кого вы должны отыгрывать?')
    task_8 = TextAreaField('Назовите несколько пунктов из раздела "Применение физической силы"')
    task_9 = TextAreaField(None)
    task_10 = TextAreaField(None)
    task_11 = TextAreaField(None)
    task_12 = TextAreaField(None)
    task_13 = TextAreaField(None)
    task_14 = TextAreaField(None)
    submit = SubmitField('Submit')
