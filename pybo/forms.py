from flask_wft import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    subject = StringField('タイトル', validators=[DataRequired('タイトルを入力してください。')])
    content = TextAreaField('内容', validators=[DataRequired('内容を入力してください。')])

class AnswerForm(FlaskForm):
    content = TextAreaField('内容', validators=[DataRequired('内容を入力してください。')])