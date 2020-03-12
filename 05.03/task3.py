from flask import Flask
from flask_login import LoginManager, login_user

from werkzeug.utils import redirect

from data import db_session, news_api
from data.Login_Form import LoginForm
from data.users import User
import datetime
from flask import render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = "yandex_secret_key"
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init('db/blogs.sqlite')
    app.register_blueprint(news_api.blueprint)
    session = db_session.create_session()
    app.run()

    session.commit()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = db_session.create_session()
        user = session.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    main()
