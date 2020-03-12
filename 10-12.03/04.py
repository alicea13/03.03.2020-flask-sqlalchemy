from flask import Flask, request, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from data import db_session, news_api
from data.Login_Form import LoginForm
from data.News_Form import NewsForm
from data.add_jobs import AddJobForm
from data.jobs import Jobs
from data.users import User
from data.news import News
from data.RegisterForm import RegisterForm
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


@app.route('/addjob', methods=['GET', 'POST'])
@login_required
def addJob():
    addform = AddJobForm()

    if addform.validate_on_submit():
        session = db_session.create_session()
        jobs = Jobs(
            job=addform.job.data,
            team_leader=addform.team_leader.data,
            work_size=addform.work_size.data,
            collaborators=addform.collaborators.data,
            is_finished=addform.is_finished.data
        )

        session.add(jobs)
        session.commit()
        return redirect('/')
    return render_template('add_job.html', title='Добавление работы', form=addform)
