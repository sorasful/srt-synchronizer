from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import FileField, IntegerField, SubmitField, TextField, TextAreaField


class UploadForm(FlaskForm):
    file = FileField(validators=[FileAllowed(['srt'], '.srt only !')])
    text = TextAreaField()
    hours = IntegerField(default=0)
    minuts = IntegerField(default=0)
    seconds = IntegerField(default=0)
    miliseconds = IntegerField(default=0)

    submit = SubmitField()