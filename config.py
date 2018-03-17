import os

basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'THIS IS VERY SECRET !'
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = ['srt']
    MAX_CONTENT_LENGTH = 0.5 * 1024 * 1024  # 0.5 mb