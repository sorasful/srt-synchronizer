import os

basedir = os.path.abspath(os.path.dirname(__name__))


class Config:
    SECRET_KEY = os.getenv('FLASK_SECRET_KEY') or 'THIS IS VERY SECRET !'
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER') or os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = ['srt']
    MAX_CONTENT_LENGTH = os.getenv('MAX_CONTENT_LENGHT') or 0.5 * 1024 * 1024  # 0.5 mb
    DEBUG = os.getenv('DEBUG_ACTIVATED') or False
    HOST = os.getenv('HOST') or '0.0.0.0'
