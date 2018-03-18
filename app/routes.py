import os
from flask import render_template, request, flash, redirect, url_for, make_response
from werkzeug.utils import secure_filename

from app import app
from app.forms import UploadForm
from app.methods import convert_text_with_new_offset
from config import Config


@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()
    if form.validate_on_submit():
        hour_offset = form.data.get('hours', 0)
        minuts_offset = form.data.get('minuts', 0)
        seconds_offset = form.data.get('seconds', 0)
        miliseconds_offset = form.data.get('miliseconds', 0)
        offset = hour_offset, minuts_offset, seconds_offset, miliseconds_offset

        text_area_content = form.text.data
        if text_area_content != "":
            print(text_area_content)
            result = convert_text_with_new_offset(text_area_content, offset)
            response = make_response(result)
            response.headers["Content-Disposition"] = "attachment; filename={}".format("lolff.srt")
            return response

        if 'file' not in request.files:
            flash('No file part ...')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No file selected ...')
            return redirect(request.url)

        if file and file.filename.split('.')[-1] in Config.ALLOWED_EXTENSIONS:
            filename = secure_filename(file.filename)
            file_content = file.stream.read().decode('utf-16')  # TODO : See why it doens't pass thourh the regex ..
            result = convert_text_with_new_offset(file_content, offset)
            response = make_response((result))
            response.headers["Content-Disposition"] = "attachment; filename={}".format(filename)
            return response

    return render_template('index.html', form=form)
