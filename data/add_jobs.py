from flask_wtf import FlaskForm
from sqlalchemy_serializer import SerializerMixin
from wtforms import StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm, SerializerMixin):

    job = StringField('Название работы', validators=[DataRequired()])
    team_leader = IntegerField('ID Тим-Лида', validators=[DataRequired()])
    work_size = StringField('Размер работы', validators=[DataRequired()])
    collaborators = StringField('Работники', validators=[DataRequired()])
    is_finished = BooleanField('Работа закончена?')

    submit = SubmitField('Сдать')
