from flask import Flask, render_template, redirect, request, abort
import json
from data.jobs import Jobs
from data.users import User
from data.departments import Department
from data import db_session
from forms.register import RegisterForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from forms.login import LoginForm
from forms.jobs import JobsForm
from forms.test_form import TestForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    js = [json.loads(x) for x in open('passed.json').read().strip().split('\n') if x]
    db_sess = db_session.create_session()
    users = []
    for user in db_sess.query(User):
        for x in js:
            if user.name == x['name']:
                users.append(x)
    jobs = db_sess.query(Jobs)
    return render_template("index.html", users=users, jobs=jobs)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run()


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.name == form.name.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name = form.name.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm()
    if form.validate_on_submit():
        js = [json.loads(x) for x in open('passed.json').read().strip().split('\n') if x]
        d = {}
        d['name'] = form.name.data
        d['id'] = current_user.id
        d['task_1'] = form.task_1.data
        d['task_2'] = form.task_2.data
        d['task_3'] = form.task_3.data
        d['task_4'] = form.task_4.data
        d['task_5'] = form.task_5.data
        d['task_6'] = form.task_6.data
        d['task_7'] = form.task_7.data
        d['task_8'] = form.task_8.data
        js.append(d)
        file = open('passed.json', 'w')
        for x in js:
            file.write(f'{json.dumps(x)}\n')
        db_sess = db_session.create_session()
        users = db_sess.query(User).filter(User.id == current_user.id).first()
        if users:
            users.passed = True
            job = Jobs()
            job.passed = users.id
            db_sess.add(job)
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)

    return render_template('text.html', title='Тест', form=form)


@app.route('/answer/<user_id>')
def answer(user_id):
    db_sess = db_session.create_session()
    name = db_sess.query(User).filter(User.id == user_id).first().name
    users = [json.loads(x) for x in open('passed.json').read().strip().split('\n') if x]
    for x in users:
        if x['name'] == name:
            user = x
            break
    job = db_sess.query(Jobs).filter(Jobs.passed == user_id).first()
    return render_template('proverka.html', user=user, job=job)


@app.route('/edit/<job_id>/<number>/<answe>')
def edit(job_id, number, answe):
    answe = int(answe)
    job_id = int(job_id)
    number = int(number)
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == job_id).first()
    if answe == 1:
        if number == 1:
            job.task_1 = True
        elif number == 2:
            job.task_2 = True
        elif number == 3:
            job.task_3 = True
        elif number == 4:
            job.task_4 = True
        elif number == 5:
            job.task_5 = True
        elif number == 6:
            job.task_6 = True
        elif number == 7:
            job.task_7 = True
        elif number == 8:
            job.task_8 = True
    elif answe == 2:
        if number == 1:
            job.task_1 = False
        elif number == 2:
            job.task_2 = False
        elif number == 3:
            job.task_3 = False
        elif number == 4:
            job.task_4 = False
        elif number == 5:
            job.task_5 = False
        elif number == 6:
            job.task_6 = False
        elif number == 7:
            job.task_7 = False
        elif number == 8:
            job.task_8 = False
    else:
        if number == 1:
            job.task_1 = None
        elif number == 2:
            job.task_2 = None
        elif number == 3:
            job.task_3 = None
        elif number == 4:
            job.task_4 = None
        elif number == 5:
            job.task_5 = None
        elif number == 6:
            job.task_6 = None
        elif number == 7:
            job.task_7 = None
        elif number == 8:
            job.task_8 = None
    db_sess.commit()
    return redirect(f'/answer/{job.passed}')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.name == form.name.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


if __name__ == '__main__':
    main()
